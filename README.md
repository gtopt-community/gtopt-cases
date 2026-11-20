# gtopt-cases

**Real power-system cases, ready to run with
[gtopt](https://github.com/gtopt-community/gtopt).**  From a one-hour DC
OPF to a 23-year hydrothermal SDDP, built from data published by system
operators and research groups.

> [!WARNING]
> Provided **AS IS**, not validated by the institutions that published
> the data, which keep all rights over it.  See the
> [disclaimer](DISCLAIMER.md) and [licensing](LICENSING.md).

## Countries

| | Country | System | Data from | Cases |
|:-:|---|---|---|---|
| <img src="https://flagcdn.com/w20/cl.png" width="20" alt="Chile"> | [**Chile**](chile/README.md) | SEN | CEN | 14 daily unit commitments (PLEXOS) · 3 SDDP of 2, 5 and 23 years (PLP), with the Laja and Maule irrigation agreements |
| <img src="https://flagcdn.com/w20/gt.png" width="20" alt="Guatemala"> | [**Guatemala**](guatemala/README.md) | SNI | AMM, EOR | 2 daily/weekly dispatches (NCP) · 6 annual SDDP programmes · 6 PSS®E network snapshots |
| <img src="https://flagcdn.com/w20/pe.png" width="20" alt="Peru"> | [**Peru**](peru/README.md) | SEIN | COES | 4 annual SDDP cases of the 2026-2029 reserve-margin study |
| <img src="https://flagcdn.com/w20/pl.png" width="20" alt="Poland"> | [**Poland**](poland/README.md) | Polish transmission system | R. Korab / MATPOWER | 1 DC OPF of 3,374 buses |

### Model size

| | Country | Buses | Lines | Generators | Demands | Reservoirs | Batteries |
|:-:|---|---:|---:|---:|---:|---:|---:|
| <img src="https://flagcdn.com/w20/cl.png" width="20" alt="Chile"> | [Chile](chile/README.md) | 237–339 | 305–449 | 1,628–1,892 | 127–161 | 10–12 | 0–112 |
| <img src="https://flagcdn.com/w20/gt.png" width="20" alt="Guatemala"> | [Guatemala](guatemala/README.md) | 461–877 | 519–955 | 75–230 | 116–261 | 0–44 | — |
| <img src="https://flagcdn.com/w20/pe.png" width="20" alt="Peru"> | [Peru](peru/README.md) | 270 | 312–394 | 157–163 | 133–135 | 60 | — |
| <img src="https://flagcdn.com/w20/pl.png" width="20" alt="Poland"> | [Poland](poland/README.md) | 3,374 | 4,161 | 489 | 2,414 | — | — |

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

Inputs only: no objective values, prices, logs or operator solutions.
Run the cases and compare on your own.

## Quick start

```bash
git clone --depth 1 https://github.com/gtopt-community/gtopt-cases.git
cd gtopt-cases/poland/dc_opf/case3375wp   # small: runs in a moment
cat README.md                             # the exact gtopt command
```

## Documentation

| Page | |
|---|---|
| 📋 [Case index](docs/cases.md) | all cases by application and country, sizes and resources |
| ▶️ [Running a case](docs/running.md) | command line, profiles, output outside the repository |
| 🔧 [Getting and rebuilding cases](docs/tools.md) | `tools/get_case.py` and the gtopt converters |
| 🧾 [Provenance](docs/provenance.md) | where each dataset comes from and how it was converted |
| ⚖️ [Licensing](LICENSING.md) | rights, attribution, removal requests |
| 🤝 [Contributing](CONTRIBUTING.md) | propose a case, data checklist, size rules |

## Community

Questions, results and new data:
[gtopt Discussions](https://github.com/gtopt-community/gtopt/discussions).
Have public data for another system?  Open an issue with the
[new-case form](https://github.com/gtopt-community/gtopt-cases/issues/new?template=new-case.yml).
