# plp_23y — CEN PLP long-term input (23 years), 1-year SDDP case

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../../DISCLAIMER.md).

Long-term **PLP** (*Programa de Largo Plazo*) input set of the CEN:
**276 monthly stages** (year 1 month 1 to year 23 month 12, 10 blocks per
stage), **28 hydrologies**, 339 buses, irrigation agreements and
reservoir seepage (`plpfilemb.dat`: ELTORO, CIPRESES, COLBUN).  The
committed case, `cen_long_term_1y`, is its **first year**; the full
23-year horizon is a [variant](#variants).

| Field | Value |
|---|---|
| Case id | `chile/medium_long_term/plp_23y` |
| Horizon | 12 monthly stages = 12 SDDP phases, 120 blocks, 8,784 h |
| Hydrologies | 1 scenario: hydrology 1 (of 28); no apertures (`-a 0`) |
| Network | 339 buses, 449 lines |
| Units | 1628 generators, 10 reservoirs, 156 turbines, 3 flow rights |
| LP (`--lp-only`) | 673,493 rows, 472,250 cols, 1,693,693 nnz over 12 phase LPs (gtopt `75d9cec1c`) |
| Method / profile | sddp, no profile (method and SDDP options are in the case JSON; `sddp_options.max_iterations = 3`) |
| Future cost | `system.future_cost_array`: `boundary_cuts.csv` (810 PLP cuts), `mode: phi_expectation` |
| Converter | `plp2gtopt` from gtopt `75d9cec1c` (converter last changed in `801bf32b3`) |

## Files

- `source/` — the PLP input files as used by the CEN (`plp*.dat`,
  `indhor.csv`), xz-compressed; `plpaflce.dat` is split into 12 parts
  (`plpaflce.dat.1.xz` … `.12.xz`).  `plp2gtopt` reads both forms
  directly.  Formerly `support/plp/long_term` in the gtopt repository.
- `case/` — `cen_long_term_1y.json`, per-class Parquet inputs,
  `boundary_cuts.csv`, `solvers/` (parameter files, comments removed) and
  `plp2gtopt_state.json` (exact converter invocation and options).

## How to run

Results are never written into this repository: run from an output
directory outside it.

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/medium_long_term/plp_23y/case
OUT=~/gtopt-cases-out/chile/medium_long_term/plp_23y
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/cen_long_term_1y.json" --set input_directory="$C" -d .
```

- `--set input_directory="$C"` resolves the Parquet/CSV inputs against
  `case/` while the run happens in the output directory.
- The case ships with `sddp_options.max_iterations = 3` (a smoke-test
  setting, not a converged policy); raise it with
  `--set sddp_options.max_iterations=N` for real studies.
- Solver: gtopt picks the best available plugin (`--solver highs|…`).
- Expected resources: **large** — SDDP over 12 phase LPs (0.67 M rows in
  total); plan for 8+ cores and 16+ GB RAM.
- Check that your gtopt reads the case as intended (LP size vs
  `catalog.json`): `gtopt_check_cases --repo "$REPO" --only plp_23y`.

## Regenerating `case/` from `source/`

`case/` was produced from this folder (`plp_23y/`) with

```bash
plp2gtopt -i source -o case -f case/cen_long_term_1y.json \
    -n cen_long_term_1y -s 12 -y 1 -a 0 --method sddp
```

(also `plp2gtopt --from-state case/plp2gtopt_state.json`; the snapshot
stores `source`/`case` relative to `plp_23y/`), keeping the planning
JSON, data directories, `boundary_cuts.csv` and `solvers/` (comments
removed), without the converter's `README.md` and `logs/`.
`tools/get_case.py` does exactly that from the catalogued flags:

```bash
tools/get_case.py rebuild plp_23y --out <dir outside the repo>
```

reproduces `case/` byte for byte (except `plp2gtopt_state.json`) with
the gtopt revision above.

| Flag | Meaning |
|---|---|
| `-n cen_long_term_1y` | System name (also the default JSON stem when `-f` is omitted). |
| `-s 12` | `--last-stage`: the first 12 (monthly) stages = 1 year. |
| `-y 1` | `--hydrologies`: hydrology 1 only. |
| `-a 0` | `--num-apertures 0`: no SDDP apertures. |
| `--method sddp` | One scene per scenario, one phase per stage. |

All other options are plp2gtopt defaults.  The PLP boundary cuts
(`plpplem1/2.dat`) go to `boundary_cuts.csv`, referenced from
`system.future_cost_array` by a path relative to `case/`.

### Variants

From `plp_23y/`, writing to a directory `<out>` outside the repository
(its basename is the default case stem).  Hydrologies are 1-based
`plpaflce.dat` columns (1–28, all simulated); PLP defines 28 apertures
per stage (`plpidap2.dat`).

| Variant | Command |
|---|---|
| This case: first year, hydrology 1, no apertures | `plp2gtopt -i source -o <out> -s 12 -y 1 -a 0 --method sddp` |
| **Full 23-year horizon** (276 stages), hydrology 1, no apertures | `plp2gtopt -i source -o <out> -y 1 -a 0 --method sddp` |
| Full 23-year horizon, all 28 hydrologies, all apertures | `plp2gtopt -i source -o <out> --method sddp` (`-y all`, `-a all`) |
| First 5 years (60 stages), 4 hydrologies | `plp2gtopt -i source -o <out> -s 60 -y 1,8,15,22 --method sddp` |
| First year, every hydrology | `plp2gtopt -i source -o <out> -s 12 --method sddp` |

`-s` / `--last-stage` is a **stage count** (default all 276) and `-t` an
accumulated time (`-t 5y`); `plp2gtopt --help` lists every flag.  The
full horizon is a large SDDP problem (276 phases × scenarios); expect
long runs and plan memory accordingly.
