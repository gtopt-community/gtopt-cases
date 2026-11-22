# <img src="https://flagcdn.com/w40/au.png" width="28" align="absmiddle" alt="🇦🇺"> Australia — National Electricity Market (NEM)

> [!WARNING]
> Provided **AS IS**, not validated by AEMO, which keeps all rights over
> the data.  See the [disclaimer](../DISCLAIMER.md).

Cases of the Australian National Electricity Market (NEM) built from the
**2026 Integrated System Plan (ISP)** PLEXOS model published by the
**Australian Energy Market Operator (AEMO)**.

| Application | Folder | Source | Converter |
|---|---|---|---|
| Production cost (weekly dispatch), summer | [production_cost/isp2026_sc_2027w03](production_cost/isp2026_sc_2027w03/README.md) | 2026 ISP PLEXOS model, Step Change scenario: 18-24 January 2027, 15 sub-regions and 20 REZ buses | `plexos2gtopt.aemo_isp` (gtopt 1.1.0 or later) |
| Production cost (weekly dispatch), autumn | [production_cost/isp2026_sc_2027w16](production_cost/isp2026_sc_2027w16/README.md) | same model: 19-25 April 2027 | same |
| Production cost (weekly dispatch), winter | [production_cost/isp2026_sc_2027w29](production_cost/isp2026_sc_2027w29/README.md) | same model: 19-25 July 2027 | same |
| Production cost (weekly dispatch), spring | [production_cost/isp2026_sc_2027w42](production_cost/isp2026_sc_2027w42/README.md) | same model: 18-24 October 2027 | same |
| Expansion planning (prototype) | [expansion/isp2026_sc_exp_fy28_3y](expansion/isp2026_sc_exp_fy28_3y/README.md) | same model: FY2028-FY2030 plus a fill year, one representative day per month | `plexos2gtopt.aemo_isp_expansion` (not yet released) |

The weekly cases are prototypes: one hourly week of the ISP capacity-outlook
database with the fleet in service on its first day and no expansion.
The operational PLEXOS constraints (REZ, transmission group, purchaser
network, gas-zone offtake), pumped storage, purchasers and hydrogen demand
are converted; long-period policy targets are not enforced (see the case
README, "Limitations").  The four weeks,
one per season of 2027, come from the same scenario database and differ
in demand, renewable and hydro traces, seasonal line limits and the fleet
in service (523 to 542 generators, 85 to 106 batteries as new projects
enter).  Each one solves in a few seconds with HiGHS.

| | Summer (w03) | Autumn (w16) | Winter (w29) | Spring (w42) |
|---|---:|---:|---:|---:|
| Peak demand (MW) | 30,650 | 27,902 | 32,710 | 28,811 |
| Weekly demand (GWh) | 4,155 | 3,870 | 4,540 | 3,925 |
| Wind capability (MW) | 12,066 | 11,030 | 12,375 | 13,789 |
| Solar + rooftop PV (MW) | 31,648 | 28,596 | 27,943 | 35,885 |
| Batteries (MW) | 10,952 | 12,025 | 14,456 | 15,480 |
| LP rows | 143,688 | 149,907 | 162,695 | 170,267 |

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
