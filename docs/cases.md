# Case index

Every case in the repository, by application and country.  The same
information, machine-readable, is in [`catalog.json`](../catalog.json).

## Layout

```
gtopt-cases/
├── README.md            overview
├── docs/                case index, running, tools, provenance
├── DISCLAIMER.md        AS-IS terms: read before using any case
├── LICENSING.md         who holds which rights; LICENSES/ has the texts
├── THIRD_PARTY_DATA.md  data sources, rights holders, attribution
├── catalog.json         one entry per case: size, source (+sha256), converter
│                        revision and exact flags, profile, run command,
│                        rights holders and terms, notes
├── profiles/            shared gtopt options per application
├── tools/               get_case.py: download sources + run the converters
├── australia/           National Electricity Market (NEM), data from AEMO
│   ├── expansion/           2026 ISP PLEXOS model, FY2028-FY2030 expansion (plexos2gtopt.aemo_isp_expansion)
│   └── production_cost/     2026 ISP PLEXOS model, one-week dispatch (plexos2gtopt.aemo_isp)
├── chile/               Sistema Eléctrico Nacional (SEN), data from the CEN
│   ├── daily_scheduling/    CEN PCP daily unit commitment (PLEXOS → gtopt)
│   ├── medium_long_term/    CEN PLP hydrothermal SDDP (PLP → gtopt)
│   ├── transmission_planning/  CEN PET 2027 PLP bases, PLP-PET27 (PLP → gtopt)
│   └── expansion/           (no case yet)
├── guatemala/           Sistema Nacional Interconectado (SNI), data from AMM/EOR
│   ├── daily_scheduling/    PSR NCP daily/weekly dispatch (sddp2gtopt)
│   └── medium_long_term/    AMM SDDP programmes + PSS®E snapshots
├── ireland/             Single Electricity Market (SEM), data from the SEM Committee
│   └── unit_commitment/     SEM PLEXOS model week, recipe only: fetched + converted on demand
├── peru/                Sistema Eléctrico Interconectado Nacional (SEIN), data from the COES
│   └── medium_long_term/    COES SDDP base cases 2026-2029 (sddp2gtopt)
└── poland/              Polish transmission system, MATPOWER case3375wp (R. Korab)
    └── dc_opf/              single-hour DC OPF snapshot (pp2gtopt)
```

New countries go in their own top-level folder (e.g. `colombia/`) with the
same application sub-folders and a country `README.md`.

## Model elements by case

Counts of the gtopt elements in each case (from its `case/` JSON).  Blocks × stages × scenarios give the time and uncertainty structure.

