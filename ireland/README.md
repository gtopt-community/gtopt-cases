# <img src="https://flagcdn.com/w40/ie.png" width="28" align="absmiddle" alt="🇮🇪"> Ireland — Single Electricity Market (SEM)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the all-island Single Electricity Market (Ireland and Northern
Ireland) built from the public **SEM PLEXOS Forecast Model 2024-2032**
published by the **SEM Committee** (CRU and Utility Regulator).

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
