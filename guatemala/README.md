# <img src="https://flagcdn.com/w20/gt.png" width="20" alt="Guatemala"> Guatemala — Sistema Nacional Interconectado (SNI)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the Guatemalan power system built from models and data published
by the **AMM** (*Administrador del Mercado Mayorista*, the system and market
operator) and the **EOR** (*Ente Operador Regional*, the Central American
regional operator).  They were converted with `sddp2gtopt` and
`psse2gtopt` from gtopt; rebuild with gtopt master of November 2026 or
later.  The long-term SDDP programmes (`medium_long_term/sddp_plp_*`)
were converted from the AMM databases published at
<https://www.amm.org.gt/pdfs2/programas_despacho/03_PROGRAMAS_DE_LARGO_PLAZO/>.

| Application | Folder | Source model | Converter |
|---|---|---|---|
| Daily scheduling | [daily_scheduling/](daily_scheduling/README.md) | PSR NCP daily program (PDD 22-Jun-2026) and weekly NCP dispatch (21–27 Jun 2026) | `sddp2gtopt` |
| Medium / long term | [medium_long_term/](medium_long_term/README.md) | PSR SDDP long-term programmes 2021-2022 … 2026-2027; PSS®E network snapshots of the AMM long-term study May-2026–Apr-2027 | `sddp2gtopt`, `psse2gtopt` |
| Expansion | — | — | — |

## Provenance and rights

* **Rights holders: Administrador del Mercado Mayorista (AMM) and Ente
  Operador Regional (EOR).**  All rights to the original models and data
  (PSR NCP and SDDP models, PSS®E study files) belong to their
  authors and/or the AMM and the EOR; this repository claims no ownership
  of them (see [DISCLAIMER.md](../DISCLAIMER.md)).
  * AMM (Administrador del Mercado Mayorista): <https://www.amm.org.gt> —
    planning publications
    <https://www.amm.org.gt/ultpub/ultimas_pub_plani.php>, results
    publications <https://www.amm.org.gt/ultpub/ultimas_pub_resul.php>.
  * EOR (Ente Operador Regional, MER): <https://www.enteoperador.org> —
    maximum transfers
    <https://www.enteoperador.org/mer/gestion-comercial/maximas-transferencias/>,
    transfer-capacity study
    <https://www.enteoperador.org/mer/gestion-tecnica-operativa/estudio-de-maximas-capacidades-de-transferencias-de-potencia/>.
* The converter inputs are kept xz-compressed in each case's `source/`
  (`.dat`/`.csv` of the PSR models, PSS®E `.raw` and AMM spreadsheets), so
  every case can be regenerated without the original archives.  The
  original AMM archives (`.rar`, `.7z`) are not redistributed.
* Converter, gtopt revision and file hashes per case: `catalog.json`.
* The cases are self-contained (no application profile).  Each case
  README has a **How to run** section (exact command, expected resources;
  results go to `~/gtopt-cases-out/<case id>`, outside the repository).
  They were tested with a gtopt build that includes the FutureCost element
  (`system.future_cost_array`), which `ncp_pdd_2026-06-22` requires.

## Data terms

The data derive from public publications of the AMM and the EOR, which keep
the rights on the original data; check their terms of use before
redistributing them.  Only model inputs are published here; operator
results (prices, dispatches, studies) are not redistributed.