| Case | Buses | Lines | Generators | Demands | Reservoirs | Turbines | Batteries | Water rights | Unit commitments | Blocks | Stages | Scenarios |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [expansion/isp2026_sc_exp_fy28_3y](../australia/expansion/isp2026_sc_exp_fy28_3y) | 15 | 18 | 765 | 32 | 22 | 101 | 223 | — | — | 1,152 | 48 | 1 |
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [production_cost/isp2026_sc_2027w03](../australia/production_cost/isp2026_sc_2027w03) | 15 | 18 | 523 | 15 | 22 | 95 | 85 | — | — | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [production_cost/isp2026_sc_2027w16](../australia/production_cost/isp2026_sc_2027w16) | 15 | 18 | 527 | 15 | 22 | 95 | 90 | — | — | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [production_cost/isp2026_sc_2027w29](../australia/production_cost/isp2026_sc_2027w29) | 15 | 18 | 540 | 15 | 22 | 95 | 100 | — | — | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [production_cost/isp2026_sc_2027w42](../australia/production_cost/isp2026_sc_2027w42) | 15 | 18 | 542 | 15 | 22 | 95 | 106 | — | — | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2025-10-05](../chile/daily_scheduling/pcp_2025-10-05) | 237 | 305 | 1,739 | 127 | 12 | 35 | 23 | 4 | 1,009 | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2025-10-19](../chile/daily_scheduling/pcp_2025-10-19) | 239 | 306 | 1,747 | 127 | 12 | 37 | 25 | 4 | 1,001 | 107 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2025-11-09](../chile/daily_scheduling/pcp_2025-11-09) | 239 | 307 | 1,751 | 127 | 12 | 34 | 25 | 5 | 1,005 | 118 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2025-11-23](../chile/daily_scheduling/pcp_2025-11-23) | 241 | 310 | 1,753 | 127 | 12 | 35 | 25 | 5 | 996 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2025-12-07](../chile/daily_scheduling/pcp_2025-12-07) | 241 | 309 | 1,753 | 127 | 12 | 34 | 26 | 6 | 1,020 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2025-12-21](../chile/daily_scheduling/pcp_2025-12-21) | 241 | 309 | 1,753 | 127 | 12 | 34 | 26 | 5 | 1,043 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-01-04](../chile/daily_scheduling/pcp_2026-01-04) | 243 | 311 | 1,763 | 127 | 12 | 36 | 29 | 5 | 1,026 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-01-18](../chile/daily_scheduling/pcp_2026-01-18) | 243 | 311 | 1,765 | 127 | 12 | 34 | 29 | 5 | 1,034 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-02-15](../chile/daily_scheduling/pcp_2026-02-15) | 246 | 315 | 1,769 | 127 | 12 | 35 | 32 | 6 | 1,008 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-03-15](../chile/daily_scheduling/pcp_2026-03-15) | 246 | 315 | 1,768 | 127 | 12 | 32 | 33 | 5 | 1,066 | 132 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-04-07](../chile/daily_scheduling/pcp_2026-04-07) | 247 | 317 | 1,772 | 127 | 12 | 30 | 36 | 4 | 1,047 | 111 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-04-12](../chile/daily_scheduling/pcp_2026-04-12) | 247 | 316 | 1,773 | 127 | 12 | 31 | 36 | 4 | 1,097 | 110 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-04-22](../chile/daily_scheduling/pcp_2026-04-22) | 247 | 317 | 1,776 | 127 | 12 | 35 | 36 | 4 | 1,100 | 111 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [daily_scheduling/pcp_2026-05-17](../chile/daily_scheduling/pcp_2026-05-17) | 251 | 321 | 1,790 | 139 | 12 | 32 | 41 | 4 | 1,093 | 110 | 1 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [medium_long_term/plp_23y](../chile/medium_long_term/plp_23y) | 339 | 449 | 1,628 | 161 | 10 | 156 | — | 3 | — | 120 | 12 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [medium_long_term/plp_2y](../chile/medium_long_term/plp_2y) | 245 | 343 | 1,892 | 137 | 10 | 176 | 112 | 4 | — | 270 | 52 | 4 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [medium_long_term/plp_5y](../chile/medium_long_term/plp_5y) | 241 | 345 | 1,880 | 139 | 10 | 177 | 68 | 4 | — | 234 | 72 | 4 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [transmission_planning/plp_pet27/e01](../chile/transmission_planning/plp_pet27/e01) | 292 | 430 | 933 | 148 | 10 | 173 | 158 | 3 | — | 96 | 12 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [transmission_planning/plp_pet27/e02](../chile/transmission_planning/plp_pet27/e02) | 292 | 430 | 965 | 148 | 10 | 173 | 171 | 3 | — | 96 | 12 | 1 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [transmission_planning/plp_pet27/e03](../chile/transmission_planning/plp_pet27/e03) | 292 | 430 | 988 | 148 | 10 | 173 | 202 | 3 | — | 96 | 12 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [daily_scheduling/ncp_pdd_2026-06-22](../guatemala/daily_scheduling/ncp_pdd_2026-06-22) | 830 | 955 | 229 | 241 | 44 | 98 | — | — | — | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [daily_scheduling/ncp_week_2026-06-21](../guatemala/daily_scheduling/ncp_week_2026-06-21) | 830 | 955 | 203 | 241 | — | — | — | — | — | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/psse_bdd_2026-2027/PAEMARMAX27](../guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMAX27) | 877 | 948 | 121 | 260 | — | — | — | — | — | 1 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/psse_bdd_2026-2027/PAEMARMED27](../guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMED27) | 877 | 948 | 114 | 261 | — | — | — | — | — | 1 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/psse_bdd_2026-2027/PAEMARMIN27](../guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMIN27) | 877 | 948 | 75 | 259 | — | — | — | — | — | 1 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/psse_bdd_2026-2027/PAESEPMAX26](../guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMAX26) | 871 | 942 | 122 | 253 | — | — | — | — | — | 1 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/psse_bdd_2026-2027/PAESEPMED26](../guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMED26) | 871 | 942 | 115 | 255 | — | — | — | — | — | 1 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/psse_bdd_2026-2027/PAESEPMIN26](../guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMIN26) | 871 | 942 | 96 | 253 | — | — | — | — | — | 1 | 1 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/sddp_plp_2021-2022](../guatemala/medium_long_term/sddp_plp_2021-2022) | 503 | 539 | 167 | 116 | 40 | 58 | — | — | — | 108 | 12 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/sddp_plp_2022-2023](../guatemala/medium_long_term/sddp_plp_2022-2023) | 472 | 527 | 149 | 119 | 43 | 58 | — | — | — | 108 | 12 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/sddp_plp_2023-2024](../guatemala/medium_long_term/sddp_plp_2023-2024) | 461 | 519 | 153 | 121 | 44 | 58 | — | — | — | 108 | 12 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/sddp_plp_2024-2025](../guatemala/medium_long_term/sddp_plp_2024-2025) | 462 | 524 | 160 | 127 | 44 | 58 | — | — | — | 108 | 12 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/sddp_plp_2025-2026](../guatemala/medium_long_term/sddp_plp_2025-2026) | 489 | 553 | 178 | 136 | 44 | 58 | — | — | — | 108 | 12 | 1 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [medium_long_term/sddp_plp_2026-2027](../guatemala/medium_long_term/sddp_plp_2026-2027) | 497 | 559 | 217 | 134 | 44 | 58 | — | — | — | 108 | 12 | 1 |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [unit_commitment/sem_2025w03](../ireland/unit_commitment/sem_2025w03) | 3 | 2 | 116 | 3 | — | — | 23 | — | 61 | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [unit_commitment/sem_2025w16](../ireland/unit_commitment/sem_2025w16) | 3 | 3 | 116 | 3 | — | — | 24 | — | 58 | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [unit_commitment/sem_2025w29](../ireland/unit_commitment/sem_2025w29) | 3 | 3 | 116 | 3 | — | — | 24 | — | 65 | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [unit_commitment/sem_2025w42](../ireland/unit_commitment/sem_2025w42) | 3 | 3 | 116 | 3 | — | — | 25 | — | 69 | 168 | 1 | 1 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [medium_long_term/coes_mrfo_2026-2029/2026](../peru/medium_long_term/coes_mrfo_2026-2029/2026) | 270 | 312 | 157 | 133 | 60 | 56 | — | — | — | 60 | 12 | 56 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [medium_long_term/coes_mrfo_2026-2029/2027](../peru/medium_long_term/coes_mrfo_2026-2029/2027) | 270 | 331 | 162 | 134 | 60 | 56 | — | — | — | 60 | 12 | 56 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [medium_long_term/coes_mrfo_2026-2029/2028](../peru/medium_long_term/coes_mrfo_2026-2029/2028) | 270 | 346 | 162 | 134 | 60 | 56 | — | — | — | 60 | 12 | 56 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [medium_long_term/coes_mrfo_2026-2029/2029](../peru/medium_long_term/coes_mrfo_2026-2029/2029) | 270 | 394 | 163 | 135 | 60 | 56 | — | — | — | 60 | 12 | 56 |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [dc_opf/case3375wp](../poland/dc_opf/case3375wp) | 3,374 | 4,161 | 489 | 2,414 | — | — | — | — | — | 1 | 1 | 1 |

