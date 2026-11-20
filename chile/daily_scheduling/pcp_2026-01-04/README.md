# PCP 2026-01-04 — CEN daily unit commitment

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

> These cases try to reproduce the conditions under which PLEXOS is run for
> the CEN daily program.  That configuration (model settings, constraints,
> line ratings and expansions, solver settings, …) is defined by the CEN,
> not by gtopt; the profile, flags and line lifts here only aim to
> replicate it and are not gtopt's recommended defaults.

Mid-summer week; 29 batteries.

| Field | Value |
|---|---|
| Case id | `chile/daily_scheduling/pcp_2026-01-04` |
| Program date | 2026-01-04 (horizon starts 00:00 of this day) |
| Horizon | 132 blocks covering 168 h (PLEXOS ST block layout) |
| Network | 243 buses, 311 lines |
| Units | 1763 generators, 29 batteries, 1026 commitments, 12 reservoirs |
| LP (`--lp-only`) | 1,037,557 rows, 1,302,031 cols, 4,602,228 nnz (gtopt development revision `3b70b4ee9eca`) |
| Method / profile | monolithic MIP, [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json) |
| Source | [`source/DATOS20260104.zip.xz`](source/DATOS20260104.zip.xz) (sha256 `6e1bf9d6f6f63144…`) |
| Converter | `plexos2gtopt` from gtopt; rebuild with gtopt master of November 2026 or later (development revision used: `catalog.json`) |
| Flags | `--no-check --write-out all --plexos-legacy --no-battery-efin-pin --line-losses-mode piecewise --loss-cost-eps 0` |
| Line lifts | `--lifts case`: 39 lines (35 common + 4) |

## Files

- `case/` — gtopt planning JSON, PAMPL user constraints, boundary cuts
  (end-of-horizon water values from the CEN input), solver parameter
  files, conversion provenance.
- `source/` — PLEXOS input `DATOS20260104.zip.xz` as published by the CEN.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/daily_scheduling/pcp_2026-01-04/case
OUT=~/gtopt-cases-out/chile/daily_scheduling/pcp_2026-01-04
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pcp_2026-01-04.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$C" -d . --set solver_options.threads=8
```

To check that your gtopt build reads the case as intended, compare its LP
size with `catalog.json` (`gtopt_check_cases` ships with the gtopt Python
tools):

```bash
gtopt_check_cases --repo "$REPO" --only pcp_2026-01-04    # LP only: rows/cols/nnz
```

- The case JSON goes first and the profile [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json)
  second (its options win).  Monolithic MIP: MIP gap 0.5 %, time limit 7200 s, MIP start.
- `--set input_directory="$C"` makes the case's relative input files
  (PAMPL, CSV, solver parameter files) resolve against the case directory
  while the run happens in the output directory, so solver side files
  (e.g. CPLEX `clone*.log`) never land in the repository.
- Solver: gtopt picks the best available plugin (`--solver highs|cplex|…`
  to choose); `gtopt --solvers` lists them.
- Expected resources: **large** — ~1M-row MIP (unit commitment); plan for a multi-core machine and 5-30 GB RAM (LP build alone ~1.5 GB).

### Rebuild `case/` from `source/`

```bash
tools/get_case.py pcp 2026-01-04
```

`tools/get_case.py` runs the installed `plexos2gtopt` with the flags and
line lifts pinned in `catalog.json`.  It needs the PLEXOS solution bundle
`RES20260104.zip` only for the variable-length block layout; RES is a PLEXOS
result and is not redistributed here: the script downloads it from the CEN
portal (Chilean IP addresses only) into `~/.cache/gtopt-cases/20260104/`, or
pass a local copy with `--res`.  The bundle used for this case has sha256
`10adad89d44f1861…`.

### Line lifts

This case uses `--lifts case`: 39 lines = the 35 `common` lines + 4 for this day
(`DonHumberto033->PPeuco110`, `Jadresic500->Jadresic220`, `NvaPAzucar500->Polpaico500_I`, `Salar110->Salar220`); see
[`line_lifts.json`](../line_lifts.json).  Other choices change the model
(it is then no longer this catalogued case):

```bash
tools/get_case.py pcp 2026-01-04 --lifts common --out ~/gtopt-cases-out/x/case
#   --lifts {case,common,union,none}
```

`plexos2gtopt-line-lifts` (gtopt) ranks the binding lines of a solution to
help choose them (see [the daily-scheduling README](../README.md)).
