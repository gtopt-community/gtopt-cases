# Third-party data

Every case in this repository is derived from data published by third
parties.  This file lists **all** data sources, their licence or terms of
use, and the attribution to give.  It complements
[`LICENSING.md`](LICENSING.md) (the gtopt tools are AGPL-3.0-or-later +
GTOpt Solver Plugin Exception, or the GTOpt Commercial License, and the
gtopt-authored conversion layer is CC0-1.0; **neither extends to the case
data**) and
[`DISCLAIMER.md`](DISCLAIMER.md) (all cases are provided AS IS, not
validated by the publishers, and must never be used as a reference for
official operation analysis or financial analysis).

All rights to the original data belong to their authors and/or the
publishing institutions.  `source/` holds the data unmodified except for
xz compression and splitting into parts; `case/` holds gtopt conversions
derived from it, which remain subject to the publishers' rights; no
licence is granted over either.  The conversion layer added by the gtopt
authors is CC0-1.0, without granting any right in the third-party data.
The full rights statement is in [`LICENSING.md`](LICENSING.md); per-case
terms are in each `source/NOTICE.md`, `case/NOTICE.md` and the `terms`
object of [`catalog.json`](catalog.json).  This is not legal advice.

**Removal requests**: e-mail <marcelomatusacuna@gmail.com> with the
subject "gtopt-cases removal request" (or, for non-confidential requests,
open an issue with the data removal form).  We acknowledge within 5
working days, remove the material from `main` promptly and, when required,
rewrite the git history and ask GitHub Support to purge cached views; see
[`DISCLAIMER.md`](LICENSING.md#removal-requests).

## Summary

| Data source | Cases | Rights holder / author | Licence or terms | In this repo |
|---|---|---|---|---|
| CEN — PCP daily programme (PLEXOS model bases) | `chile/daily_scheduling/pcp_*` (14) | Coordinador Eléctrico Nacional (CEN), Chile | No open licence stated; public CEN publications, CEN keeps the rights; check CEN terms before redistribution | PLEXOS input bundles (`DATOS*.zip.xz`) + gtopt cases; PLEXOS results (`RES*.zip`) not redistributed |
| CEN — PLP medium/long-term programme | `chile/medium_long_term/plp_*` (3) | Coordinador Eléctrico Nacional (CEN), Chile | As above | PLP inputs + gtopt cases |
| AMM / EOR — PSR NCP daily/weekly programme | `guatemala/daily_scheduling/ncp_*` (2) | Administrador del Mercado Mayorista (AMM) and Ente Operador Regional (EOR) | No open licence stated; public AMM/EOR publications, they keep the rights; check their terms | Selected converter inputs (xz) + gtopt cases; original `.rar` archives and operator results not redistributed |
| AMM — PSS®E long-term study (BDD 2026-2027) | `guatemala/medium_long_term/psse_bdd_2026-2027/*` (6) | AMM (and EOR for regional data) | As above | PSS®E `.raw` / spreadsheets (xz) + gtopt cases |
| COES — MRFO 2026-2029 study, Anexo D (PSR SDDP base cases) | `peru/medium_long_term/coes_mrfo_2026-2029/*` (4) | Comité de Operación Económica del Sistema Interconectado Nacional (COES), Peru | No open licence stated; public COES publication, COES keeps the rights; cite COES; check its terms | SDDP inputs read by the converter (xz) + gtopt cases; original zip and PSR results not redistributed |
| MATPOWER `case3375wp` (Polish system, winter 2007-08 evening peak) | `poland/dc_opf/case3375wp` | Roman Korab, Silesian University of Technology; distributed by MATPOWER (PSERC / R. D. Zimmerman, C. E. Murillo-Sánchez) | **No explicit licence**: MATPOWER's BSD-3-Clause licence explicitly does **not** cover its case files; distributed with MATPOWER *"with the permission of Roman Korab"*; MATPOWER asks users of its data files to cite the MATPOWER paper | `.m` file unchanged (xz) + gtopt case |

## Details and attribution

### CEN (Chile)

- Publisher: Coordinador Eléctrico Nacional, <https://www.coordinador.cl>.
- PCP model bases (PLEXOS): "Programa de Operación" portal,
  <https://programa.coordinador.cl/operacion/pcp/bases-modelo> (download
  bucket serves Chilean IP addresses only).  PLP data: same portal.