## <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> Australia

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [expansion/isp2026_sc_exp_fy28_3y](../australia/expansion/isp2026_sc_exp_fy28_3y) | expansion | 15 | 1,152 | 1,681,763 | medium |
| [production_cost/isp2026_sc_2027w03](../australia/production_cost/isp2026_sc_2027w03) | production_cost | 15 | 168 | 126,129 | small |
| [production_cost/isp2026_sc_2027w16](../australia/production_cost/isp2026_sc_2027w16) | production_cost | 15 | 168 | 132,012 | small |
| [production_cost/isp2026_sc_2027w29](../australia/production_cost/isp2026_sc_2027w29) | production_cost | 15 | 168 | 143,792 | small |
| [production_cost/isp2026_sc_2027w42](../australia/production_cost/isp2026_sc_2027w42) | production_cost | 15 | 168 | 150,860 | small |

Four one-week hourly dispatches, one per season of 2027 (18-24 January,
19-25 April, 19-25 July and 18-24 October), of the AEMO 2026 ISP PLEXOS
model, Step Change scenario; prototype without expansion or PLEXOS
constraints.  See [australia/README.md](../australia/README.md).  The expansion case plans generation,
storage and network augmentations over FY2028-FY2030 (plus a fill year)
with one representative day of 24 hourly blocks per month.

