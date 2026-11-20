# Chile — daily scheduling (CEN PCP, PLEXOS → gtopt)

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../DISCLAIMER.md).

> **These cases replicate the CEN's PLEXOS setup, not gtopt defaults.**
> The 14 PCP cases try to reproduce the conditions under which PLEXOS is run
> for the CEN daily program.  That configuration (model settings,
> constraints, line ratings and expansions, solver settings, …) is defined
> by the CEN (Coordinador Eléctrico Nacional), not by the gtopt project.
> The profile, converter flags and line lifts used here only aim to
> replicate it; they are not gtopt's recommended defaults for daily
> scheduling.

Each case is one day of the CEN *Programa de Coordinación de Predespacho*
(PCP): a security-constrained unit commitment of the whole SEN over a
6–7 day horizon (the first day is the program; the rest is look-ahead),
with DC power flow (Kirchhoff), piecewise line losses, reserves, hydro
cascades with end-of-horizon water values (boundary cuts), batteries and the
CEN's user constraints.  gtopt solves it as one monolithic MIP.

| Case | Buses | Generators | Blocks (horizon) | Lifted lines | LP rows | LP cols | LP nnz |
|---|---:|---:|---:|---:|---:|---:|---:|
| [pcp_2025-10-05](pcp_2025-10-05) | 237 | 1739 | 168 (168 h) | 37 | 1,288,403 | 1,636,065 | 5,750,362 |
| [pcp_2025-10-19](pcp_2025-10-19) | 239 | 1747 | 107 (144 h) | 39 | 820,905 | 1,035,513 | 3,623,480 |
| [pcp_2025-11-09](pcp_2025-11-09) | 239 | 1751 | 118 (144 h) | 40 | 910,149 | 1,140,367 | 3,989,755 |
| [pcp_2025-11-23](pcp_2025-11-23) | 241 | 1753 | 132 (168 h) | 41 | 1,015,462 | 1,277,429 | 4,487,081 |
| [pcp_2025-12-07](pcp_2025-12-07) | 241 | 1753 | 132 (168 h) | 43 | 1,031,274 | 1,280,963 | 4,554,741 |
| [pcp_2025-12-21](pcp_2025-12-21) | 241 | 1753 | 132 (168 h) | 41 | 1,043,802 | 1,294,927 | 4,636,298 |
| [pcp_2026-01-04](pcp_2026-01-04) | 243 | 1763 | 132 (168 h) | 39 | 1,037,557 | 1,302,031 | 4,602,228 |
| [pcp_2026-01-18](pcp_2026-01-18) | 243 | 1765 | 132 (168 h) | 37 | 1,041,981 | 1,304,470 | 4,634,096 |
| [pcp_2026-02-15](pcp_2026-02-15) | 246 | 1769 | 132 (168 h) | 41 | 1,036,862 | 1,290,589 | 4,553,540 |
| [pcp_2026-03-15](pcp_2026-03-15) | 246 | 1768 | 132 (168 h) | 42 | 1,066,186 | 1,303,587 | 4,687,564 |
| [pcp_2026-04-07](pcp_2026-04-07) | 247 | 1772 | 111 (168 h) | 42 | 889,504 | 1,099,603 | 3,880,447 |
| [pcp_2026-04-12](pcp_2026-04-12) | 247 | 1773 | 110 (168 h) | 38 | 906,263 | 1,109,851 | 3,986,400 |
| [pcp_2026-04-22](pcp_2026-04-22) | 247 | 1776 | 111 (168 h) | 37 | 918,500 | 1,125,802 | 4,087,208 |
| [pcp_2026-05-17](pcp_2026-05-17) | 251 | 1790 | 110 (168 h) | 37 | 915,043 | 1,136,220 | 4,057,816 |

## Canonical build ("cen-trad0" + per-case lifts)

```
plexos2gtopt -i <bundle dir with DATOS (+ RES)> -o <out> \
  --no-check --write-out all --plexos-legacy --no-battery-efin-pin \
  --line-losses-mode piecewise --loss-cost-eps 0 \
  --lift-line-caps <per-case list from line_lifts.json>
```

- `--plexos-legacy --no-battery-efin-pin` ("cen" flavor): stay as close as
  possible to what PLEXOS/CEN solves, without gtopt's physical corrections.
- `--line-losses-mode piecewise --loss-cost-eps 0` ("trad0"): traditional
  piecewise losses with no loss cost, like PLEXOS.
