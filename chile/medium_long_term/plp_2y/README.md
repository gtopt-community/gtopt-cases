# plp_2y — CEN PLP 2-year case (SDDP)

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
**PLP** (*Programa de Largo Plazo*) input set of 52 stages (February of
year 1 to December of year 3; weekly stages first, then monthly; 10/5
blocks per stage).  It is the reference case for the Laja and Maule
irrigation agreements (`plplajam.dat`, `plpmaulen.dat`).

| Field | Value |
|---|---|
| Case id | `chile/medium_long_term/plp_2y` |
| Horizon | 52 stages = 52 SDDP phases, 270 blocks, 25,248 h |
| Hydrologies | 4 equiprobable scenarios: 2, 17, 52, 67 (of 68 in `plpaflce.dat`; PLP simulates 51–68) |
| Apertures | 20 (every PLP aperture, `-a all`) |
| Network | 245 buses, 343 lines |
| Units | 1892 generators, 112 batteries, 10 reservoirs, 176 turbines, 4 flow rights |
| LP (`--lp-only`) | 4,279,344 rows, 3,237,404 cols, 11,166,608 nnz over 208 (scene, phase) LPs (gtopt `75d9cec1c`) |
| Method / profile | sddp, no profile (method and SDDP options are in the case JSON) |
| Future cost | `system.future_cost_array`: `boundary_cuts.csv` (1007 PLP cuts), `mode: phi_expectation` |
| Converter | `plp2gtopt` from gtopt `75d9cec1c` (converter last changed in `801bf32b3`) |

## Files

- `source/` — the PLP input files as used by the CEN (`plp*.dat`,
  `indhor.csv`, `centipo.csv`; xz-compressed, `plp2gtopt` reads them
  directly) and `run_plp_cen65_*.sh`, the environment flags of the PLP
  run.  Formerly `support/plp/2_years` in the gtopt repository.
- `case/` — `gtopt_case_2y.json`, per-class Parquet inputs, `apertures/`,
  `boundary_cuts.csv`, `solvers/` (parameter files, comments removed) and
  `plp2gtopt_state.json` (exact converter invocation and options).

## How to run

Results are never written into this repository: run from an output
directory outside it.

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/medium_long_term/plp_2y/case
OUT=~/gtopt-cases-out/chile/medium_long_term/plp_2y
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/gtopt_case_2y.json" --set input_directory="$C" -d .
```

- `--set input_directory="$C"` resolves the Parquet/CSV inputs against
  `case/` while the run happens in the output directory.
- The case ships with `sddp_options.max_iterations = 20`; override with
  `--set sddp_options.max_iterations=N`, and use fewer apertures for a
  quick run with `--set sddp_options.num_apertures=K`.
- Solver: gtopt picks the best available plugin (`--solver highs|…`).
- Expected resources: **large** — SDDP over 208 phase LPs; plan for 8+
  cores and 16+ GB RAM.
- Check that your gtopt reads the case as intended (LP size vs
  `catalog.json`): `gtopt_check_cases --repo "$REPO" --only plp_2y`.

## Regenerating `case/` from `source/`

`case/` was produced from this folder (`plp_2y/`) with

```bash
plp2gtopt -i source -o case -f case/gtopt_case_2y.json -n gtopt_case_2y \
    -y 2,17,52,67 -a all --method sddp
```

(also `plp2gtopt --from-state case/plp2gtopt_state.json`; the snapshot
stores `source`/`case` relative to `plp_2y/`), keeping the planning JSON,
data directories, `boundary_cuts.csv` and `solvers/` (comments removed),
without the converter's `README.md` and `logs/`.  `tools/get_case.py`
does exactly that from the catalogued flags:

```bash
tools/get_case.py rebuild plp_2y --out <dir outside the repo>
```

reproduces `case/` byte for byte (except `plp2gtopt_state.json`) with
the gtopt revision above.

| Flag | Meaning |
|---|---|
| `-n gtopt_case_2y` | System name (also the default JSON stem when `-f` is omitted). |
| `-y 2,17,52,67` | `--hydrologies`: 4 scenarios, probability 0.25 each. |
| `-a all` | `--num-apertures`: keep every SDDP aperture. |
| `--method sddp` | One scene per scenario, one phase per stage. |

All other options are plp2gtopt defaults.  The PLP boundary cuts
(`plpplem1/2.dat`) go to `boundary_cuts.csv`, referenced from
`system.future_cost_array` by a path relative to `case/`.

### Selecting hydrologies

`-y` / `--hydrologies` takes 1-based `plpaflce.dat` column indices: a
single index (`-y 17`), a comma list (`-y 2,17,52,67`), a range
(`-y 1-16`) or a mix (`-y 1-4,51,60-68`).  `-y all` (the default) keeps
the PLP simulated set (`plpidsim.dat`: 51–68) and `--first-scenario` its
first member.  A hydrology outside the simulated set (e.g. 2 or 17)
advances one historical year at each January exactly like the simulated
ones (wrapping 68 → 1).  By total inflow over the horizon, 67 is the
driest of the 68, 52 and 17 lie somewhat below the median and 2 is
wetter than most.

### Variants

Former variants of this case differ only in hydrologies, stages and
method.  From `plp_2y/`, writing to a directory `<out>` outside the
repository (its basename is the default case stem):

| Variant | Command |
|---|---|
| This case: 4 hydrologies, full horizon, SDDP | `plp2gtopt -i source -o <out> -y 2,17,52,67 -a all --method sddp` |
| First scenario only (former `gtopt_case_2y_fs`), SDDP | `plp2gtopt -i source -o <out> --first-scenario --method sddp` |
| Single hydrology (former `gtopt_case_2y_17`), SDDP | `plp2gtopt -i source -o <out> -y 17 --method sddp` |
| 6 stages, monolithic (former `gtopt_case_2y_6s`) | `plp2gtopt -i source -o <out> -s 6 -y 2,17,52,67 --method monolithic` |
| 6 stages, first scenario, SDDP | `plp2gtopt -i source -o <out> -s 6 --first-scenario --method sddp` |
| Two simulated hydrologies (former `gtopt_case_2y`) | `plp2gtopt -i source -o <out> -y 51,52 -a all --method sddp` |
| Every simulated hydrology (18 scenarios) | `plp2gtopt -i source -o <out>` (`-y all`, `--method sddp`) |
| Whole inflow record (68 scenarios) | `plp2gtopt -i source -o <out> -y 1-68 --method sddp` |

`-s` / `--last-stage` is a **stage count** (default all 52), not a
scenario count; `--method monolithic` puts every scenario and stage in
one LP; `plp2gtopt --help` lists every flag.
