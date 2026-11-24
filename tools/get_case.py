#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-gtopt-commercial
"""Download the source files of a case and convert them with the pinned flags.

    tools/get_case.py pcp 2026-06-03   # -> chile/daily_scheduling/pcp_<date>/
    tools/get_case.py plp 2026-05-15   # -> chile/medium_long_term/plp_<date>/
    tools/get_case.py rebuild pcp_2025-10-19 --res RES20251019.zip.xz --out ~/x
    tools/get_case.py fetch sem_2025w03  # data not redistributed: download
    tools/get_case.py fetch pcp_2024-09-01  # CEN day from coordinador.cl
    tools/get_case.py fetch nrel118_2024w01 # benchmark: pinned upstream files

All the work is done by the gtopt Python tools, installed from a gtopt
checkout (``pip install -e <gtopt>/scripts``) and called here as console
scripts: ``cen2gtopt-pcp-archive`` (CEN portal), ``plexos2gtopt``,
``plp2gtopt``, ``plp_compress_case``, ``sddp2gtopt`` and ``psse2gtopt``.
Converter, flags, line lifts and profile come from ``catalog.json``.

Files are only downloaded when not already local.  Inputs land in the
case directory (``source/``, ``case/``); the PLEXOS solution bundle
(``RES<date>.zip``, a result needed only for the block layout) stays in
``$GTOPT_CASES_CACHE`` (default ``~/.cache/gtopt-cases``), outside the
repository.  ``fetch`` downloads the publisher's archives of a case whose
data are not redistributed here (``source.redistributed: false``) into
the cache, checks their sha256 and extracts the members the converter
reads into the (git-ignored) ``source/`` of the case (plain files and
``sha256sum``-style manifests of files at a pinned upstream commit are
downloaded straight into ``source/``); ``cache_members``
(e.g. the PLEXOS solution bundle) are extracted next to the archive in
the cache.  On a CEN PCP day whose input bundle is in ``source/``,
``fetch`` checks its sha256 and runs ``pcp``.  The CEN portal
only serves Chilean IP addresses.  Cases are
provided AS IS (see DISCLAIMER.md); run them as the READMEs show.
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import lzma
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
CACHE = Path(os.environ.get("GTOPT_CASES_CACHE", "~/.cache/gtopt-cases")).expanduser()
DROP = {"README.md", "logs", "plexos2gtopt_state.json", "plp2gtopt_state.json"}
SIDE = (".provenance.json", "_state.json", "_report.json", ".plexos_model.json")
OUTPUT_ONLY = {"output_compression", "output_format", "write_out"}


def run(*cmd: str | Path, cwd: Path | None = None) -> None:
    """Run a gtopt console script; stop on failure."""
    print("+", shlex.join(map(str, cmd)), flush=True)
    if shutil.which(str(cmd[0])) is None:
        sys.exit(f"{cmd[0]} not found: pip install -e <gtopt checkout>/scripts")
    subprocess.run([str(c) for c in cmd], check=True, cwd=cwd)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def catalog_entry(key: str) -> dict[str, Any] | None:
    """Catalog case by id, path, last path component or date."""
    for c in load(REPO / "catalog.json")["cases"]:
        if key in (c["id"], c["path"], c["id"].rsplit("/", 1)[-1], c.get("date")):
            return c
    return None


def new_entry(application: str, stem: str, date: str) -> dict[str, Any]:
    """Entry for an uncatalogued day, from ``converter_defaults``."""
    d = load(REPO / "catalog.json")["converter_defaults"][application]
    conv = {"tool": d["tool"], "flags": list(d["flags"])}
    if "lifts" in d:
        conv["lifts"] = {"mode": d["lifts"]["mode"], "file": d["lifts"]["file"]}
    folder = f"chile/{application}/{stem}_{date}"
    return {
        "id": folder,
        "path": folder,
        "date": date,
        "case_json": f"case/{stem}_{date}.json",
        "profile": f"profiles/{application}.json",
        "converter": conv,
    }


def lift_flags(entry: dict[str, Any], mode: str | None) -> list[str]:
    """``--lift-line-caps`` for lift mode case|common|union|none."""
    lifts = entry["converter"].get("lifts") or {}
    mode = mode or lifts.get("mode", "none")
    if mode == "none":
        return []
    table = load(REPO / lifts.get("file", "chile/daily_scheduling/line_lifts.json"))
    if mode == "case":
        names = table["per_case"].get(entry.get("date"))
        if names is None:
            print(f"no per-case lift list for {entry.get('date')}: using common")
            names = table["common"]
    else:
        names = table[mode]
    return ["--lift-line-caps", ",".join(names)]


def postprocess(
    raw: Path, dest: Path, name: str, profile: Path | None, drop: list[str]
) -> Path:
    """Copy converter output to ``dest``: profile options and ``drop``
    keys (dotted paths) stripped, no side files, solver-file comments and
    build-machine paths removed."""
    jsons = [p for p in raw.glob("*.json") if not p.name.endswith(SIDE)]
    if len(jsons) != 1:
        sys.exit(f"expected one planning JSON in {raw}, got {jsons}")
    case = load(jsons[0])
    conflicts: list[str] = []

    def strip(c: dict[str, Any], p: dict[str, Any], path: str) -> None:
        for k, pv in p.items():
            if k not in c:
                continue
            if isinstance(pv, dict) and isinstance(c[k], dict):
                strip(c[k], pv, f"{path}{k}.")
                if c[k]:
                    continue
            elif c[k] != pv and k not in OUTPUT_ONLY:
                conflicts.append(f"{path}{k}: case={c[k]!r} profile={pv!r}")
            del c[k]

    if profile is not None:
        strip(case.setdefault("options", {}), load(profile).get("options", {}), "")
    if conflicts:
        sys.exit("profile would change the model:\n  " + "\n  ".join(conflicts))
    for key in drop:
        *parents, leaf = key.split(".")
        node = case
        for k in parents:
            node = node.get(k, {})
        node.pop(leaf, None)
    notice = dest / "NOTICE.md"  # rights notice: kept across rebuilds
    kept = notice.read_bytes() if notice.is_file() else None
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    if kept is not None:
        notice.write_bytes(kept)
    for item in raw.iterdir():
        if item.name in DROP or item == jsons[0]:
            continue
        copy = shutil.copytree if item.is_dir() else shutil.copy2
        copy(item, dest / item.name)
    (dest / name).write_text(
        json.dumps(case, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    for prm in (dest / "solvers").glob("*"):
        lines = prm.read_text(encoding="utf-8").splitlines()
        keep = [ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]
        prm.write_text("\n".join(keep) + "\n", encoding="utf-8")
    for rep in dest.glob("*.json"):
        text = rep.read_text(encoding="utf-8")
        new = re.sub(r'"/(?:home|tmp)/[^"]*/([^"/]+)"', r'"\1"', text)
        if new != text:
            rep.write_text(new, encoding="utf-8")
    return dest / name


SPLIT = re.compile(r"^(?P<base>.+)\.(?P<n>\d+)(?P<ext>\.xz)$")


def stage_input(inp: Path, overlay: Path | None, stage: Path) -> Path:
    """Converter input directory assembled in ``stage``: the files of
    ``inp`` (symlinked), then those of ``overlay`` (replacing same-named
    ones), with split parts ``<name>.<N>.xz`` concatenated back into
    ``<name>.xz`` (each part is a complete xz stream)."""
    stage.mkdir(parents=True)
    files = {p.name: p for p in sorted(inp.iterdir()) if p.is_file()}
    if overlay is not None:
        files |= {p.name: p for p in sorted(overlay.iterdir()) if p.is_file()}
    parts: dict[str, list[tuple[int, Path]]] = {}
    for name, path in files.items():
        m = SPLIT.match(name)
        if m:
            parts.setdefault(m["base"] + m["ext"], []).append((int(m["n"]), path))
        else:
            (stage / name).symlink_to(path.resolve())
    for name, chunks in parts.items():
        with (stage / name).open("wb") as fo:
            for _, path in sorted(chunks):
                fo.write(path.read_bytes())
    return stage


def decompress_input(inp: Path, stage: Path) -> Path:
    """Copy of ``inp`` (a file or a directory) in ``stage`` with every
    ``.xz`` / ``.gz`` file decompressed; returns the staged path."""
    stage.mkdir(parents=True)
    files = sorted(inp.iterdir()) if inp.is_dir() else [inp]
    base = stage / inp.name if inp.is_dir() else stage
    base.mkdir(exist_ok=True)
    out = base
    for f in files:
        if not f.is_file():
            continue
        if f.suffix in (".xz", ".gz"):
            opener = lzma.open if f.suffix == ".xz" else gzip.open
            target = base / f.name[: -len(f.suffix)]
            with opener(f, "rb") as fi, target.open("wb") as fo:
                shutil.copyfileobj(fi, fo)
        else:
            target = base / f.name
            shutil.copy2(f, target)
        if not inp.is_dir():
            out = target
    return out


def download(url: str, dest: Path, sha256: str) -> None:
    """``url`` to ``dest`` unless already there; check its sha256."""
    if not (dest.is_file() and hashlib.sha256(dest.read_bytes()).hexdigest() == sha256):
        print(f"+ download {url}", flush=True)
        dest.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "gtopt"})
        with urllib.request.urlopen(req) as r, dest.open("wb") as fo:
            shutil.copyfileobj(r, fo)
    if hashlib.sha256(dest.read_bytes()).hexdigest() != sha256:
        sys.exit(f"{dest}: sha256 differs from catalog.json")


def fetch_files(entry: dict[str, Any]) -> None:
    """Plain files (``url`` + ``path``) and pinned upstream manifests
    (``manifest``: base URL + sha256sum-style file) into the case dir."""
    case_dir = REPO / entry["path"]
    for f in entry["source"]["files"]:
        if "manifest" in f:
            dest = case_dir / f.get("dest", "source")
            for line in (case_dir / f["manifest"]).read_text().splitlines():
                digest, _, rel = line.partition("  ")
                name = rel.rsplit("/", 1)[-1] if f.get("flat") else rel
                url = f"{f['base_url']}/{urllib.parse.quote(rel)}"
                download(url, dest / name, digest)
        elif "url" in f and "path" in f:
            download(f["url"], case_dir / f["path"], f["sha256"])


def convert(entry: dict[str, Any], args: argparse.Namespace) -> Path:
    """Run the catalogued converter on the case source; returns the JSON."""
    case_dir = REPO / entry["path"]
    # source-only cases have no catalogued case_json: name it after the case
    name = entry["path"].rsplit("/", 1)[-1]
    conv = entry["converter"]
    case_json = Path(entry.get("case_json") or f"case/{name}.json")
    dest = Path(args.out).expanduser() if args.out else case_dir / case_json.parent
    if dest.resolve() == case_dir.resolve():
        sys.exit("case JSON lives at the case root: pass --out")
    profile = REPO / entry["profile"] if entry.get("profile") else None
    src = Path(args.source).expanduser() if args.source else None
    inp = (src or case_dir / conv.get("input", "source")).resolve()
    needs_input = not conv.get("argv") or any("{input}" in a for a in conv["argv"])
    if needs_input and not inp.exists():
        sys.exit(f"no {inp}: pass --source")
    with tempfile.TemporaryDirectory(prefix="get-case-") as tmp:
        raw = Path(tmp) / "out" / case_json.stem
        flags = [*conv["flags"], *getattr(args, "extra", [])]
        overlay = conv.get("overlay")
        if inp.is_dir() and (overlay or conv.get("join_parts")):
            ovl = (case_dir / overlay).resolve() if overlay else None
            inp = stage_input(inp, ovl, Path(tmp) / "in")
        cwd = inp if inp.is_dir() else inp.parent
        if conv.get("decompress") and needs_input:  # .xz / .gz files
            inp = decompress_input(inp, Path(tmp) / "plain")
        if "argv" in conv:  # converter with its own command line
            raw.mkdir(parents=True)
            subst = {
                "input": str(inp),
                "out_dir": str(raw),
                "out_json": str(raw / case_json.name),
                "gtopt_src": os.environ.get("GTOPT_SRC", "<set GTOPT_SRC>"),
            }
            argv = [a.format(**subst) for a in conv["argv"]]
            if any("<set GTOPT_SRC>" in a for a in argv):
                sys.exit("set GTOPT_SRC to a gtopt checkout (see the case README)")
            run(*argv, *getattr(args, "extra", []), cwd=Path(tmp))
            sub = raw / case_json.stem  # time series next to the JSON instead
            if conv.get("flatten") and sub.is_dir():
                for item in sub.iterdir():
                    shutil.move(item, raw / item.name)
                sub.rmdir()
            out = postprocess(raw, dest, case_json.name, profile, conv.get("drop", []))
            print_run(entry, out, profile)
            return out
        if conv.get("rename_input"):  # the input name names the planning JSON
            stage = Path(tmp) / "in"
            stage.mkdir()
            (stage / f"{case_json.stem}{inp.suffix}").symlink_to(inp)
            inp, cwd = stage / f"{case_json.stem}{inp.suffix}", case_dir
        elif conv["tool"] == "plexos2gtopt":
            d8 = entry["date"].replace("-", "")
            stage = Path(tmp) / case_json.stem  # names the planning JSON
            stage.mkdir()
            names = (f"DATOS{d8}.zip.xz", f"DATOS{d8}.zip")  # kept or fetched
            datos = next((p for n in names if (p := inp / n).is_file()), inp / names[0])
            (stage / datos.name).symlink_to(datos)
            res = args.res or next(iter(sorted((CACHE / d8).glob("RES*.zip*"))), None)
            if res is not None:
                (stage / Path(res).name).symlink_to(Path(res).expanduser().resolve())
            elif not args.allow_hourly:
                sys.exit(f"no RES{d8}.zip: pass --res, or run `pcp {entry['date']}`")
            flags += lift_flags(entry, args.lifts)
            inp = cwd = stage
        run(conv["tool"], "-i", inp, "-o", raw, *flags, cwd=cwd)
        out = postprocess(raw, dest, case_json.name, profile, conv.get("drop", []))
    print_run(entry, out, profile)
    return out


def print_run(entry: dict[str, Any], case_json: Path, profile: Path | None) -> None:
    """The gtopt command that runs the built case, output outside the repo."""
    out = f"~/gtopt-cases-out/{entry['path']}/output"
    gtopt = ["gtopt", str(case_json), *([str(profile)] if profile else [])]
    gtopt += ["--set", f"input_directory={case_json.parent}", "-d", "."]
    print(f"run:\n  ulimit -c unlimited\n  mkdir -p {out} && cd {out}")
    print("  " + shlex.join(gtopt))


def cmd_pcp(args: argparse.Namespace) -> Path:
    date = dt.date.fromisoformat(args.date).isoformat()
    d8 = date.replace("-", "")
    entry = catalog_entry(f"pcp_{date}") or new_entry("daily_scheduling", "pcp", date)
    datos = REPO / entry["path"] / "source" / f"DATOS{d8}.zip.xz"
    dl = CACHE / d8
    have_res = args.res or list(dl.glob("RES*.zip*"))
    if not datos.exists() or not (have_res or args.allow_hourly):
        if not (dl / f"DATOS{d8}.zip").exists():
            run("cen2gtopt-pcp-archive", "pcp-day", date, "--dest", dl)
        if not datos.exists():
            datos.parent.mkdir(parents=True, exist_ok=True)
            with (dl / f"DATOS{d8}.zip").open("rb") as fi:
                datos.write_bytes(lzma.compress(fi.read(), preset=9))
    return convert(entry, args)


def cmd_plp(args: argparse.Namespace) -> Path | None:
    date = dt.date.fromisoformat(args.date).isoformat()
    entry = catalog_entry(f"plp_{date}") or new_entry("medium_long_term", "plp", date)
    source = REPO / entry["path"] / "source"
    pick = ["--name", args.name] if args.name else []
    if args.dry_run:
        run("cen2gtopt-pcp-archive", "plp-in-force", date, "--dry-run", *pick)
        return None
    if not any(source.glob("plpblo.dat*")):
        run("cen2gtopt-pcp-archive", "plp-in-force", date, "--extract", source, *pick)
        run("plp_compress_case", source)
    return convert(entry, args)


def cmd_fetch(args: argparse.Namespace) -> Path:
    """Download, check and extract the publisher's archives, then convert."""
    entry = catalog_entry(args.case)
    if entry is None:
        sys.exit(f"{args.case}: no such case in catalog.json")
    if entry["source"].get("redistributed", True):
        if entry.get("converter", {}).get("tool") != "plexos2gtopt":
            sys.exit(f"{args.case}: source/ is in the repository: use rebuild")
        for f in entry["source"]["files"]:  # PCP day: input bundle in source/
            path = REPO / entry["path"] / f["path"]
            if hashlib.sha256(path.read_bytes()).hexdigest() != f["sha256"]:
                sys.exit(f"{path}: sha256 differs from catalog.json")
        args.date = entry["date"]
        return cmd_pcp(args)
    if entry["source"].get("fetched_by") == "converter":
        return convert(entry, args)  # the converter downloads + checks them
    archives = [f for f in entry["source"]["files"] if "archive" in f]
    if len(archives) < len(entry["source"]["files"]):
        fetch_files(entry)
    # cases that share the same archives name a common "cache" folder
    key = entry["source"].get("cache") or entry["id"].rsplit("/", 1)[-1]
    case_dir, dl = REPO / entry["path"], CACHE / key
    for f in archives:
        archive = dl / f["archive"]
        if not archive.is_file():
            print(f"+ download {f['url']}", flush=True)
            dl.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(f["url"], headers={"User-Agent": "gtopt"})
            with urllib.request.urlopen(req) as r, archive.open("wb") as fo:
                shutil.copyfileobj(r, fo)
        if hashlib.sha256(archive.read_bytes()).hexdigest() != f["sha256"]:
            sys.exit(f"{archive}: sha256 differs from catalog.json")
        # members -> case dir (git-ignored); cache_members (results) -> cache
        targets = [(m, case_dir / p) for m, p in f["members"].items()]
        targets += [(m, dl / p) for m, p in f.get("cache_members", {}).items()]
        with zipfile.ZipFile(archive) as z:
            for member, out in targets:
                out.parent.mkdir(parents=True, exist_ok=True)
                with z.open(member) as zi, out.open("wb") as fo:
                    shutil.copyfileobj(zi, fo)
    return convert(entry, args)


