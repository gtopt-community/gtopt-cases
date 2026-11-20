#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-gtopt-commercial
# Keep gtopt-cases small and clean.  Run by CI on every push / PR and,
# when enabled (git config core.hooksPath .githooks), before each commit.
#
# Rules:
#   * no tracked file larger than MAX_MB (default 10 MB) -- compress with
#     `xz -6` and/or split the source bundle;
#   * inputs only: no results/, output/, logs/ directories, no *.log,
#     no solver output (*.sol, *.lp dumps) and no Python caches;
#   * no absolute home paths (/home/..., /Users/..., C:\Users\...) in text files;
#   * every source/ file matches its sha256/bytes in catalog.json, and no
#     tracked source/ file is missing from the catalog (NOTICE.md excepted;
#     a catalogued sha256 manifest with a "manifest" directory covers the
#     files it lists; cases with "redistributed": false have no source/);
#   * the whole tracked tree stays under MAX_TREE_MB (default 400 MB).
set -euo pipefail

MAX_MB="${MAX_MB:-10}"
MAX_TREE_MB="${MAX_TREE_MB:-400}"
mode="${1:-tree}"   # tree: all tracked files; staged: files staged for commit

if [[ "$mode" == "staged" ]]; then
  mapfile -d '' files < <(git diff --cached --name-only -z --diff-filter=ACMR)
else
  mapfile -d '' files < <(git ls-files -z)
fi

fail=0
err() { echo "error: $*" >&2; fail=1; }

max_bytes=$((MAX_MB * 1024 * 1024))
for f in "${files[@]}"; do
  [[ -f "$f" ]] || continue
  size=$(stat -c %s -- "$f")
  if (( size > max_bytes )); then
    err "$f is $((size / 1024 / 1024)) MB (> ${MAX_MB} MB); compress (xz -6) or split it"
  fi
  case "$f" in
    */results/*|results/*|*/output/*|output/*|*/logs/*|logs/*|*.log|*.sol|*.sol.gz|*/__pycache__/*|*.pyc|*/.pytest_cache/*)
      err "$f: results, logs and caches are not published (inputs only)" ;;
  esac
done

text_files=()
for f in "${files[@]}"; do
  [[ -f "$f" ]] || continue
  case "$f" in
    *.md|*.json|*.csv|*.txt|*.py|*.sh|*.toml|*.yml|*.yaml|*.prm|*.cfg|*.ini)
      text_files+=("$f") ;;
  esac
done
if (( ${#text_files[@]} )); then
  if hits=$(grep -nIE '(/home/[a-z_][a-z0-9_-]*/|/Users/[A-Za-z]|[A-Z]:\\Users\\)' \
      -- "${text_files[@]}" | grep -v 'check_repo.sh' | head -20) && [[ -n "$hits" ]]; then
    err "absolute home paths found (use paths relative to the case):"
    echo "$hits" >&2
  fi
fi

# source/ integrity: every catalogued file matches its sha256/bytes, and
# every tracked file under a source/ directory is catalogued (NOTICE.md
# excepted).
python3 - <<'PY' || fail=1
import hashlib, json, os, subprocess, sys
cat = json.load(open("catalog.json", encoding="utf-8"))
tracked = set(subprocess.run(["git", "ls-files", "-z"], capture_output=True,
                             text=True, check=True).stdout.split("\0"))
listed, bad = set(), []
for c in cat["cases"]:
    for f in c["source"]["files"]:
        if not c["source"].get("redistributed", True):
            continue  # remote archives, fetched by tools/get_case.py
        p = os.path.normpath(os.path.join(c["path"], f["path"]))
        if p in listed:
            continue
        listed.add(p)
        if p not in tracked or not os.path.isfile(p):
            bad.append(f"{p}: in catalog.json but not tracked")
        elif (os.path.getsize(p) != f["bytes"] or hashlib.sha256(
                open(p, "rb").read()).hexdigest() != f["sha256"]):
            bad.append(f"{p}: sha256/bytes differ from catalog.json")
        elif "manifest" in f:
            # sha256sum-style manifest of the files under f["manifest"]
            # (paths relative to that directory): each is catalogued by it.
            base = os.path.join(c["path"], f["manifest"])
            for line in open(p, encoding="utf-8").read().splitlines():
                digest, _, rel = line.partition("  ")
                q = os.path.normpath(os.path.join(base, rel))
                listed.add(q)
                if q not in tracked or not os.path.isfile(q):
                    bad.append(f"{q}: in {p} but not tracked")
                elif hashlib.sha256(open(q, "rb").read()).hexdigest() != digest:
                    bad.append(f"{q}: sha256 differs from {p}")
bad += [f"{p}: under source/ but not in catalog.json" for p in sorted(tracked - listed)
        if "/source/" in p and os.path.basename(p) != "NOTICE.md"]
for b in bad:
    print(f"error: {b}", file=sys.stderr)
sys.exit(1 if bad else 0)
PY

if [[ "$mode" == "tree" ]]; then
  total=$(git ls-files -z | xargs -0 stat -c %s -- 2>/dev/null | awk '{s+=$1} END {print int(s/1024/1024)}')
  echo "tracked tree: ${total} MB (limit ${MAX_TREE_MB} MB)"
  if (( total > MAX_TREE_MB )); then
    err "tracked tree is ${total} MB (> ${MAX_TREE_MB} MB)"
  fi
fi

exit "$fail"