- Terms: data derived from public CEN publications; CEN keeps the rights
  on the original data.  No open licence is stated.
- Attribution: *"Source: Coordinador Eléctrico Nacional (CEN), Programa
  de Operación, PCP/PLP model bases of <date>; converted to gtopt by the
  gtopt authors."*
- See [`chile/README.md`](chile/README.md).

### AMM and EOR (Guatemala)

- Publishers: Administrador del Mercado Mayorista, <https://www.amm.org.gt>
  (planning publications
  <https://www.amm.org.gt/ultpub/ultimas_pub_plani.php>; long-term
  programme databases such as
  `pdfs2/programas_despacho/03_PROGRAMAS_DE_LARGO_PLAZO/2026-2027/Base_de_datos_Programacion_2026-2027_Definitiva.rar`);
  Ente Operador Regional, <https://www.enteoperador.org> (maximum
  transfers, transfer-capacity studies).
- Terms: data derived from public AMM/EOR publications, which keep the
  rights; no open licence stated.
- Attribution: *"Source: Administrador del Mercado Mayorista (AMM) and
  Ente Operador Regional (EOR); converted to gtopt by the gtopt authors."*
- See [`guatemala/README.md`](guatemala/README.md).

### COES (Peru)

- Publisher: Comité de Operación Económica del Sistema Interconectado
  Nacional, <https://www.coes.org.pe>.
- Source: *Estudio de Verificación del Margen de Reserva Firme Objetivo
  2026-2029*, Anexo D, `DatosSDDP_CasoBase.zip` (PSR SDDP 17.3 base cases).
- Terms: public COES publication; COES keeps the rights; cite COES as the
  source; no open licence stated.
- Attribution: *"Source: COES, Estudio de Verificación del Margen de
  Reserva Firme Objetivo 2026-2029, Anexo D; converted to gtopt by the
  gtopt authors."*
- See [`peru/README.md`](peru/README.md).

### MATPOWER `case3375wp` (Poland)

- Data author: Roman Korab, Silesian University of Technology
  (Politechnika Śląska), Gliwice.  File: MATPOWER `data/case3375wp.m`,
  tag 8.1, commit `1a828c7af590714499284e36ee9c81273388c594`,
  <https://github.com/MATPOWER/matpower>; sha256
  `f814bc31845cfbfb7754610f3c9b496a2dfd5eb3f86601ff8be015c21653722f`.
- Terms: MATPOWER `LICENSE`: *"The MATPOWER case files distributed with
  MATPOWER are not covered by the BSD license.  In most cases, the data
  has either been included with permission or has been converted from data
  available from a public source."*  File header: *"This data was
  graciously provided by, and is distributed with the permission of, Roman
  Korab"*.  Redistributed here unchanged, with attribution.
- Citations (MATPOWER `CITATION`: publications using MATPOWER *or its data
  files* should cite the MATPOWER paper):
  - R. D. Zimmerman, C. E. Murillo-Sánchez and R. J. Thomas, "MATPOWER:
    Steady-State Operations, Planning, and Analysis Tools for Power
    Systems Research and Education," *IEEE Trans. Power Systems*, vol. 26,
    no. 1, pp. 12-19, Feb. 2011, doi: 10.1109/TPWRS.2010.2051168.
  - R. D. Zimmerman and C. E. Murillo-Sánchez, *MATPOWER (Version 8.1)*,
    2025, doi: 10.5281/zenodo.15871662.
  - Origin of the Polish cases: J. Snodgrass et al. (incl. R. Korab),
    "Case Study of Enhancing the MATPOWER Polish Electric Grid," *2022 IEEE
    Texas Power and Energy Conference (TPEC)*, doi:
    10.1109/TPEC54980.2022.9750807.
- Attribution: *"Polish system winter 2007-08 evening peak (case3375wp),
  data by R. Korab (Silesian University of Technology), distributed with
  MATPOWER 8.1; converted to gtopt by the gtopt authors."*
- See [`poland/dc_opf/case3375wp/README.md`](poland/dc_opf/case3375wp/README.md).