## <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> Chile: daily scheduling — day-ahead unit commitment (monolithic MIP)

> **Note.** The 14 PCP cases try to reproduce the conditions under which
> PLEXOS is run for the CEN daily program.  That configuration (model
> settings, constraints, line ratings and expansions, solver settings, …)
> is defined by the CEN (Coordinador Eléctrico Nacional), not by the gtopt
> project.  The profile, converter flags and line lifts used here only aim
> to replicate it; they are not gtopt's recommended defaults for daily
> scheduling.

| Case | Buses | Generators | Blocks (horizon) | LP rows | Resources |
|---|---:|---:|---:|---:|---|
| [pcp_2025-10-05](../chile/daily_scheduling/pcp_2025-10-05) | 237 | 1739 | 168 (168 h) | 1,288,403 | large |
| [pcp_2025-10-19](../chile/daily_scheduling/pcp_2025-10-19) | 239 | 1747 | 107 (144 h) | 820,905 | large |
| [pcp_2025-11-09](../chile/daily_scheduling/pcp_2025-11-09) | 239 | 1751 | 118 (144 h) | 910,149 | large |
| [pcp_2025-11-23](../chile/daily_scheduling/pcp_2025-11-23) | 241 | 1753 | 132 (168 h) | 1,015,462 | large |
| [pcp_2025-12-07](../chile/daily_scheduling/pcp_2025-12-07) | 241 | 1753 | 132 (168 h) | 1,031,274 | large |
| [pcp_2025-12-21](../chile/daily_scheduling/pcp_2025-12-21) | 241 | 1753 | 132 (168 h) | 1,043,802 | large |
| [pcp_2026-01-04](../chile/daily_scheduling/pcp_2026-01-04) | 243 | 1763 | 132 (168 h) | 1,037,557 | large |
| [pcp_2026-01-18](../chile/daily_scheduling/pcp_2026-01-18) | 243 | 1765 | 132 (168 h) | 1,041,981 | large |
| [pcp_2026-02-15](../chile/daily_scheduling/pcp_2026-02-15) | 246 | 1769 | 132 (168 h) | 1,036,862 | large |
| [pcp_2026-03-15](../chile/daily_scheduling/pcp_2026-03-15) | 246 | 1768 | 132 (168 h) | 1,066,186 | large |
| [pcp_2026-04-07](../chile/daily_scheduling/pcp_2026-04-07) | 247 | 1772 | 111 (168 h) | 889,504 | large |
| [pcp_2026-04-12](../chile/daily_scheduling/pcp_2026-04-12) | 247 | 1773 | 110 (168 h) | 906,263 | large |
| [pcp_2026-04-22](../chile/daily_scheduling/pcp_2026-04-22) | 247 | 1776 | 111 (168 h) | 918,500 | large |
| [pcp_2026-05-17](../chile/daily_scheduling/pcp_2026-05-17) | 251 | 1790 | 110 (168 h) | 915,043 | large |

