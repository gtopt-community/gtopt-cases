# coes_mrfo_2028 — Peru SEIN, COES SDDP base case 2028

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../../../DISCLAIMER.md).

See [../README.md](../README.md) for the source, data terms (rights:
COES), modelling notes and how to regenerate.

| Field | Value |
|---|---|
| Case id | `peru/medium_long_term/coes_mrfo_2026-2029/2028` |
| Horizon | 12 monthly stages (2028-01 … 2028-12) = 12 SDDP phases, 60 blocks, 8,760 h |
| Scenarios | 56 historical hydrologies (1966–2021), one scene each |
| Network | 270 buses, 346 lines (DC, Kirchhoff + losses) |
| Units | 162 generators, 60 reservoirs |
| LP (`--lp-only`) | 6,915,664 rows, 14,049,224 cols, 34,917,008 nnz over 672 (scene, phase) LPs (gtopt development revision `75d9cec1ce81`) |
| Inputs | `../source/` (common) + `../source/2028/sddp.dat.xz` |
| Converter | `sddp2gtopt` from gtopt; rebuild with gtopt master of November 2026 or later (development revision used: `catalog.json`) |

## How to run

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/peru/medium_long_term/coes_mrfo_2026-2029/2028/case
OUT=~/gtopt-cases-out/peru/medium_long_term/coes_mrfo_2026-2029/2028
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/coes_mrfo_2028.json" --set input_directory="$C" -d . \
    --set sddp_options.max_iterations=15 --set sddp_options.num_apertures=8
```

Rebuild `case/`: `tools/get_case.py rebuild peru/medium_long_term/coes_mrfo_2026-2029/2028 --out <dir outside the repo>`.
