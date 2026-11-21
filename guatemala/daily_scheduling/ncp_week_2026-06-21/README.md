# ncp_week_2026-06-21 — Guatemala (daily scheduling)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

| Field | Value |
|---|---|
| Case id | `guatemala/daily_scheduling/ncp_week_2026-06-21` |
| Horizon | 168 blocks covering 168 h, 1 stage, 1 scenario |
| Network | 830 buses, 955 lines |
| Units | 203 generators, 0 batteries |
| LP (`--lp-only`) | 192,024 rows, 281,898 cols, 585,262 nnz (gtopt development revision `18548ca102a8`, local build) |
| Method / profile | monolithic, no profile (self-contained JSON) |
| Source | `source/Volt.dat.xz`, `source/ccombuGU.dat.xz`, `source/chidroGU.dat.xz`, `source/cpdexbus.dat.xz`, `source/ctermigu.dat.xz`, `source/dbus.dat.xz`, `source/dcirc.dat.xz`, `source/sddp.dat.xz`, `source/sistem.dat.xz` |
| Origin | AMM weekly NCP model '26 - Semana del 21 al 27 de junio de 2026 NCP.5.29.b.rar' (not redistributed) |
| Converter | `sddp2gtopt` from gtopt commit `5a4fd2ef8` (no-offer import rule) or later |
| Flags | none |

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/guatemala/daily_scheduling/ncp_week_2026-06-21/case
OUT=~/gtopt-cases-out/guatemala/daily_scheduling/ncp_week_2026-06-21
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/sddp_ncp_week.json" \
    --set input_directory="$C" -d .
```

To check that your gtopt build reads the case as intended, compare its LP
size with `catalog.json` (`gtopt_check_cases` ships with the gtopt Python
tools):

```bash
gtopt_check_cases --repo "$REPO" --only ncp_week_2026-06-21    # LP only: rows/cols/nnz
```

- Self-contained case: no profile; all options are in the case JSON.
- `--set input_directory="$C"` makes the case's relative input files
  (PAMPL, CSV, solver parameter files) resolve against the case directory
  while the run happens in the output directory, so solver side files
  (e.g. CPLEX `clone*.log`) never land in the repository.
- Solver: gtopt picks the best available plugin (`--solver highs|cplex|…`
  to choose); `gtopt --solvers` lists them.
- Expected resources: **medium** — ~0.2M-row LP/MIP; a few GB RAM.
- Tested with a gtopt build that includes FutureCost (`system.future_cost_array`).

### Regenerate `case/` from `source/`

The case JSON was produced with `sddp2gtopt` from gtopt commit
`5a4fd2ef8`.  To regenerate it with the installed converter and the flags
pinned in `catalog.json`:

```bash
tools/get_case.py rebuild ncp_week_2026-06-21 --out <dir>
```

A rebuild with a later converter may differ from the committed case;
check it with `gtopt_check_cases`.

## Notes

- Self-contained case (no application profile); run as is.
- Weekly NCP dispatch 21-27 Jun 2026 (short-term weekly program), 168 hourly blocks, single stage; kept under daily_scheduling (dispatch with hourly resolution).
- No water-value file shipped: thermal merit costs only.
- Imports: the bundle has no `PRECIOSMEX.csv`, so the fuel table
  (`ccombuGU.dat`) prices the imports.  An import unit whose fuel costs $0
  (`MEX-I`, `IMP-01`) has no offer and is left out: 16 units, `MEX-I`,
  `MEX-I2` to `MEX-I11`, `MEX-I15`, `IMP-01`, `ESA-IMP`, `HON-IMP` and
  `IMP-OPO`.  `EDC-I` (38.89 $/MWh, 120 MW) and `ESA-I`, `HON-I`,
  `MEX-01` (fuel `INTER-SAL`, 1000 $/MWh) stay available.  No aggregate
  import limit is added (`sddp2gtopt --import-limit` is opt-in).
