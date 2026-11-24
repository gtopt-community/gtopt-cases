# NREL test systems

> [!WARNING]
> Provided **AS IS**, not validated by the data authors, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

NREL test systems.  The NREL-118 data are taken from Sienna's
`PowerSystemsTestData`, which has no licence, so the case is a recipe:
`tools/get_case.py fetch` downloads and converts it locally.

| Case | What | Network | Application | In this repository |
|---|---|---|---|---|
| [nrel118_2024w01](nrel118_2024w01/README.md) | NREL-118 extended IEEE 118-bus system, first week (hourly) | 118 buses | production_cost | recipe only |

Licence, citation and the exact converter command of each case are in its
README; machine-readable provenance is in [`catalog.json`](../../catalog.json).
