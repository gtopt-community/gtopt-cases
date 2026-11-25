# plp_pet27/e02_sens — PLP-PET27, energy scenario E02 (CS_I_sens), 1-year SDDP case

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../../DISCLAIMER.md).

PLP base `PET27_E02_CS_I_v4_d_sens` of the CEN **Proceso de Planificación de la
Transmisión 2027** (Diagnóstico, Anexo IV.1): energy scenario **E02**,
the entry-year sensitivity of the plan of works (*sensibilidad año EO*): CS-I with the dates of about 15 Centro-Sur works moved (Charrúa, Pichirropulli, Entre Ríos, Baja Cordillera–Alto Jahuel, …); most changes fall after the first year.  Same horizon, hydrologies and cut as [`e02`](../e02) (first year,
hydrology 1, no apertures).  Context and the other set-ups:
[group README](../README.md).

| Field | Value |
|---|---|
| Case id | `chile/transmission_planning/plp_pet27/e02_sens` |
| Horizon | 12 monthly stages = 12 SDDP phases, 96 blocks, 8,760 h |
| Hydrologies | 1 scenario: hydrology 1 (of 25); no apertures (`-a 0`) |
| Network | 292 buses, 430 lines (time-varying ratings, status and R/X from `mantlin.csv`) |
| Units | 965 generators, 171 batteries |
| LP (`--lp-only`) | 474,617 rows over 12 phase LPs (gtopt 1.1.0) |
| Future cost | `system.future_cost_array`: `boundary_cuts.csv` (PLP `plpplem1/2.dat` cuts), `mode: phi_expectation` |
| Converter | `plp2gtopt` from gtopt 1.1.0 or later; revision in `catalog.json` |

## Files

- `source/` — **only the files that differ** from `PET27_E02_CS_I_v4_d`
  (`mantlin.csv`), xz-compressed.
  The other inputs are those of [`../e02/source`](../e02/source).
- `case/` — `pet27_e02_cs_i_sens_1y.json`, per-class Parquet inputs, `boundary_cuts.csv`
  and `solvers/`.  Files identical to
  [`../e02/case`](../e02/case) are relative symbolic links to it (only
  the files that change are stored; `tools/get_case.py rebuild` writes
  plain files).

## How to run

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/transmission_planning/plp_pet27/e02_sens/case
OUT=~/gtopt-cases-out/chile/transmission_planning/plp_pet27/e02_sens
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pet27_e02_cs_i_sens_1y.json" --set input_directory="$C" -d .
```

Check the LP size against `catalog.json`:
`gtopt_check_cases --repo "$REPO" --only plp_pet27/e02_sens`.

## Regenerating `case/`

`tools/get_case.py` stages `../e02/source` with `source/` overlaid (and
the split parts joined), then runs `plp2gtopt` with the catalogued flags:

```bash
tools/get_case.py rebuild chile/transmission_planning/plp_pet27/e02_sens --out <dir outside the repo>
```

For longer horizons or all hydrologies, stage the same overlay and use
the flags of the [`e02` variants](../e02/README.md#variants) (e.g. drop
`-s 12 -y 1 -a 0` for the full 23-year, 25-hydrology problem).
