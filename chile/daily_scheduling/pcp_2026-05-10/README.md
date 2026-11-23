# PCP 2026-05-10 — CEN daily unit commitment (source only)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

> [!IMPORTANT]
> **Source only: no gtopt case is built yet.**  This folder keeps the
> PLEXOS input bundle as published by the CEN; `tools/get_case.py fetch
> pcp_2026-05-10` builds the case on your machine.  No gtopt case has been
> built or checked for this day by the gtopt authors.

> These cases try to reproduce the conditions under which PLEXOS is run for
> the CEN daily program.  That configuration (model settings, constraints,
> line ratings and expansions, solver settings, …) is defined by the CEN,
> not by gtopt; the profile, flags and line lifts here only aim to
> replicate it and are not gtopt's recommended defaults.

Kept as a test day for the comparison of line-loss models (PLEXOS and
gtopt) on the CEN daily programme.

| Field | Value |
|---|---|
| Case id | `chile/daily_scheduling/pcp_2026-05-10` |
| Program date | 2026-05-10 (horizon starts 00:00 of this day) |
| Purpose | loss-model comparison |
| Source | [`source/DATOS20260510.zip.xz`](source/DATOS20260510.zip.xz) (sha256 `24b828157bf75ff0…`) |
| Origin | CEN PCP portal, `PLEXOS20260510.zip` (<https://programa.coordinador.cl/operacion/pcp/bases-modelo>) |
| PLEXOS version | 10.000 (database `DBSEN_PRGDIARIO.xml`) |
| Converter | `plexos2gtopt` from gtopt master of November 2026 or later (`--source-version 10.000`) |
| Flags | `--no-check --write-out all --plexos-legacy --no-battery-efin-pin --line-losses-mode piecewise --loss-cost-eps 0 --source-version 10.000` |
| Line lifts | `--lifts common`: the 35 `common` lines of [`line_lifts.json`](../line_lifts.json) (no per-case list for this day) |
| Method / profile | monolithic MIP, [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json) |

## Files

- `source/` — PLEXOS input `DATOS20260510.zip.xz` as published by the CEN
  (inner zip of `PLEXOS20260510.zip`, recompressed with `xz -6`).

## Get and convert

With the gtopt Python tools of gtopt master of November 2026 or later
installed (`pip install -e <gtopt>/scripts`):

```bash
tools/get_case.py fetch pcp_2026-05-10      # same as: tools/get_case.py pcp 2026-05-10
```

This checks `source/DATOS20260510.zip.xz` against its sha256 in
[`catalog.json`](../../../catalog.json), downloads the PLEXOS solution
bundle `RES20260510.zip` (a result, needed only for the variable-length
block layout; not redistributed here) from the CEN portal into
`$GTOPT_CASES_CACHE/20260510/` (default `~/.cache/gtopt-cases`, outside
the repository), runs `plexos2gtopt` with the flags and line lifts in
`catalog.json`, writes `case/pcp_2026-05-10.json` (git-ignored) and prints
the gtopt command to run it. **The portal only serves Chilean IP
addresses**: from abroad, pass a local copy of the solution bundle with
`--res`. Use `--out DIR` to write the case elsewhere.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/daily_scheduling/pcp_2026-05-10/case
OUT=~/gtopt-cases-out/chile/daily_scheduling/pcp_2026-05-10
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pcp_2026-05-10.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$C" -d . --set solver_options.threads=8
```

- The case JSON goes first and the profile
  [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json)
  second (its options win).  Monolithic MIP: MIP gap 0.5 %, time limit
  7200 s, MIP start.
- `--set input_directory="$C"` makes the case's relative input files
  resolve against the case directory while the run happens in the output
  directory, so nothing lands in the repository.
- Expected resources: not measured for this day (no case is catalogued);
  the catalogued PCP cases are 0.8–1.3 M-row MIPs that need a multi-core
  machine and 5–30 GB of RAM.
