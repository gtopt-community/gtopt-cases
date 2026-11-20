# gtopt-cases

**Real power-system cases, ready to run with
[gtopt](https://github.com/gtopt-community/gtopt).**  From a one-hour DC
OPF to a 23-year hydrothermal SDDP and the transmission planning bases of
the Chilean system operator, built from data published by system operators
and research groups.  Needs gtopt **1.1.0 or later**
([releases](https://github.com/gtopt-community/gtopt/releases)).

> [!WARNING]
> The cases are provided **AS IS**, without warranty of any kind.  They
> were built with gtopt's own converters and checked only as far as the
> gtopt authors can; they are **not validated by the institutions that
> published the data**, and they must not be used as a reference for
> official operation, planning or financial analysis.  All rights to the
> source data remain with their publishers (AEMO, CEN, AMM, EOR, COES,
> the SEM Committee, R. Korab / MATPOWER); no licence over that data is
> granted here.  Read the [disclaimer](DISCLAIMER.md) and
> [licensing](LICENSING.md) before using any case.

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
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [**Australia**](australia/README.md) | NEM · AEMO | 1 weekly dispatch (PLEXOS ISP 2026, Step Change) |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [**Chile**](chile/README.md) | SEN · CEN | 14 daily operation programmes, each scheduling one week: unit commitment (PLEXOS)<br>3 SDDP of 2, 5 and 23 years (PLP), with the Laja and Maule irrigation agreements<br>3 SDDP of the PLP-PET27 transmission planning process (PLP) |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [**Guatemala**](guatemala/README.md) | SNI · AMM, EOR | 2 daily/weekly dispatches (NCP)<br>6 annual SDDP programmes · 6 PSS®E snapshots |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [**Ireland**](ireland/README.md) | SEM · SEM Committee (CRU, UR) | 1 weekly unit commitment (PLEXOS), 116 units, 61 with commitment; recipe only, fetched and converted on demand |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [**Peru**](peru/README.md) | SEIN · COES | 4 annual SDDP cases (2026-2029 reserve-margin study) |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [**Poland**](poland/README.md) | Polish grid · R. Korab / MATPOWER | 1 DC OPF of 3,374 buses |

### Model size

How large the systems are, counted as gtopt elements in the converted
cases: buses and lines of the network, generators (thermal, hydro,
wind, solar and, where the source models them, neighbouring markets as
price bids), demands, hydro reservoirs and batteries (including pumped
storage modelled as a battery).  The horizon is the period each case
simulates: one hour for the OPF and network snapshots, one week for
unit commitment and dispatch, one to 4.5 years for the SDDP cases (the
23-year Chilean PLP and the PET 2027 bases are converted for their
first year).  Where a country has several cases the
table gives the range.  The Ireland figures describe the case that
`tools/get_case.py fetch` builds locally, since its data are not
redistributed here.

| Country | Horizon | Buses | Lines | Generators | Demands | Reservoirs | Batteries |
|---|---|---:|---:|---:|---:|---:|---:|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [Australia](australia/README.md) | 1 week (hourly) | 15 | 18 | 523 | 15 | 22 | 85 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [Chile](chile/README.md) | 1 week · 1 year · 2.9 years · 4.5 years | 237–339 | 305–449 | 933–1,892 | 127–161 | 10–12 | 0–202 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [Guatemala](guatemala/README.md) | 1 hour · 1 week · 1 year | 461–877 | 519–955 | 75–230 | 116–261 | 0–44 | — |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [Ireland](ireland/README.md) | 1 week (hourly) | 3 | 2 | 116 | 3 | — | 23 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [Peru](peru/README.md) | 1 year | 270 | 312–394 | 157–163 | 133–135 | 60 | — |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [Poland](poland/README.md) | 1 hour | 3,374 | 4,161 | 489 | 2,414 | — | — |

Per-case detail (demands, turbines,
water rights, unit commitments, blocks, scenarios, LP size) is in the
[case index](docs/cases.md) and [`catalog.json`](catalog.json).

## What each case contains

```
<country>/<application>/<case>/
├── README.md   what it is, how to run it, how to rebuild it
├── source/     the data exactly as published (xz-compressed)
└── case/       the gtopt case built from it
```

Inputs only: no gtopt results, logs or solutions.  Run the cases and
compare on your own.  A few case READMEs show figures the publisher itself
released (e.g. CEN's PET 2027 diagnosis), with their source, as context.

Where the data may not be redistributed (Ireland), the case folder holds
only a recipe: `tools/get_case.py fetch <case>` downloads the files from the
publisher, checks their hashes and converts them on your machine.

## Quick start

```bash
git clone --depth 1 https://github.com/gtopt-community/gtopt-cases.git
cd gtopt-cases/poland/dc_opf/case3375wp   # small: runs in a moment
cat README.md                             # the exact gtopt command to run it
```

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
