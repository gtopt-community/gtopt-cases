# gtopt-cases

> [!IMPORTANT]
> **Licensing at a glance**
> - **Data** (`source/`, `case/`): third-party data; **this repository
>   grants no licence** over it.  The rights stay with the publishers: CEN
>   (Chile), AMM and EOR (Guatemala), COES (Peru), and R. Korab / MATPOWER
>   (Poland).
> - **Tools** (`tools/`): AGPL-3.0-or-later with the GTOpt Solver Plugin
>   Exception, or the GTOpt Commercial License.
> - **Conversion layer** written by the gtopt authors (layout, profiles,
>   line lifts, catalog, documentation): CC0-1.0, to the extent they hold
>   any rights in it.
>
> Details in [`LICENSING.md`](LICENSING.md) and
> [`THIRD_PARTY_DATA.md`](THIRD_PARTY_DATA.md); removal requests:
> [below](#removal-requests).

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](DISCLAIMER.md).

A structured collection of study cases for
[gtopt](https://github.com/gtopt-community/gtopt), the C++ generation and
transmission expansion planning (GTEP) / SDDP solver.

**This repository publishes inputs only**: the source data as published
by the system operators (`source/`), the gtopt case inputs built from them
(`case/`), the shared option profiles, and instructions on how to run each
case with gtopt.  It contains **no results of any kind** (no objective
values, marginal costs, solver logs or operator solutions): run gtopt and
the analysis tools with their output outside the repository (e.g.
`~/gtopt-cases-out`).

Cases are organised by **country first, then application**;
[`catalog.json`](catalog.json) indexes every case in machine-readable form.

```
gtopt-cases/
├── README.md            this index
├── DISCLAIMER.md        AS-IS terms: read before using any case
├── LICENSING.md         who holds which rights; LICENSES/ has the texts
├── THIRD_PARTY_DATA.md  data sources, rights holders, attribution
├── catalog.json         one entry per case: size, source (+sha256), converter
│                        revision and exact flags, profile, run command,
│                        rights holders and terms, notes
├── profiles/            shared gtopt options per application
├── tools/               get_case.py: download sources + run the converters
├── chile/               Sistema Eléctrico Nacional (SEN), data from the CEN
│   ├── daily_scheduling/    CEN PCP daily unit commitment (PLEXOS → gtopt)
│   ├── medium_long_term/    CEN PLP hydrothermal SDDP (PLP → gtopt)
│   └── expansion/           (no case yet)
├── guatemala/           Sistema Nacional Interconectado (SNI), data from AMM/EOR
│   ├── daily_scheduling/    PSR NCP daily/weekly dispatch (sddp2gtopt)
│   └── medium_long_term/    AMM long-term SDDP programmes (sddp2gtopt) and PSS®E snapshots (psse2gtopt)
├── peru/                Sistema Eléctrico Interconectado Nacional (SEIN), data from the COES
│   └── medium_long_term/    COES SDDP base cases 2026-2029 (sddp2gtopt)
└── poland/              Polish transmission system, MATPOWER case3375wp (R. Korab)
    └── dc_opf/              single-hour DC OPF snapshot (pp2gtopt)
```

New countries go in their own top-level folder (e.g. `colombia/`) with the
same application sub-folders and a country `README.md`.

## Cases by application

### Daily scheduling — day-ahead unit commitment (monolithic MIP)

> **Note.** The 14 PCP cases try to reproduce the conditions under which
> PLEXOS is run for the CEN daily program.  That configuration (model
> settings, constraints, line ratings and expansions, solver settings, …)
> is defined by the CEN (Coordinador Eléctrico Nacional), not by the gtopt
> project.  The profile, converter flags and line lifts used here only aim
> to replicate it; they are not gtopt's recommended defaults for daily
> scheduling.

| Case | Buses | Generators | Blocks (horizon) | LP rows | Resources |
|---|---:|---:|---:|---:|---|
| [pcp_2025-10-05](chile/daily_scheduling/pcp_2025-10-05) | 237 | 1739 | 168 (168 h) | 1,288,403 | large |
| [pcp_2025-10-19](chile/daily_scheduling/pcp_2025-10-19) | 239 | 1747 | 107 (144 h) | 820,905 | large |
| [pcp_2025-11-09](chile/daily_scheduling/pcp_2025-11-09) | 239 | 1751 | 118 (144 h) | 910,149 | large |
| [pcp_2025-11-23](chile/daily_scheduling/pcp_2025-11-23) | 241 | 1753 | 132 (168 h) | 1,015,462 | large |
| [pcp_2025-12-07](chile/daily_scheduling/pcp_2025-12-07) | 241 | 1753 | 132 (168 h) | 1,031,274 | large |
| [pcp_2025-12-21](chile/daily_scheduling/pcp_2025-12-21) | 241 | 1753 | 132 (168 h) | 1,043,802 | large |
| [pcp_2026-01-04](chile/daily_scheduling/pcp_2026-01-04) | 243 | 1763 | 132 (168 h) | 1,037,557 | large |
| [pcp_2026-01-18](chile/daily_scheduling/pcp_2026-01-18) | 243 | 1765 | 132 (168 h) | 1,041,981 | large |
| [pcp_2026-02-15](chile/daily_scheduling/pcp_2026-02-15) | 246 | 1769 | 132 (168 h) | 1,036,862 | large |
| [pcp_2026-03-15](chile/daily_scheduling/pcp_2026-03-15) | 246 | 1768 | 132 (168 h) | 1,066,186 | large |
| [pcp_2026-04-07](chile/daily_scheduling/pcp_2026-04-07) | 247 | 1772 | 111 (168 h) | 889,504 | large |
| [pcp_2026-04-12](chile/daily_scheduling/pcp_2026-04-12) | 247 | 1773 | 110 (168 h) | 906,263 | large |
| [pcp_2026-04-22](chile/daily_scheduling/pcp_2026-04-22) | 247 | 1776 | 111 (168 h) | 918,500 | large |
| [pcp_2026-05-17](chile/daily_scheduling/pcp_2026-05-17) | 251 | 1790 | 110 (168 h) | 915,043 | large |

Line lifts, converter flags and run instructions:
[chile/daily_scheduling/README.md](chile/daily_scheduling/README.md).

### Medium / long term — hydrothermal SDDP

One folder per CEN PLP input set: `source/` (PLP inputs) and `case/` (the
gtopt case converted with `plp2gtopt`); other horizons and hydrology sets
are documented as `plp2gtopt` variants in each README.

| Case | Source (PLP) | Case | Buses | LP rows | Resources |
|---|---|---|---:|---:|---|
| [plp_2y](chile/medium_long_term/plp_2y) | 52 stages, 68 hydrologies | 52 phases, 4 hydrologies, 20 apertures | 245 | 4,279,344 | large |
| [plp_5y](chile/medium_long_term/plp_5y) | 72 stages (~4.5 years), 65 hydrologies | 72 phases, 4 hydrologies, 34 apertures | 241 | 3,593,820 | large |
| [plp_23y](chile/medium_long_term/plp_23y) | 276 monthly stages (23 years), 28 hydrologies | first year: 12 phases, 1 hydrology | 339 | 673,493 | large |

See [chile/medium_long_term/README.md](chile/medium_long_term/README.md).

### Guatemala

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [daily_scheduling/ncp_pdd_2026-06-22](guatemala/daily_scheduling/ncp_pdd_2026-06-22) | daily_scheduling | 830 | 168 | 192,056 | medium |
| [daily_scheduling/ncp_week_2026-06-21](guatemala/daily_scheduling/ncp_week_2026-06-21) | daily_scheduling | 830 | 168 | 160,608 | medium |
| [medium_long_term/psse_bdd_2026-2027/PAESEPMIN26](guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMIN26) | medium_long_term | 871 | 1 | 943 | small |
| [medium_long_term/psse_bdd_2026-2027/PAESEPMED26](guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMED26) | medium_long_term | 871 | 1 | 943 | small |
| [medium_long_term/psse_bdd_2026-2027/PAESEPMAX26](guatemala/medium_long_term/psse_bdd_2026-2027/PAESEPMAX26) | medium_long_term | 871 | 1 | 943 | small |
| [medium_long_term/psse_bdd_2026-2027/PAEMARMIN27](guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMIN27) | medium_long_term | 877 | 1 | 949 | small |
| [medium_long_term/psse_bdd_2026-2027/PAEMARMED27](guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMED27) | medium_long_term | 877 | 1 | 949 | small |
| [medium_long_term/psse_bdd_2026-2027/PAEMARMAX27](guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMAX27) | medium_long_term | 877 | 1 | 949 | small |
| [medium_long_term/sddp_plp_2021-2022](guatemala/medium_long_term/sddp_plp_2021-2022) | medium_long_term | 503 | 108 | 197,476 | medium |
| [medium_long_term/sddp_plp_2022-2023](guatemala/medium_long_term/sddp_plp_2022-2023) | medium_long_term | 472 | 108 | 193,720 | medium |
| [medium_long_term/sddp_plp_2023-2024](guatemala/medium_long_term/sddp_plp_2023-2024) | medium_long_term | 461 | 108 | 190,836 | medium |
| [medium_long_term/sddp_plp_2024-2025](guatemala/medium_long_term/sddp_plp_2024-2025) | medium_long_term | 462 | 108 | 191,160 | medium |
| [medium_long_term/sddp_plp_2025-2026](guatemala/medium_long_term/sddp_plp_2025-2026) | medium_long_term | 489 | 108 | 200,025 | medium |
| [medium_long_term/sddp_plp_2026-2027](guatemala/medium_long_term/sddp_plp_2026-2027) | medium_long_term | 497 | 108 | 204,120 | medium |

See [guatemala/README.md](guatemala/README.md).

### Peru

> [!CAUTION]
> Conversion not yet validated; use for software testing only.

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [medium_long_term/coes_mrfo_2026-2029/2026](peru/medium_long_term/coes_mrfo_2026-2029/2026) | medium_long_term | 270 | 60 | 6,457,304 | large |
| [medium_long_term/coes_mrfo_2026-2029/2027](peru/medium_long_term/coes_mrfo_2026-2029/2027) | medium_long_term | 270 | 60 | 6,640,984 | large |
| [medium_long_term/coes_mrfo_2026-2029/2028](peru/medium_long_term/coes_mrfo_2026-2029/2028) | medium_long_term | 270 | 60 | 6,915,664 | large |
| [medium_long_term/coes_mrfo_2026-2029/2029](peru/medium_long_term/coes_mrfo_2026-2029/2029) | medium_long_term | 270 | 60 | 7,514,584 | large |

See [peru/README.md](peru/README.md).

### Poland

| Case | Application | Buses | Blocks | LP rows | Resources |
|---|---|---:|---:|---:|---|
| [dc_opf/case3375wp](poland/dc_opf/case3375wp) | dc_opf | 3,374 | 1 | 4,162 | small |

Single-hour DC OPF of the Polish system (winter 2007-08 evening peak),
from the MATPOWER case file `case3375wp.m`.  See
[poland/README.md](poland/README.md).

### Expansion planning

No case yet; see [chile/expansion/README.md](chile/expansion/README.md).

## Cases by country

| Country | System | Data source | Daily scheduling | Medium/long term | Expansion |
|---|---|---|---:|---:|---:|
| [Chile](chile/README.md) | SEN | CEN (Coordinador Eléctrico Nacional) | 14 | 3 | — |
| [Guatemala](guatemala/README.md) | SNI | AMM (Administrador del Mercado Mayorista), EOR (Ente Operador Regional) | 2 | 6 SDDP + 6 snapshots | — |
| [Peru](peru/README.md) | SEIN | COES (Comité de Operación Económica del Sistema Interconectado Nacional) | — | 4 SDDP (not yet validated) | — |
| [Poland](poland/README.md) | Polish transmission system | MATPOWER `case3375wp` (data by R. Korab, Silesian University of Technology) | — | 1 DC OPF snapshot | — |


Each country README names the rights holders of its source data (Chile:
CEN; Guatemala: AMM and EOR; Peru: COES; Poland: R. Korab / MATPOWER).
All third-party data sources, their terms and the attribution to give are
listed in [`THIRD_PARTY_DATA.md`](THIRD_PARTY_DATA.md).  New countries
follow the same pattern.

## How to run

A case is a gtopt planning JSON plus the files it references (PAMPL, CSV,
solver parameter files), run **together with its application profile**
when it has one: the case file goes first and the profile second (its
options win).  Run from an output directory **outside** the repository
and point `input_directory` at the case, so nothing is written into the
checkout:

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)
C=$REPO/chile/daily_scheduling/pcp_2025-10-19/case
OUT=~/gtopt-cases-out/chile/daily_scheduling/pcp_2025-10-19
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pcp_2025-10-19.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$C" -d . --set solver_options.threads=8
```

Every case README has its exact command, the expected resources and how
to regenerate the case from `source/`; `catalog.json` → `run` holds the
same command per case.  Resource classes: **large** — the 14 Chilean
daily cases (MIPs of 0.8–1.3 M rows, 5–30 GB RAM), the Chilean and
Peruvian SDDP cases;
**medium** — the Guatemalan NCP and SDDP cases (~0.2 M rows); **small** — the
PSS®E snapshots (~1 k rows).

## Cloning

The repository holds input data only and is kept small.  A shallow clone
is enough to use the cases:

```bash
git clone --depth 1 https://github.com/gtopt-community/gtopt-cases.git
```

## Contributing data: size and hygiene rules

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to propose a case and the
data provenance and licence checklist.

`tools/check_repo.sh` runs in CI on every push and pull request (and,
after `git config core.hooksPath .githooks`, before each local commit).
It rejects:

- a `source/` file whose sha256 or size differs from `catalog.json`, or a
  tracked `source/` file missing from the catalog (`NOTICE.md` excepted);

- any file larger than 10 MB (compress with `xz -6`, or split the file
  into `<name>.<N>.xz` parts, which `tools/get_case.py` joins back);
- results, logs and caches (`results/`, `output/`, `logs/`, `*.log`,
  `*.sol`, `__pycache__`): the repository publishes inputs only;
- absolute home paths (`/home/...`, Windows user folders) in text files;
- a tracked tree larger than 400 MB.

When a case is updated, its files are replaced in place rather than added
as a new copy next to the old one.  Pull requests are squash-merged.

## Getting and rebuilding cases

This repository keeps a single, minimal script; all real tooling
(converters, the CEN downloader, checks and analysis) lives in gtopt and
is installed with its Python tools from a gtopt checkout:

```bash
pip install -e <gtopt checkout>/scripts      # plexos2gtopt, plp2gtopt, ...
```

| Command | Purpose |
|---|---|
| `tools/get_case.py pcp <date>` | CEN PCP day: download `DATOS`/`RES` (only if not local), convert with `plexos2gtopt` and the flags/line lifts of `catalog.json` |
| `tools/get_case.py plp <date>` | CEN PLP bundle in force on a date: download, compress into `source/`, convert with `plp2gtopt` |
| `tools/get_case.py rebuild <case>` | reconvert a catalogued case from its `source/` (`--out` to write elsewhere) |

`get_case.py` uses the Python standard library only and calls the gtopt
console scripts `cen2gtopt-pcp-archive`, `plexos2gtopt`, `plp2gtopt`,
`plp_compress_case`, `sddp2gtopt` and `psse2gtopt`.  Downloads not kept in
git (the PLEXOS solution bundle) go to `$GTOPT_CASES_CACHE` (default
`~/.cache/gtopt-cases`).  Install the gtopt tools editable (or from a
revision whose wheel ships their data files): without the converter data
files (CEN hard user constraints, emission factors, cogeneration list)
`plexos2gtopt` builds a different model.

Related gtopt tools:

| gtopt command | Purpose |
|---|---|
| `gtopt_check_cases --repo <this checkout>` | `gtopt --lp-only` on every case and compare rows/cols/nnz with the catalog (checks that your gtopt reads the inputs as intended); `--solve` runs the cases with output outside the repository |
| `plexos2gtopt-line-lifts <case.json> <output>` | rank the binding lines of a gtopt solution, to choose line lifts |
| `cen2gtopt-pcp-solution summary --res <RES bundle> --output <dir>` | summarise a PLEXOS solution bundle (for your own comparisons; keep the output outside the repository) |
| `cen2gtopt-pcp-archive plp-in-force <date>` | which CEN PLP input bundle is in force on a date |

Style of `tools/`: `ruff format tools && ruff check tools`.

## Provenance

* **Daily scheduling**: CEN PCP bundles `PLEXOS<YYYYMMDD>.zip` from the CEN
  "Programa de Operación" portal.  `source/` keeps the PLEXOS input
  (`DATOS*.zip.xz`).  The PLEXOS solution (`RES*.zip`) is a result and is
  not redistributed; it is needed only to rebuild a case (block layout) and
  is fetched from the CEN portal by `tools/get_case.py`.
* **Medium/long term**: CEN PLP input sets, kept in `source/` (xz) and
  converted with `plp2gtopt` from gtopt.
* **Guatemala**: AMM PSR NCP models and PSS®E study files, converted with
  `sddp2gtopt` / `psse2gtopt` in the gtopt repository; inputs kept in
  `source/` (xz).
* **Guatemala, long-term SDDP programmes**: AMM PSR SDDP databases
  (`Base_de_datos_Programacion_<years>_Definitiva.rar`, AMM programmes
  portal), converted with `sddp2gtopt`; converter inputs kept in `source/`
  (xz), archives not redistributed.
* **Peru**: COES PSR SDDP base cases (`DatosSDDP_CasoBase.zip`, Anexo D of
  the MRFO 2026-2029 study), converted with `sddp2gtopt`; converter inputs
  kept once in `source/` (xz), archive not redistributed.

* **Poland**: MATPOWER 8.1 `data/case3375wp.m` (data by R. Korab),
  kept unchanged in `source/` (xz) and converted with `pp2gtopt` (gtopt,
  `matpower` extra of the scripts).

* Every case was converted with the named tool (`plexos2gtopt`,
  `plp2gtopt`, `sddp2gtopt`, `psse2gtopt`, `pp2gtopt`) from gtopt; rebuild
  with gtopt master of November 2026 or later.
* The exact flags and file hashes of each case are in `catalog.json`.  Its
  `gtopt_revision` (and `converter_last_change`) fields record the gtopt
  development revision used for the conversion (pre-publication history;
  may not exist in the public repository); the same holds for the gtopt
  revisions quoted in the case READMEs.

The CEN portal only serves Chilean IP addresses; from abroad, download
through a relay/VPN in Chile or copy the files by hand (`DATOS*.zip.xz`
into the case `source/`, the solution bundle via `--res`).

## Licensing and data terms

This repository holds third-party data and a thin layer added by the gtopt
authors; they are under different terms.

- **`source/`**: third-party data, redistributed as published and
  unmodified except for xz compression and, for large files, splitting
  into numbered parts.  **No licence is granted** by this repository.
- **`case/`**: derived from that data by the gtopt conversion tools; the
  cases remain subject to the rights and terms of the publishers.
- **Rights holders**: Coordinador Eléctrico Nacional (CEN), Chile;
  Administrador del Mercado Mayorista (AMM), Guatemala; Ente Operador
  Regional (EOR), Central America; Comité de Operación Económica del
  Sistema Interconectado Nacional (COES), Peru; Roman Korab, Silesian
  University of Technology, whose data are distributed by MATPOWER.
  Sources, terms and the attribution to give:
  [`THIRD_PARTY_DATA.md`](THIRD_PARTY_DATA.md).
- **Conversion layer**: to the extent the gtopt authors hold any rights in
  what they add (the file layout, `profiles/`, line lifts, solver
  parameter files, `catalog.json`, the READMEs, `NOTICE.md` files and
  other documentation and metadata), they dedicate those rights to the
  public domain under **CC0-1.0**
  ([`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt)).  This dedication
  grants no right in the third-party data.
- **Tools** (`tools/`, `.githooks/`): the gtopt licence,
  AGPL-3.0-or-later with the GTOpt Solver Plugin Exception, or the GTOpt
  Commercial License.

This statement is not legal advice.  Everything is provided **AS IS**,
without warranty of any kind; see [`DISCLAIMER.md`](DISCLAIMER.md).

## Removal requests

If you are a rights holder and object to the redistribution of any
material here, e-mail <marcelomatusacuna@gmail.com> with the subject
**"gtopt-cases removal request"**; for non-confidential requests you may
instead open an issue with the
[data removal form](https://github.com/gtopt-community/gtopt-cases/issues/new?template=data-removal.yml).
We acknowledge each request within 5 working days and remove the material
from `main` promptly.  When required, we also rewrite the git history and
ask GitHub Support to purge cached views; the maintainers bypass the
main-branch protection ruleset only for that purpose.