**Source-only days** (no gtopt case built or checked; sizes unknown):
14 further PCP days, test days for the study of negative nodal prices
(2024-09-01, 2024-10-03, 2024-12-15, 2025-02-17, 2025-04-10, 2025-04-27,
2025-06-26, 2025-09-16) and for the comparison of line-loss models
(2021-10-17, 2021-10-24, 2026-05-10, 2026-05-25, 2026-11-03, 2026-11-09).
The four 2026 days keep their PLEXOS input in `source/`; the other ten
are fetched from the public CEN files.  `tools/get_case.py fetch
pcp_<date>` builds any of them; see the
[daily-scheduling README](../chile/daily_scheduling/README.md#source-only-days).

Line lifts, converter flags and run instructions:
[chile/daily_scheduling/README.md](../chile/daily_scheduling/README.md).

## <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> Chile: medium / long term — hydrothermal SDDP

One folder per CEN PLP input set: `source/` (PLP inputs) and `case/` (the
gtopt case converted with `plp2gtopt`); other horizons and hydrology sets
are documented as `plp2gtopt` variants in each README.

| Case | Source (PLP) | Case | Buses | LP rows | Resources |
|---|---|---|---:|---:|---|
| [plp_2y](../chile/medium_long_term/plp_2y) | 52 stages, 68 hydrologies | 52 phases, 4 hydrologies, 20 apertures | 245 | 4,279,344 | large |
| [plp_5y](../chile/medium_long_term/plp_5y) | 72 stages (~4.5 years), 65 hydrologies | 72 phases, 4 hydrologies, 34 apertures | 241 | 3,593,820 | large |
| [plp_23y](../chile/medium_long_term/plp_23y) | 276 monthly stages (23 years), 28 hydrologies | first year: 12 phases, 1 hydrology | 339 | 673,493 | large |

See [chile/medium_long_term/README.md](../chile/medium_long_term/README.md).

## <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> Chile: transmission planning — PLP-PET27 (hydrothermal SDDP)

PLP bases of the CEN **Proceso de Planificación de la Transmisión 2027**
(Diagnóstico, Anexo IV.1), one case per energy scenario in configuration
CS_I; the group folder also holds the CEN methodology (Anexo II).

| Case | Source (PLP) | Case | Buses | LP rows | Resources |
|---|---|---|---:|---:|---|
| [plp_pet27/e01](../chile/transmission_planning/plp_pet27/e01) | `PET27_E01_CS_I_v4_d`: 276 monthly stages, 25 hydrologies | first year: 12 phases, 1 hydrology | 292 | 455,069 | medium |
| [plp_pet27/e02](../chile/transmission_planning/plp_pet27/e02) | `PET27_E02_CS_I_v4_d`: 276 monthly stages, 25 hydrologies | first year: 12 phases, 1 hydrology | 292 | 458,969 | medium |
| [plp_pet27/e03](../chile/transmission_planning/plp_pet27/e03) | `PET27_E03_CS_I_v4_d`: 276 monthly stages, 25 hydrologies | first year: 12 phases, 1 hydrology | 292 | 468,269 | medium |

See [chile/transmission_planning/plp_pet27/README.md](../chile/transmission_planning/plp_pet27/README.md).

## <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> Guatemala

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [daily_scheduling/ncp_pdd_2026-06-22](../guatemala/daily_scheduling/ncp_pdd_2026-06-22) | daily_scheduling | 830 | 168 | 192,056 | medium |
| [daily_scheduling/ncp_week_2026-06-21](../guatemala/daily_scheduling/ncp_week_2026-06-21) | daily_scheduling | 830 | 168 | 192,024 | medium |
| [medium_long_term/psse_bdd_2026-2027/PAESEPMIN26](../guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMIN26) | medium_long_term | 871 | 1 | 943 | small |
| [medium_long_term/psse_bdd_2026-2027/PAESEPMED26](../guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMED26) | medium_long_term | 871 | 1 | 943 | small |
| [medium_long_term/psse_bdd_2026-2027/PAESEPMAX26](../guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMAX26) | medium_long_term | 871 | 1 | 943 | small |
| [medium_long_term/psse_bdd_2026-2027/PAEMARMIN27](../guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMIN27) | medium_long_term | 877 | 1 | 949 | small |
| [medium_long_term/psse_bdd_2026-2027/PAEMARMED27](../guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMED27) | medium_long_term | 877 | 1 | 949 | small |
| [medium_long_term/psse_bdd_2026-2027/PAEMARMAX27](../guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMAX27) | medium_long_term | 877 | 1 | 949 | small |
| [medium_long_term/sddp_plp_2021-2022](../guatemala/medium_long_term/sddp_plp_2021-2022) | medium_long_term | 503 | 108 | 197,476 | medium |
| [medium_long_term/sddp_plp_2022-2023](../guatemala/medium_long_term/sddp_plp_2022-2023) | medium_long_term | 472 | 108 | 193,720 | medium |
| [medium_long_term/sddp_plp_2023-2024](../guatemala/medium_long_term/sddp_plp_2023-2024) | medium_long_term | 461 | 108 | 190,836 | medium |
| [medium_long_term/sddp_plp_2024-2025](../guatemala/medium_long_term/sddp_plp_2024-2025) | medium_long_term | 462 | 108 | 191,160 | medium |
| [medium_long_term/sddp_plp_2025-2026](../guatemala/medium_long_term/sddp_plp_2025-2026) | medium_long_term | 489 | 108 | 200,025 | medium |
| [medium_long_term/sddp_plp_2026-2027](../guatemala/medium_long_term/sddp_plp_2026-2027) | medium_long_term | 497 | 108 | 204,120 | medium |

See [guatemala/README.md](../guatemala/README.md).

## <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> Ireland

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [unit_commitment/sem_2025w03](../ireland/unit_commitment/sem_2025w03) | unit_commitment | 3 | 168 | 102,351 | small |
| [unit_commitment/sem_2025w16](../ireland/unit_commitment/sem_2025w16) | unit_commitment | 3 | 168 | 100,505 | small |
| [unit_commitment/sem_2025w29](../ireland/unit_commitment/sem_2025w29) | unit_commitment | 3 | 168 | 105,724 | small |
| [unit_commitment/sem_2025w42](../ireland/unit_commitment/sem_2025w42) | unit_commitment | 3 | 168 | 112,609 | small |

Four one-week unit commitments, one per season of 2025 (13-19 January,
14-20 April, 14-20 July and 13-19 October), of the SEM PLEXOS Forecast
Model 2024-2032.  **Recipe only**: the SEM data are not redistributed;
`tools/get_case.py fetch sem_2025w03` (or `w16`, `w29`, `w42`) downloads and
converts them.  See
[ireland/README.md](../ireland/README.md).

## <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> Peru

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [medium_long_term/coes_mrfo_2026-2029/2026](../peru/medium_long_term/coes_mrfo_2026-2029/2026) | medium_long_term | 270 | 60 | 6,457,304 | large |
| [medium_long_term/coes_mrfo_2026-2029/2027](../peru/medium_long_term/coes_mrfo_2026-2029/2027) | medium_long_term | 270 | 60 | 6,640,984 | large |
| [medium_long_term/coes_mrfo_2026-2029/2028](../peru/medium_long_term/coes_mrfo_2026-2029/2028) | medium_long_term | 270 | 60 | 6,915,664 | large |
| [medium_long_term/coes_mrfo_2026-2029/2029](../peru/medium_long_term/coes_mrfo_2026-2029/2029) | medium_long_term | 270 | 60 | 7,514,584 | large |

See [peru/README.md](../peru/README.md).

## <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> Poland

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [dc_opf/case3375wp](../poland/dc_opf/case3375wp) | dc_opf | 3,374 | 1 | 4,162 | small |

Single-hour DC OPF of the Polish system (winter 2007-08 evening peak),
from the MATPOWER case file `case3375wp.m`.  See
[poland/README.md](../poland/README.md).

## Expansion planning

No case yet; see [chile/expansion/README.md](../chile/expansion/README.md).

## Summary by country

| Country | System | Data source | Daily scheduling | Medium/long term | Expansion |
|---|---|---|---:|---:|---:|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [Australia](../australia/README.md) | NEM | AEMO (Australian Energy Market Operator), 2026 ISP | 1 weekly dispatch (production cost) | — | — |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [Chile](../chile/README.md) | SEN | CEN (Coordinador Eléctrico Nacional) | 14 | 3 + 3 PLP-PET27 (transmission planning) | — |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [Guatemala](../guatemala/README.md) | SNI | AMM (Administrador del Mercado Mayorista), EOR (Ente Operador Regional) | 2 | 6 SDDP + 6 snapshots | — |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [Ireland](../ireland/README.md) | SEM | SEM Committee (CRU, Utility Regulator); not redistributed, fetched on demand | 1 weekly unit commitment | — | — |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [Peru](../peru/README.md) | SEIN | COES (Comité de Operación Económica del Sistema Interconectado Nacional) | — | 4 SDDP | — |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [Poland](../poland/README.md) | Polish transmission system | MATPOWER `case3375wp` (data by R. Korab, Silesian University of Technology) | — | 1 DC OPF snapshot | — |


Each country README names the rights holders of its source data
(Australia: AEMO; Chile: CEN; Guatemala: AMM and EOR; Ireland: SEM
Committee, CRU and UR; Peru: COES; Poland: R. Korab / MATPOWER).
All third-party data sources, their terms and the attribution to give are
listed in [`THIRD_PARTY_DATA.md`](../THIRD_PARTY_DATA.md).  New countries
follow the same pattern.
