# plp_pet27/e02 — PLP-PET27, energy scenario E02 (CS_I), 1-year SDDP case

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../../DISCLAIMER.md).

PLP base `PET27_E02_CS_I_v4_d` of the CEN **Proceso de Planificación de
la Transmisión 2027** (Diagnóstico, Anexo IV.1): energy scenario **E02**,
transmission configuration **CS_I**.  276 monthly stages (April 2026 – March 2049,
8 blocks each), 25 hydrologies, transmission plan of works in
`mantlin.csv`.  The committed case is its **first year**; the full
horizon is a [variant](#variants).  Context, the other set-ups (CS_I_sens,
NC_VI) and what the base does not contain (investment costs, candidates):
[group README](../README.md).

| Field | Value |
|---|---|
| Case id | `chile/transmission_planning/plp_pet27/e02` |
| Horizon | 12 monthly stages = 12 SDDP phases, 96 blocks, 8,760 h |
| Hydrologies | 1 scenario: hydrology 1 (of 25); no apertures (`-a 0`) |
| Network | 292 buses, 430 lines (time-varying ratings, status and R/X from `mantlin.csv`) |
| Units | 965 generators, 171 batteries, 10 reservoirs, 173 turbines, 3 flow rights |
| LP (`--lp-only`) | 475,577 rows over 12 phase LPs (gtopt 1.1.0) |
| Method / profile | sddp, no profile (method and SDDP options are in the case JSON) |
| Future cost | `system.future_cost_array`: `boundary_cuts.csv` (PLP `plpplem1/2.dat` cuts), `mode: phi_expectation` |
| Converter | `plp2gtopt` from gtopt 1.1.0 or later (`mantlin.csv` support); revision in `catalog.json` |

## Files

- `source/` — the PLP input files as published by the CEN (`plp*.dat`,
  `indhor.csv`, `mantlin.csv`, `run_plp_plani.sh`), xz-compressed;
  `plpaflce.dat` is split into 4 parts (`plpaflce.dat.1.xz` …
  `.4.xz`).  `plp2gtopt` reads both forms directly.  The IPLP workbook
  (`.xlsm`) is not included.
- `case/` — `pet27_e02_cs_i_1y.json`, per-class Parquet inputs,
  `boundary_cuts.csv` and `solvers/` (parameter files, comments
  removed).

## How to run

Results are never written into this repository: run from an output
directory outside it.

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/transmission_planning/plp_pet27/e02/case
OUT=~/gtopt-cases-out/chile/transmission_planning/plp_pet27/e02
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pet27_e02_cs_i_1y.json" --set input_directory="$C" -d .
```

- `--set input_directory="$C"` resolves the Parquet/CSV inputs against
  `case/` while the run happens in the output directory.
- The PLP base sets no iteration limit (`PDMaxIte = 0`, it warm-starts
  from the CEN's own cuts), so gtopt's SDDP defaults apply; cap them with
  `--set sddp_options.max_iterations=N`.
- Solver: gtopt picks the best available plugin (`--solver highs|…`).
- Expected resources: **medium** — SDDP over 12 phase LPs; the 1-year,
  1-hydrology case converges in a few minutes on 8 cores.
- Check that your gtopt reads the case as intended (LP size vs
  `catalog.json`):
  `gtopt_check_cases --repo "$REPO" --only plp_pet27/e02`.

## Regenerating `case/` from `source/`

From this folder (`plp_pet27/e02/`):

```bash
plp2gtopt -i source -o case -f case/pet27_e02_cs_i_1y.json \
    -n pet27_e02_cs_i_1y -s 12 -y 1 -a 0 --method sddp
```

keeping the planning JSON, data directories, `boundary_cuts.csv` and
`solvers/` (comments removed), without the converter's `README.md` and
`logs/`.  `tools/get_case.py` does exactly that from the catalogued
flags:

```bash
tools/get_case.py rebuild chile/transmission_planning/plp_pet27/e02 --out <dir outside the repo>
```

### Variants

From `plp_pet27/e02/`, writing to a directory `<out>` outside the
repository.  Hydrologies are 1-based `plpaflce.dat` columns (1–25); PLP
defines 25 apertures per stage (`plpidap2.dat`).

| Variant | Command |
|---|---|
| This case: first year, hydrology 1, no apertures | `plp2gtopt -i source -o <out> -s 12 -y 1 -a 0 --method sddp` |
| First 5 years (60 stages), all 25 hydrologies | `plp2gtopt -i source -o <out> -s 60 -a 0 --method sddp` |
| Planning horizon of the methodology (20 years, 240 stages), 25 hydrologies | `plp2gtopt -i source -o <out> -s 240 --method sddp` |
| Full horizon (276 stages), 5 hydrologies, no apertures | `plp2gtopt -i source -o <out> -y 1,6,11,16,21 -a 0 --method sddp` |
| Full horizon (276 stages), 5 hydrologies, as a 4-level cascade (warmup, uninodal, transport, full network) | `plp2gtopt -i source -o <out> -y 1,6,11,16,21 --method cascade` |
| **Full horizon** (276 stages), all hydrologies and apertures | `plp2gtopt -i source -o <out> --method sddp` |

The full horizon is a large SDDP problem (276 phases × 25 scenarios); expect
long runs and plan memory accordingly.  The 5-hydrology full-horizon variant
converts and runs with gtopt 1.1.0 (`--set solver_options.threads=1`;
measured on e01 and e02): on a 40-core, 247 GB machine the first SDDP
iteration took about 2.5 h and the process peaked at 84–90 GB of resident
memory, so give it at least ~100 GB and run the scenarios one at a time.

To run the cascade, writing outside the repository (plp2gtopt names the case
JSON after the output directory; the levels and their apertures, 1, 4, 8 and
all, are in `options.cascade_options` of that JSON):

```bash
OUT=$HOME/pet27_e02_cascade
plp2gtopt -i source -o "$OUT" -y 1,6,11,16,21 --method cascade
ulimit -c unlimited
cd "$(dirname "$OUT")" && mkdir -p run_e02_cascade && cd run_e02_cascade
gtopt "$OUT/$(basename "$OUT").json" --set input_directory="$OUT" -d .
```

With gtopt 1.1.0 this converts in about 4 min and builds the LPs
(`--lp-only`) in about 25 s with 23 GB of memory (e01).

The CS_I_sens set-up of this scenario is [`e02_sens`](../e02_sens); for NC_VI see the [group README](../README.md#variants-of-the-publication).
