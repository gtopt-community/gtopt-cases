# ncp_pdd_2026-06-22 — Guatemala (daily scheduling)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

| Field | Value |
|---|---|
| Case id | `guatemala/daily_scheduling/ncp_pdd_2026-06-22` |
| Horizon | 168 blocks covering 168 h, 1 stage, 1 scenario |
| Network | 830 buses, 955 lines |
| Units | 229 generators, 0 batteries |
| LP (`--lp-only`) | 192,056 rows, 302,762 cols, 605,654 nnz (gtopt development revision `18548ca102a8`, local build) |
| Method / profile | monolithic, no profile (self-contained JSON) |
| Source | `source/PRECIOSMEX.csv.xz`, `source/RESTMEX.csv.xz`, `source/Volt.dat.xz`, `source/ccombuGU.dat.xz`, `source/cgndgu.dat.xz`, `source/chidroGU.dat.xz`, `source/commith.dat.xz`, `source/cpdexbus.dat.xz`, `source/cpgndgu.dat.xz`, `source/cprmxhgu_u.dat.xz`, `source/cprmxtgu_u.dat.xz`, `source/ctermigu.dat.xz`, `source/dbus.dat.xz`, `source/dcirc.dat.xz`, `source/gndsitegu.dat.xz`, `source/inflow.csv.xz`, `source/sddp.dat.xz`, `source/sistem.dat.xz`, `source/volfincp.csv.xz`, `source/watervcp.csv.xz` |
| Origin | AMM PSR NCP daily program PDD_22JUN2026_V5.29.b.rar (not redistributed) |
| Converter | `sddp2gtopt` from gtopt commit `5a4fd2ef8` (no-offer import rule, not yet on public master); rebuild with a gtopt that includes it |
| Flags | none |

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/guatemala/daily_scheduling/ncp_pdd_2026-06-22/case
OUT=~/gtopt-cases-out/guatemala/daily_scheduling/ncp_pdd_2026-06-22
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/ncp_pdd_22jun.json" \
    --set input_directory="$C" -d .
```

To check that your gtopt build reads the case as intended, compare its LP
size with `catalog.json` (`gtopt_check_cases` ships with the gtopt Python
tools):

```bash
gtopt_check_cases --repo "$REPO" --only ncp_pdd_2026-06-22    # LP only: rows/cols/nnz
```

- Self-contained case: no profile; all options are in the case JSON.
- `--set input_directory="$C"` makes the case's relative input files
  (PAMPL, CSV, solver parameter files) resolve against the case directory
  while the run happens in the output directory, so solver side files
  (e.g. CPLEX `clone*.log`) never land in the repository.
- Solver: gtopt picks the best available plugin (`--solver highs|cplex|…`
  to choose); `gtopt --solvers` lists them.
- Expected resources: **medium** — ~0.2M-row LP/MIP; a few GB RAM.
- Tested with a gtopt build that includes FutureCost (`system.future_cost_array`); older builds do not read this case.

### Regenerate `case/` from `source/`

The case JSON was produced with `sddp2gtopt` from gtopt commit
`5a4fd2ef8`.  To regenerate it with the installed converter and the flags
pinned in `catalog.json`:

```bash
tools/get_case.py rebuild ncp_pdd_2026-06-22 --out <dir>
```

The converters have evolved since this case was produced, so a rebuild may
differ from the committed case; check it with `gtopt_check_cases`.

## Notes

- Self-contained case (no application profile); run as is.
- Daily PSR NCP model (PDD 22-Jun-2026) over a 168-hour horizon, single stage, 1 block per hour.
- Terminal water value: system.future_cost_array 'fcf' -> case/boundary_cuts.csv (watervcp single-cut proxy).
  `case/boundary_cuts_gtopt_fcf.csv` holds gtopt's own FCF from the
  two-run pipeline: a 12-week deterministic SDDP built from this case
  (one weekly block per stage), whose converged phase-1 cut prices the
  reservoirs at the end of week 1.  It is an A/B alternative, not used by
  default: point `future_cost_array[0].cuts_file` at it in a copy of the
  case JSON.  Its cut carries the 11-week cost-to-go, so the objective is
  not comparable with the default run; compare the dispatch instead.
- Economics: thermal merit costs, water values, inflow-limited run-of-river.
- Imports: an interconnection import is available only in the hours
  where it has an offer.  `PRECIOSMEX.csv` prices the imports hour by
  hour on 21–22 Jun and is zero for every unit on 23–27 Jun; a blank or
  zero price means no offer, so the import is closed (capacity 0) in that
  hour.  `MEX-I` is zero in every hour and is left out; the AMM lists it
  as unavailable since November 2020, but the bundle has no outage record
  of its own, so the general rule is what removes it.  `EDC-I` keeps its
  fixed `RESTMEX.csv` schedule (120 MW, 22 Jun only).  No aggregate
  import limit is added, because the source sets none; the modelled
  border network (the two LBR 400/230 kV transformers, 2 x 225 MW, on
  the Mexico side) still limits the imports.  `sddp2gtopt --import-limit`
  remains available as an opt-in cap.
