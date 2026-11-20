# plp_5y — CEN PLP 5-year case (SDDP)

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../../DISCLAIMER.md).

Hydrothermal case of the Chilean SEN built with `plp2gtopt` from a CEN
**PLP** (*Programa de Largo Plazo*) input set of 72 stages (July of
year 1 to December of year 5; weekly stages first, then monthly; 10/5/3
blocks per stage).  Mid-horizon companion of [plp_2y](../plp_2y).

| Field | Value |
|---|---|
| Case id | `chile/medium_long_term/plp_5y` |
| Horizon | 72 stages = 72 SDDP phases, 234 blocks, 39,432 h (~4.5 years) |
| Hydrologies | 4 equiprobable scenarios: 16, 17, 19, 48 (of 65 in `plpaflce.dat`; PLP simulates 36–65) |
| Apertures | 34 (every PLP aperture, `-a all`) |
| Network | 241 buses, 345 lines |
| Units | 1880 generators, 68 batteries, 10 reservoirs, 177 turbines, 4 flow rights |
| LP (`--lp-only`) | 3,593,820 rows, 2,781,076 cols, 9,513,040 nnz over 288 (scene, phase) LPs (gtopt development revision `75d9cec1c`) |
| Method / profile | sddp, no profile (method and SDDP options are in the case JSON) |
| Future cost | `system.future_cost_array`: `boundary_cuts.csv` (1665 PLP cuts), `mode: phi_expectation` |
| Converter | `plp2gtopt` from gtopt; rebuild with gtopt master of November 2026 or later (development revision used: `catalog.json`) |

## Files

- `source/` — the PLP input files as used by the CEN (`plp*.dat`,
  `indhor.csv`; xz-compressed, `plp2gtopt` reads them directly).
- `case/` — `gtopt_case_5y.json`, per-class Parquet inputs, `apertures/`,
  `boundary_cuts.csv`, `solvers/` (parameter files, comments removed) and
  `plp2gtopt_state.json` (exact converter invocation and options).

## How to run

Results are never written into this repository: run from an output
directory outside it.

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/medium_long_term/plp_5y/case
OUT=~/gtopt-cases-out/chile/medium_long_term/plp_5y
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/gtopt_case_5y.json" --set input_directory="$C" -d .
```

- `--set input_directory="$C"` resolves the Parquet/CSV inputs against
  `case/` while the run happens in the output directory.
- The case ships with `sddp_options.max_iterations = 20`; a quick
  feasibility check is `--set sddp_options.max_iterations=1 --set
  sddp_options.num_apertures=3`.
- Solver: gtopt picks the best available plugin (`--solver highs|…`).
- Expected resources: **large** — SDDP over 288 phase LPs; plan for 8+
  cores and 16+ GB RAM.
- Check that your gtopt reads the case as intended (LP size vs
  `catalog.json`): `gtopt_check_cases --repo "$REPO" --only plp_5y`.

## Regenerating `case/` from `source/`

`case/` was produced from this folder (`plp_5y/`) with

```bash
plp2gtopt -i source -o case -f case/gtopt_case_5y.json -n gtopt_case_5y \
    -y 16,17,19,48 -a all --method sddp
```

(also `plp2gtopt --from-state case/plp2gtopt_state.json`; the snapshot
stores `source`/`case` relative to `plp_5y/`), keeping the planning JSON,
data directories, `boundary_cuts.csv` and `solvers/` (comments removed),
without the converter's `README.md` and `logs/`.  `tools/get_case.py`
does exactly that from the catalogued flags:

```bash
tools/get_case.py rebuild plp_5y --out <dir outside the repo>
```

reproduces `case/` byte for byte (except `plp2gtopt_state.json`) with
the gtopt revision above.

| Flag | Meaning |
|---|---|
| `-n gtopt_case_5y` | System name (also the default JSON stem when `-f` is omitted). |
| `-y 16,17,19,48` | `--hydrologies`: 4 scenarios, probability 0.25 each. |
| `-a all` | `--num-apertures`: keep every SDDP aperture. |
| `--method sddp` | One scene per scenario, one phase per stage. |

All other options are plp2gtopt defaults.  The PLP boundary cuts
(`plpplem1/2.dat`) go to `boundary_cuts.csv`, referenced from
`system.future_cost_array` by a path relative to `case/`.

### Selecting hydrologies

`-y` / `--hydrologies` takes 1-based `plpaflce.dat` column indices (65
hydrologies, 1–65): a single index, a comma list, a range or a mix
(`-y 1-4,40,60-65`).  `-y all` (the default) keeps the PLP simulated set
(`plpidsim.dat`: 36–65) and `--first-scenario` its first member.  A
hydrology outside the simulated set advances one historical year at each
January exactly like the simulated ones.

The four hydrologies of this case span the record: ranked by total
inflow over the horizon, 48 is near the 10th percentile, 17 near the
35th, 16 near the 65th and 19 near the 90th.

### Variants

From `plp_5y/`, writing to a directory `<out>` outside the repository
(its basename is the default case stem):

| Variant | Command |
|---|---|
| This case: 4 hydrologies, full horizon, SDDP | `plp2gtopt -i source -o <out> -y 16,17,19,48 -a all --method sddp` |
| First scenario only, SDDP | `plp2gtopt -i source -o <out> --first-scenario --method sddp` |
| First year only (about 1 year of stages), SDDP | `plp2gtopt -i source -o <out> -t 1y -y 16,17,19,48 --method sddp` |
| Every simulated hydrology (30 scenarios) | `plp2gtopt -i source -o <out>` (`-y all`, `--method sddp`) |
| Whole inflow record (65 scenarios) | `plp2gtopt -i source -o <out> -y 1-65 --method sddp` |
| Monolithic, 6 stages | `plp2gtopt -i source -o <out> -s 6 -y 16,17,19,48 --method monolithic` |

`-s` / `--last-stage` is a **stage count** (default all 72) and `-t` an
accumulated time (`1y`, `6m`, hours); `plp2gtopt --help` lists every flag.