- Block layout: plexos2gtopt reads the variable-length PLEXOS block layout
  from the solution bundle `RES<date>.zip`, so rebuilding a case needs it.
  RES is a PLEXOS result: it is not redistributed here;
  `tools/get_case.py pcp <date>` downloads it from the CEN portal into
  `~/.cache/gtopt-cases/` (or pass a local copy with `--res`).
- The converter needs its data files (cogeneration list, emission factors,
  the list of CEN user constraints that are hard): install the gtopt Python
  tools in editable mode from a checkout (`pip install -e <gtopt>/scripts`)
  or from a gtopt revision whose wheel ships them; without them the
  converter builds a different model.
- Shared solve options live in
  [`profiles/daily_scheduling.json`](../../profiles/daily_scheduling.json):
  monolithic, MIP gap 0.5 %, time limit 7200 s, MIP start, zstd output.
  Each case keeps only what distinguishes it (VoLL-based
  `demand_fail_cost`, reserve shortage cost, loss mode, solver parameter
  file, boundary cuts).  LP equilibration is left at the gtopt default.
- Exact flags, converter revision and file hashes per case:
  [`catalog.json`](../../catalog.json).

### Documented variant (not built): `tsf1`

`--line-losses-mode tangent_signed_flow --loss-cost-eps 1.0` (the current
plexos2gtopt default loss model).  It removes most phantom losses under
negative prices but departs from the PLEXOS loss model; build it with
`plexos2gtopt` directly (or `tools/get_case.py` after editing the flags in
`catalog.json`).

## Line lifts (lines expanded from outside the model)

PLEXOS dispatches some lines above their stated rating: their capacity is
expanded outside the model (operational limits the CEN manages separately).
With the rating as a hard cap, gtopt would be over-constrained.
`plexos2gtopt --lift-line-caps <names>` turns those caps into soft bands
(`--auto-lift-lines [THR]` detects candidates with a DC OPF).

[`line_lifts.json`](line_lifts.json) holds the lists used here, captured
from the PLEXOS solutions:

- `common` — 35 lines over-rated on every one of the 14 days (equal to the
  plexos2gtopt default `--lift-line-caps`);
- `union` — 54 lines over-rated on at least one day;
- `per_case` — the list for each day (37–43 lines: common + extras).

**Recommendation.** Because some lines are expanded from outside the model,
analyse the output and choose which lines to lift
(`plexos2gtopt-line-lifts <case.json> <gtopt output> --lifted
line_lifts.json --lifted-key common --suggest`, from gtopt, ranks binding
lines by their dual), and/or start from the lists used for the 14 cases.
`tools/get_case.py pcp <date> --lifts {case,common,union,none}` uses `case`
for the 14 catalogued days and `common` otherwise; `plexos2gtopt
--auto-lift-lines` detects candidates before solving.

## How to run

Every case README has the exact commands.  In short (results always go
outside the repository):

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)
D=chile/daily_scheduling/pcp_2025-10-19          # any of the 14 cases
OUT=~/gtopt-cases-out/$D
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/$D/case/pcp_2025-10-19.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$REPO/$D/case" -d . --set solver_options.threads=8
```

`gtopt_check_cases --repo "$REPO" --only pcp_2025-10-19` (from the gtopt
Python tools) only builds the LP and compares its rows/cols/nnz with
`catalog.json`, which is the quick way to confirm that your gtopt build
reads the case as intended.

Expected resources: each case is a monolithic MIP of 0.8–1.3 M rows;
plan for a multi-core machine and 5–30 GB of RAM (the LP build alone
needs about 1.5 GB).  The profile caps the solve with
`time_limit` 7200 s and a 0.5 % MIP gap.

## New days

```bash
tools/get_case.py pcp 2026-06-03
```

The inputs land in `chile/daily_scheduling/pcp_<date>/{source,case}/`; the
PLEXOS solution bundle stays in `~/.cache/gtopt-cases/<YYYYMMDD>/`, outside
the repository.  Then run the case as above (results outside the
repository) and, to review the line lifts, `plexos2gtopt-line-lifts` on its
output.  `cen2gtopt-pcp-solution summary --res <RES bundle> --output <dir>`
(gtopt) summarises the PLEXOS solution for your own comparisons.

Files already present (`source/DATOS<date>.zip.xz`, the cached RES) are
not downloaded again.  The CEN bucket only serves Chilean IP addresses.