def cmd_rebuild(args: argparse.Namespace) -> Path:
    entry = catalog_entry(args.case)
    if entry is None or not entry.get("case_json"):
        sys.exit(f"{args.case}: no such case in catalog.json")
    return convert(entry, args)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    pcp = sub.add_parser("pcp", help="CEN PCP day (PLEXOS -> gtopt)")
    plp = sub.add_parser("plp", help="CEN PLP bundle in force on a date")
    reb = sub.add_parser("rebuild", help="reconvert a catalogued case from source/")
    fet = sub.add_parser("fetch", help="download a not-redistributed case + convert")
    pcp.add_argument("date", help="YYYY-MM-DD")
    plp.add_argument("date", help="YYYY-MM-DD")
    reb.add_argument("case", help="case id, path, name or date")
    fet.add_argument("case", help="case id, path or name")
    plp.add_argument("--name", help="force a CEN file (e.g. IPLP_20260401.zip)")
    plp.add_argument("--dry-run", action="store_true", help="only print the choice")
    plp.add_argument("--plp2gtopt-arg", dest="extra", action="append", default=[])
    for p in (pcp, plp, reb, fet):
        p.add_argument("--out", help="case/ output directory (default: in place)")
        p.add_argument("--source", help="converter input instead of source/")
        p.add_argument("--res", help="PLEXOS RES<date>.zip[.xz] (block layout)")
        p.add_argument("--lifts", choices=("case", "common", "union", "none"))
        p.add_argument("--allow-hourly", action="store_true", help="no RES needed")
    args = ap.parse_args(argv)
    cmds = {"pcp": cmd_pcp, "plp": cmd_plp, "rebuild": cmd_rebuild, "fetch": cmd_fetch}
    case_json = cmds[args.cmd](args)
    if case_json is not None:
        print(f"case: {case_json}\nProvided AS IS, see {REPO / 'DISCLAIMER.md'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
