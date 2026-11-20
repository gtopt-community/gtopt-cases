# Guatemala — medium / long term (AMM long-term programmes)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

**AMM long-term SDDP programmes** (`sddp_plp_<years>/`): the PSR SDDP
databases of the AMM *Programación de Largo Plazo* (*Versión Definitiva*)
of six consecutive years, converted with `sddp2gtopt` from gtopt (rebuild
with gtopt master of November 2026 or later).  Each is a one-year
hydrothermal case (12 monthly SDDP phases, the study's single hydrology,
DC network with losses) with its converter inputs in `source/` (xz) and
the gtopt case in `case/`; the AMM archives are linked from each README
and not redistributed.

| Case | Horizon | Buses | Lines | Generators | LP rows (`--lp-only`) |
|---|---|---:|---:|---:|---:|
| [sddp_plp_2021-2022](sddp_plp_2021-2022/README.md) | 2021-05, 12 monthly stages × 9 blocks | 503 | 539 | 167 | 197,476 |
| [sddp_plp_2022-2023](sddp_plp_2022-2023/README.md) | 2022-05, 12 monthly stages × 9 blocks | 472 | 527 | 149 | 193,720 |
| [sddp_plp_2023-2024](sddp_plp_2023-2024/README.md) | 2023-05, 12 monthly stages × 9 blocks | 461 | 519 | 153 | 190,836 |
| [sddp_plp_2024-2025](sddp_plp_2024-2025/README.md) | 2024-05, 12 monthly stages × 9 blocks | 462 | 524 | 160 | 191,160 |
| [sddp_plp_2025-2026](sddp_plp_2025-2026/README.md) | 2025-05, 12 monthly stages × 9 blocks | 489 | 553 | 178 | 200,025 |
| [sddp_plp_2026-2027](sddp_plp_2026-2027/README.md) | 2026-05, 12 monthly stages × 9 blocks | 497 | 559 | 217 | 204,120 |

[`psse_bdd_2026-2027/`](psse_bdd_2026-2027/README.md): six DC-OPF
**network snapshots** converted with `psse2gtopt` from the PSS®E `.raw`
files of the AMM *Programación de Largo Plazo 2026-2027* study
(May 2026 – Apr 2027).  They are single-period snapshots (1 stage, 1 block,
1 scenario) of the long-term study's representative conditions — wet
season (September 2026) and dry season (March 2027), each at minimum,
medium and maximum demand — not a multi-stage long-term model.
