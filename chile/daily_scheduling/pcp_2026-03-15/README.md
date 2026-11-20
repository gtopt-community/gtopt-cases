# PCP 2026-03-15 — CEN daily unit commitment

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../../DISCLAIMER.md).

> These cases try to reproduce the conditions under which PLEXOS is run for
> the CEN daily program.  That configuration (model settings, constraints,
> line ratings and expansions, solver settings, …) is defined by the CEN,
> not by gtopt; the profile, flags and line lifts here only aim to
> replicate it and are not gtopt's recommended defaults.

Autumn transition; extra lifts on the central 220 kV corridor (Los Vilos–Nogales, Quillota–Mauro).

| Field | Value |
|---|---|
| Case id | `chile/daily_scheduling/pcp_2026-03-15` |
| Program date | 2026-03-15 (horizon starts 00:00 of this day) |
| Horizon | 132 blocks covering 168 h (PLEXOS ST block layout) |
| Network | 246 buses, 315 lines |
| Units | 1768 generators, 33 batteries, 1066 commitments, 12 reservoirs |
| LP (`--lp-only`) | 1,066,186 rows, 1,303,587 cols, 4,687,564 nnz (gtopt 3b70b4ee9eca) |
| Method / profile | monolithic MIP, [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json) |
| Source | [`source/DATOS20260315.zip.xz`](source/DATOS20260315.zip.xz) (sha256 `c2050ffb4cf2e8e0…`) |
| Converter | `plexos2gtopt` from gtopt `d92e4cf14` (converter last changed in `53079a43f`) |
| Flags | `--no-check --write-out all --plexos-legacy --no-battery-efin-pin --line-losses-mode piecewise --loss-cost-eps 0` |
| Line lifts | `--lifts case`: 42 lines (35 common + 7) |

## Files

- `case/` — gtopt planning JSON, PAMPL user constraints, boundary cuts
  (end-of-horizon water values from the CEN input), solver parameter
  files, conversion provenance.
- `source/` — PLEXOS input `DATOS20260315.zip.xz` as published by the CEN.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/daily_scheduling/pcp_2026-03-15/case
OUT=~/gtopt-cases-out/chile/daily_scheduling/pcp_2026-03-15
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pcp_2026-03-15.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$C" -d . --set solver_options.threads=8
```

To check that your gtopt build reads the case as intended, compare its LP
size with `catalog.json` (`gtopt_check_cases` ships with the gtopt Python
tools):

```bash
gtopt_check_cases --repo "$REPO" --only pcp_2026-03-15    # LP only: rows/cols/nnz
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
tools/get_case.py pcp 2026-03-15
```

`tools/get_case.py` runs the installed `plexos2gtopt` with the flags and
line lifts pinned in `catalog.json`.  It needs the PLEXOS solution bundle
`RES20260315.zip` only for the variable-length block layout; RES is a PLEXOS
result and is not redistributed here: the script downloads it from the CEN
portal (Chilean IP addresses only) into `~/.cache/gtopt-cases/20260315/`, or
pass a local copy with `--res`.  The bundle used for this case has sha256
`a2b70a6e873aad3d…`.

### Line lifts

This case uses `--lifts case`: 42 lines = the 35 `common` lines + 7 for this day
(`Jadresic500->Jadresic220`, `LVilos220->Nogales220`, `LosChangos500->Kimal500_II`, `NvaPAzucar500->Polpaico500_I`, `NvaPAzucar500->Polpaico500_II`, `Quillota220->Mauro220`, `Salar110->Salar220`); see
[`line_lifts.json`](../line_lifts.json).  Other choices change the model
(it is then no longer this catalogued case):

```bash
tools/get_case.py pcp 2026-03-15 --lifts common --out ~/gtopt-cases-out/x/case
#   --lifts {case,common,union,none}
```

`plexos2gtopt-line-lifts` (gtopt) ranks the binding lines of a solution to
help choose them (see [the daily-scheduling README](../README.md)).
