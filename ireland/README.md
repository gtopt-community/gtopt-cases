# <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> Ireland — Single Electricity Market (SEM)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the all-island Single Electricity Market (Ireland and Northern
Ireland) built from the public **SEM PLEXOS Forecast Model 2024-2032**
published by the **SEM Committee** (CRU and Utility Regulator).

## The system

The Single Electricity Market is the wholesale electricity market of the
island of Ireland: one market, one price zone and one dispatch for the
Republic of Ireland and Northern Ireland, regulated jointly by the CRU
and the Utility Regulator through the SEM Committee and operated by
EirGrid and SONI.  It is a small island system with a high share of wind: thermal
gas units, a large and growing fleet of wind farms and grid batteries,
a few run-of-river hydro plants and one pumped-storage station
(Turlough Hill), with HVDC links to Great Britain (East-West and Moyle)
and a link to France (Celtic) under construction.

## The model

The SEM PLEXOS Forecast Model 2024-2032 is the market model the
regulators use to validate and forecast SEM outcomes (SEM-25-010,
March 2025), prepared by NERA Economic Consulting and published in a
public version with its demand, wind and solar data files.  gtopt reads
the PLEXOS XML directly (`plexos2gtopt --plexos-model`), resolves one
week of one weather sample, and builds an hourly mixed-integer
unit-commitment problem:

| | `sem_2025w03` |
|---|---|
| Horizon | 13-19 January 2025, 168 hourly blocks |
| Network | 3 nodes (SEM, Great Britain, France), 2 HVDC interconnectors |
| Units | 116 generators, 61 with unit commitment (min up/down, start costs, ramps) |
| Storage | 22 grid batteries + Turlough Hill pumped storage |
| Hydro | daily energy limits for Ardnacrusha, Erne, Lee and Liffey |
| Size | ~102k rows, ~89k columns, ~10k binaries: small, runs in minutes |

Great Britain and France enter as single nodes with price-bid
generators, as in PLEXOS.  The case README lists what is and is not
converted.

These figures describe the case that `tools/get_case.py fetch` builds;
the data themselves are not in this repository (see below).

| Application | Folder | Source | Converter |
|---|---|---|---|
| Unit commitment (weekly) | [unit_commitment/sem_2025w03](unit_commitment/sem_2025w03/README.md) | SEM-25-010 PLEXOS model, 13-19 January 2025, weather sample 1 | `plexos2gtopt --plexos-model` (gtopt 1.1.0 or later) |

## Getting the data

The SEM data are **not redistributed** here: this folder is a recipe.
`tools/get_case.py fetch sem_2025w03` downloads the public archives from
the SEM Committee site, checks their sha256 and converts them locally
(see the case README).

## Provenance and rights

* **Rights holders: the SEM Committee (Commission for Regulation of
  Utilities, Ireland, and Utility Regulator, Northern Ireland)**; the
  model was prepared by NERA Economic Consulting.
* **No licence stated**: redistribution needs the publishers' written
  permission (CRU, <info@cru.ie>), so neither the data nor converted cases
  are kept in this repository.  See
  [`../THIRD_PARTY_DATA.md`](../THIRD_PARTY_DATA.md).
* Archive URLs, sha256, converter flags and gtopt revision:
  [`catalog.json`](../catalog.json).
