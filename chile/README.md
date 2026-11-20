# <img src="https://flagcdn.com/w20/cl.png" width="20" alt="Chile"> Chile — Sistema Eléctrico Nacional (SEN)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the Chilean national power system built from data published by
the **[Coordinador Eléctrico Nacional (CEN)](https://www.coordinador.cl)**, the independent system
operator.

| Application | Folder | CEN source | Converter |
|---|---|---|---|
| Daily scheduling | [daily_scheduling/](daily_scheduling/README.md) | CEN daily operation programme (PCP), daily PLEXOS model | `plexos2gtopt` |
| Medium / long term | [medium_long_term/](medium_long_term/README.md) (`plp_2y`, `plp_5y`, `plp_23y`) | PLP — *Programa de Largo Plazo*, hydrothermal SDDP | `plp2gtopt` |
| Expansion | [expansion/](expansion/README.md) | — | — |

## Getting the data

The CEN publishes the PCP and PLP model bases on its "Programa de
Operación" portal (`programa.coordinador.cl`).  `tools/get_case.py pcp
<date>` and `tools/get_case.py plp <date>` download them with the gtopt
fetcher `cen2gtopt-pcp-archive` and convert them.  **The portal's download
bucket only serves Chilean IP addresses**: from abroad, use a relay/VPN in
Chile, or copy the files by hand (PCP: `DATOS<date>.zip.xz` into the case
`source/` and pass the solution bundle with `--res`).

## Provenance and rights

* **Rights holder: Coordinador Eléctrico Nacional (CEN).**  All rights to
  the original models and data (PCP PLEXOS bundles, PLP data) belong to
  their authors and/or the CEN; this repository claims no ownership of
  them (see [DISCLAIMER.md](../DISCLAIMER.md)).
  * CEN: <https://www.coordinador.cl> — PCP model bases (PLEXOS) on the
    "Programa de Operación" portal
    <https://programa.coordinador.cl/operacion/pcp/bases-modelo>.
* Converter, gtopt revision, flags and file hashes per case:
  [`catalog.json`](../catalog.json).

## Data terms

All input data are derived from public CEN publications.  The CEN keeps
the rights on the original data; check its terms of use before
redistributing them.  Only inputs are published here: PLEXOS solution
databases (`RES*.zip`) and any other result are not redistributed (they
remain available from the CEN portal).
