# gtopt-cases

**Real power-system cases, ready to run with
[gtopt](https://github.com/gtopt-community/gtopt).**  From a one-hour DC
OPF to a 23-year hydrothermal SDDP and the transmission planning bases of
the Chilean system operator, built from data published by system operators
and research groups.  Needs gtopt **1.1.0 or later**
([releases](https://github.com/gtopt-community/gtopt/releases)).

> [!WARNING]
> Provided **AS IS**; the data publishers keep all rights.
> See the [disclaimer](DISCLAIMER.md) and [licensing](LICENSING.md).

## Countries

| Country | System · data from | Cases |
|---|---|---|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [**Australia**](australia/README.md) | NEM · AEMO | 1 weekly dispatch (PLEXOS ISP 2026, Step Change) |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [**Chile**](chile/README.md) | SEN · CEN | 14 daily unit commitments (PLEXOS)<br>3 SDDP of 2, 5 and 23 years (PLP), with the Laja and Maule irrigation agreements<br>3 SDDP of the PLP-PET27 transmission planning process (PLP) |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [**Guatemala**](guatemala/README.md) | SNI · AMM, EOR | 2 daily/weekly dispatches (NCP)<br>6 annual SDDP programmes · 6 PSS®E snapshots |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [**Ireland**](ireland/README.md) | SEM · SEM Committee (CRU, UR) | 1 weekly unit commitment (PLEXOS), fetched and converted on demand |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [**Peru**](peru/README.md) | SEIN · COES | 4 annual SDDP cases (2026-2029 reserve-margin study) |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [**Poland**](poland/README.md) | Polish grid · R. Korab / MATPOWER | 1 DC OPF of 3,374 buses |

### Model size

| Country | Buses | Lines | Generators | Demands | Reservoirs | Batteries |
|---|---:|---:|---:|---:|---:|---:|
| <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> [Australia](australia/README.md) | 15 | 18 | 523 | 15 | 22 | 85 |
| <img src="https://flagcdn.com/w40/cl.png" width="28" align="absmiddle" alt="🇨🇱"> [Chile](chile/README.md) | 237–339 | 305–449 | 933–1,892 | 127–161 | 10–12 | 0–202 |
| <img src="https://flagcdn.com/w40/gt.png" width="28" align="absmiddle" alt="🇬🇹"> [Guatemala](guatemala/README.md) | 461–877 | 519–955 | 75–230 | 116–261 | 0–44 | — |
| <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> [Ireland](ireland/README.md) | 3 | 2 | 116 | 3 | — | 23 |
| <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> [Peru](peru/README.md) | 270 | 312–394 | 157–163 | 133–135 | 60 | — |
| <img src="https://flagcdn.com/w40/pl.png" width="28" align="absmiddle" alt="🇵🇱"> [Poland](poland/README.md) | 3,374 | 4,161 | 489 | 2,414 | — | — |

Ranges over each country's cases.  Per-case detail (demands, turbines,
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
