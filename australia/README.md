# <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> Australia — National Electricity Market (NEM)

> [!WARNING]
> Provided **AS IS**, not validated by AEMO, which keeps all rights over
> the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the Australian National Electricity Market (NEM) built from the
**2026 Integrated System Plan (ISP)** PLEXOS model published by the
**Australian Energy Market Operator (AEMO)**.

| Application | Folder | Source | Converter |
|---|---|---|---|
| Production cost (weekly dispatch) | [production_cost/isp2026_sc_2027w03](production_cost/isp2026_sc_2027w03/README.md) | 2026 ISP PLEXOS model, Step Change scenario: 18-24 January 2027, 15 sub-regions | `plexos2gtopt.aemo_isp` (gtopt 1.1.0 or later) |

The case is a prototype: one hourly week of the ISP capacity-outlook
database with the fleet in service on its first day, no expansion and no
PLEXOS constraints (see the case README, "Limitations").

## Provenance and rights

* **Rights holder: Australian Energy Market Operator (AEMO)**.  This
  repository claims no ownership of the data (see
  [DISCLAIMER.md](../DISCLAIMER.md)).
* **Terms**: AEMO's
  [copyright permissions](https://aemo.com.au/privacy-and-legal-notices/copyright-permissions)
  give general permission to use AEMO material for any purpose, with
  accurate and appropriate attribution of the material and of AEMO as its
  author.  The scenario XML is redistributed unchanged (xz-compressed in
  `source/`) and the traces cut to the case week, with attribution; they
  will be removed on request of the rights holder.
* Attribution: *"Source: Australian Energy Market Operator (AEMO), 2026
  Integrated System Plan PLEXOS model (Step Change), © AEMO, used under
  AEMO's copyright permissions; converted to gtopt format."*  See
  [`../THIRD_PARTY_DATA.md`](../THIRD_PARTY_DATA.md).
* Converter, gtopt revision and file hashes:
  [`catalog.json`](../catalog.json).
