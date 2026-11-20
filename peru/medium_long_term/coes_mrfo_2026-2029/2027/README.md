# coes_mrfo_2027 — Peru SEIN, COES SDDP base case 2027

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../../DISCLAIMER.md).

See [../README.md](../README.md) for the source, data terms (rights:
COES), modelling notes and how to regenerate.

| Field | Value |
|---|---|
| Case id | `peru/medium_long_term/coes_mrfo_2026-2029/2027` |
| Horizon | 12 monthly stages (2027-01 … 2027-12) = 12 SDDP phases, 60 blocks, 8,760 h |
| Scenarios | 56 historical hydrologies (1966–2021), one scene each |
| Network | 270 buses, 331 lines (DC, Kirchhoff + losses) |
| Units | 162 generators, 60 reservoirs |
| LP (`--lp-only`) | 6,640,984 rows, 13,452,824 cols, 32,908,848 nnz over 672 (scene, phase) LPs (gtopt development revision `75d9cec1ce81`) |
| Inputs | `../source/` (common) + `../source/2027/sddp.dat.xz` |
| Converter | `sddp2gtopt` from gtopt; rebuild with gtopt master of November 2026 or later (development revision used: `catalog.json`) |

## How to run

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/peru/medium_long_term/coes_mrfo_2026-2029/2027/case
OUT=~/gtopt-cases-out/peru/medium_long_term/coes_mrfo_2026-2029/2027
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/coes_mrfo_2027.json" --set input_directory="$C" -d . \
    --set sddp_options.max_iterations=15 --set sddp_options.num_apertures=8
```

Rebuild `case/`: `tools/get_case.py rebuild peru/medium_long_term/coes_mrfo_2026-2029/2027 --out <dir outside the repo>`.
