# gtopt-cases

**Real power-system cases, ready to run with
[gtopt](https://github.com/gtopt-community/gtopt).**  From a one-hour DC
OPF to a 23-year hydrothermal SDDP and the transmission planning bases of
the Chilean system operator, built from data published by system operators
and research groups, plus standard benchmark systems.  Needs gtopt
**1.1.0 or later**
([releases](https://github.com/gtopt-community/gtopt/releases)).

> [!WARNING]
> The cases are provided **AS IS**, without warranty of any kind.  They
> were built with gtopt's own converters and checked only as far as the
> gtopt authors can; they are **not validated by the institutions that
> published the data**, and they must not be used as a reference for
> official operation, planning or financial analysis.  All rights to the
> source data remain with their publishers (AEMO, CEN, AMM, EOR, COES,
> the SEM Committee, R. Korab / MATPOWER, and the authors of the benchmark
> data); no licence over that data is granted here beyond the open
> licences under which some benchmark data are published.  Read the [disclaimer](DISCLAIMER.md) and
> [licensing](LICENSING.md) before using any case.

## Contents

- **[Real systems](#countries)** from six countries (Australia, Chile,
  Guatemala, Ireland, Peru, Poland): unit commitment and dispatch,
  hydrothermal SDDP, transmission planning bases and DC OPF, built from
  data published by system operators and regulators.
- **[Benchmark cases](#benchmark-cases)**: standard test systems (IEEE /
  PGLib-OPF), example systems of other tools (UnitCommitment.jl, NREL
  Sienna, NREL-118) and published case studies (clustered unit
  commitment, IEEE 39 and 118 buses), to compare gtopt with other
  models.

## Countries

Six countries so far, each in its own folder with a README that
describes the power system, the publisher of the data and the cases.
The table below lists, for each country, the system and the institution
whose published data the cases are built from, and what the cases are:
daily or weekly unit commitment and dispatch, hydrothermal SDDP over
one to 23 years, transmission planning bases and a DC optimal power
flow.

| Country | System · data from | Cases |
|---|---|---|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [**Australia**](australia/README.md) | NEM · AEMO | 4 weekly dispatches, one per season of 2027 (PLEXOS ISP 2026, Step Change) |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [**Chile**](chile/README.md) | SEN · CEN | 14 daily operation programmes, each scheduling one week: unit commitment (PLEXOS)<br>14 more PCP days as source only (4 bundles here, 10 fetched on demand)<br>3 SDDP of 2, 5 and 23 years (PLP), with the Laja and Maule irrigation agreements<br>3 SDDP of the PLP-PET27 transmission planning process (PLP) |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [**Guatemala**](guatemala/README.md) | SNI · AMM, EOR | 2 daily/weekly dispatches (NCP)<br>6 annual SDDP programmes · 6 PSS®E snapshots |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [**Ireland**](ireland/README.md) | SEM · SEM Committee (CRU, UR) | 4 weekly unit commitments, one per season of 2025 (PLEXOS), 116 units, 58–69 with commitment; recipe only, fetched and converted on demand |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [**Peru**](peru/README.md) | SEIN · COES | 4 annual SDDP cases (2026-2029 reserve-margin study) |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [**Poland**](poland/README.md) | Polish grid · R. Korab / MATPOWER | 1 DC OPF of 3,374 buses |

### Model size

How large the systems are, counted as gtopt elements in the converted
cases: buses and lines of the network, generators (thermal, hydro,
wind, solar and, where the source models them, neighbouring markets as
price bids), demands, hydro reservoirs and batteries (including pumped
storage modelled as a battery).  The horizon is the period each case
simulates: one hour for the OPF and network snapshots, one week for
unit commitment and dispatch, and one to 23 years for the SDDP cases.
The Chilean `plp_2y` case is two years plus end-of-horizon fill stages.
`plp_23y` and the PET 2027 bases are 23-year horizons (276 monthly
stages, all in `source/`); to keep the repository small their committed
`case/` holds only the first year, and each case README gives the
`plp2gtopt` command that builds the full 23 years on your machine (drop
`-s 12`, e.g. `plp2gtopt -i source -o <out> -y 1 -a 0 --method sddp`).
Where a country has several cases the
table gives the range.  The Ireland figures describe the cases that
`tools/get_case.py fetch` builds locally, since its data are not
redistributed here.

| Country | Horizon | Buses | Lines | Generators | Demands | Reservoirs | Batteries |
|---|---|---:|---:|---:|---:|---:|---:|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [Australia](australia/README.md) | 1 week (hourly) · 4 years (1 day per month) | 15 | 18 | 523–765 | 15–32 | 22 | 85–223 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [Chile](chile/README.md) | 1 week · 2 years (+ fill) · 4.5 years · 23 years | 237–339 | 305–449 | 933–1,892 | 127–161 | 10–12 | 0–202 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [Guatemala](guatemala/README.md) | 1 hour · 1 week · 1 year | 461–877 | 519–955 | 75–230 | 116–261 | 0–44 | — |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [Ireland](ireland/README.md) | 1 week (hourly) | 3 | 2–3 | 116 | 3 | — | 23–25 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [Peru](peru/README.md) | 1 year | 270 | 312–394 | 157–163 | 133–135 | 60 | — |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [Poland](poland/README.md) | 1 hour | 3,374 | 4,161 | 489 | 2,414 | — | — |

Per-case detail (demands, turbines,
water rights, unit commitments, blocks, scenarios, LP size) is in the
[case index](docs/cases.md) and [`catalog.json`](catalog.json).

## Benchmark cases

Standard test systems, example systems of other tools and published case
studies, in [`benchmarks/`](benchmarks/README.md), grouped by family.
Where the source has an open licence its files are kept with the case;
otherwise the folder holds a recipe that `tools/get_case.py fetch`
downloads (pinned commit, sha256-checked) and converts on your machine.

| Family | Cases | Source · licence | In this repository |
|---|---|---|---|
| [**IEEE**](benchmarks/ieee/README.md) | 9 single-hour DC OPF, 5 to 300 buses (PJM 5, IEEE 14, 30, 57, 118, 300, RTS-79, RTS-96, New England 39) | PGLib-OPF v23.07 · CC BY 4.0 | source + case |
| [**UnitCommitment.jl**](benchmarks/unitcommitment_jl/README.md) | 3 unit-commitment MIPs (IEEE 14 and 118 buses) | UnitCommitment.jl fixtures · BSD-3-Clause | source + case |
| [**NREL**](benchmarks/nrel/README.md) | NREL-118, one week hourly | Sienna PowerSystemsTestData · no licence | recipe only |
| [**Sienna**](benchmarks/sienna/README.md) | 7 small PowerSimulations.jl test systems (PJM 5-bus) | Sienna PowerSystemsTestData · no licence | recipe only |
| [**Papers**](benchmarks/papers/README.md) | Morales-España and Tejada-Arango (2019), clustered UC: IEEE 39 and 118 buses | CUC-data · no licence | recipe only |

## What each case contains

```
<country>/<application>/<case>/     (benchmarks: benchmarks/<family>/<case>/)
├── README.md   what it is, how to run it, how to rebuild it
├── source/     the data exactly as published (xz-compressed)
└── case/       the gtopt case built from it
```

Inputs only: no gtopt results, logs or solutions.  Run the cases and
compare on your own.  A few case READMEs show figures the publisher itself
released (e.g. CEN's PET 2027 diagnosis), with their source, as context.

Where the data may not be redistributed (Ireland, the benchmark sources
without a licence), or a public file is
left out to keep the repository small (ten Chilean PCP days), the case
folder holds only a recipe: `tools/get_case.py fetch <case>` downloads the
files from the publisher, checks their hashes and converts them on your
machine.

## Quick start

```bash
git clone --depth 1 https://github.com/gtopt-community/gtopt-cases.git
cd gtopt-cases/poland/dc_opf/case3375wp   # small: runs in a moment
cat README.md                             # the exact gtopt command to run it
```

## Releases

The current release is
[**1.0.0**](https://github.com/gtopt-community/gtopt-cases/releases/tag/v1.0.0)
(2026-11-20), the first public release.  It brings 41 cases from six
countries and needs gtopt **1.1.0 or later**:

- 🇦🇺 **Australia**: 1 weekly dispatch of the NEM (AEMO ISP 2026, Step Change);
- 🇨🇱 **Chile**: 14 weekly unit commitments from the CEN daily operation
  programmes, 3 SDDP cases of 2, 5 and 23 years with the Laja and Maule
  irrigation agreements, and 3 SDDP bases of the PET 2027 transmission
  planning process;
- 🇬🇹 **Guatemala**: 2 daily/weekly dispatches, 6 annual SDDP programmes
  and 6 PSS®E network snapshots;
- 🇮🇪 **Ireland**: 1 weekly unit commitment of the SEM (recipe only);
- 🇵🇪 **Peru**: 4 annual SDDP cases of the COES 2026-2029 reserve-margin study;
- 🇵🇱 **Poland**: 1 DC OPF of 3,374 buses.

Plus `catalog.json` with provenance and model size for every case, the
[case index](docs/cases.md) and `tools/get_case.py` to download and
rebuild cases.  Changes between releases are in the
[changelog](CHANGELOG.md).

## Documentation

- 📋 [**Case index**](docs/cases.md): all cases by application and country, sizes and resources
- ▶️ [**Running a case**](docs/running.md): command line, profiles, output outside the repository
- 🔧 [**Getting and rebuilding cases**](docs/tools.md): `tools/get_case.py` and the gtopt converters
- 🧾 [**Provenance**](docs/provenance.md): where each dataset comes from and how it was converted
- ⚖️ [**Licensing**](LICENSING.md): rights, attribution, removal requests
- 🤝 [**Contributing**](CONTRIBUTING.md): propose a case, data checklist, size rules

## Community

Questions, results and new data:
[gtopt Discussions](https://github.com/gtopt-community/gtopt/discussions).
Have public data for another system?  Open an issue with the
[new-case form](https://github.com/gtopt-community/gtopt-cases/issues/new?template=new-case.yml).
