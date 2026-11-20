# <img src="https://flagcdn.com/w40/pe.png" width="28" align="absmiddle" alt="🇵🇪"> Peru — Sistema Eléctrico Interconectado Nacional (SEIN)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the Peruvian power system built from data published by the
**[COES](https://www.coes.org.pe)** (*Comité de Operación Económica del
Sistema Interconectado Nacional*), the system operator.

| Application | Folder | COES source | Converter |
|---|---|---|---|
| Daily scheduling | — | — | — |
| Medium / long term | [medium_long_term/](medium_long_term/README.md) | PSR SDDP base cases 2026–2029 of the *Estudio de Verificación del Margen de Reserva Firme Objetivo 2026-2029* (Anexo D) | `sddp2gtopt` |
| Expansion | — | — | — |

## Provenance and rights

* **Rights holder: COES.**  All rights to the original models and data
  belong to their authors and/or the COES; this repository claims no
  ownership of them (see [DISCLAIMER.md](../DISCLAIMER.md)).
  * COES: <https://www.coes.org.pe> — MRFO 2026-2029 study, Anexo D:
    [`DatosSDDP_CasoBase.zip`](https://www.coes.org.pe/portal/browser/download?url=Planificaci%C3%B3n%2FEstudios%20de%20Verificacion%20del%20Margen%20de%20Reserva%20Firme%2FMRFO_2026-2029%2FAnexos%2FANEXO%20D%2FDatosSDDP_CasoBase.zip).
* The converter inputs are kept xz-compressed in `source/`; the original
  zip is not redistributed.  Converter, gtopt revision and file hashes per
  case: [`catalog.json`](../catalog.json).

## Data terms

All input data are derived from public COES publications.  The COES keeps
the rights on the original data; check its terms of use before
redistributing them, and cite the COES as the source.  Only model inputs
are published here; PSR results are not redistributed.
