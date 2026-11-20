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

| | `sem_2025w03` | `sem_2025w16` | `sem_2025w29` | `sem_2025w42` |
|---|---|---|---|---|
| Season | winter | spring | summer | autumn |
| Horizon (2025, 168 hourly blocks) | 13-19 January | 14-20 April | 14-20 July | 13-19 October |
| Network | 3 nodes (SEM, Great Britain, France); 2 HVDC links SEM-GB (East-West, Moyle) | 3 nodes; 3 HVDC links SEM-GB (East-West, Moyle, Greenlink) | same as w16 | same as w16 |
| Units | 116 generators, 61 with unit commitment | 116, 58 with UC | 116, 65 with UC | 116, 69 with UC |
| Storage | 22 grid batteries + Turlough Hill | 23 + Turlough Hill | 23 + Turlough Hill | 24 + Turlough Hill |
| Hydro | daily energy limits for Ardnacrusha, Erne, Lee and Liffey | same | same | same |
| Size (rows / binaries) | ~102k / 10.2k | ~101k / 9.7k | ~106k / 10.9k | ~113k / 11.6k |

Unit commitment covers min up/down times, start costs and ramps; each
week is a small MIP that runs in minutes at a 0.1 % gap.

Great Britain and France enter as single nodes with price-bid
generators, as in PLEXOS.  The case README lists what is and is not
converted.

These figures describe the cases that `tools/get_case.py fetch` builds;
the data themselves are not in this repository (see below).

| Application | Folder | Source | Converter |
|---|---|---|---|
| Unit commitment (weekly), winter | [unit_commitment/sem_2025w03](unit_commitment/sem_2025w03/README.md) | SEM-25-010 PLEXOS model, 13-19 January 2025, weather sample 1 | `plexos2gtopt --plexos-model` (gtopt 1.1.0 or later) |
| Unit commitment (weekly), spring | [unit_commitment/sem_2025w16](unit_commitment/sem_2025w16/README.md) | same model: 14-20 April 2025 | same |
| Unit commitment (weekly), summer | [unit_commitment/sem_2025w29](unit_commitment/sem_2025w29/README.md) | same model: 14-20 July 2025 | same |
| Unit commitment (weekly), autumn | [unit_commitment/sem_2025w42](unit_commitment/sem_2025w42/README.md) | same model: 13-19 October 2025 | same |

## Getting the data

The SEM data are **not redistributed** here: this folder is a recipe.
`tools/get_case.py fetch sem_2025w03` (or `sem_2025w16`, `sem_2025w29`,
`sem_2025w42`) downloads the public archives from
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
