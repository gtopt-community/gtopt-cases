# AMM long-term study 2026–2027 — PSS®E DC-OPF snapshots

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../../DISCLAIMER.md).

Six single-period snapshots (1 stage / 1 block / 1 scenario) of the network
used by the AMM long-term study *BDD ESO PLP AE MAY26-ABR27 Definitiva*:
about 871–877 buses, 942 lines, 115 generators and 255 demands each.

| Snapshot | Season | Demand level | LDM (costs) |
|---|---|---|---|
| [PAESEPMIN26](PAESEPMIN26) | Sep 2026 (wet) | minimum | LDM Septiembre 2026 |
| [PAESEPMED26](PAESEPMED26) | Sep 2026 (wet) | medium | LDM Septiembre 2026 |
| [PAESEPMAX26](PAESEPMAX26) | Sep 2026 (wet) | maximum | LDM Septiembre 2026 |
| [PAEMARMIN27](PAEMARMIN27) | Mar 2027 (dry) | minimum | LDM Marzo 2027 |
| [PAEMARMED27](PAEMARMED27) | Mar 2027 (dry) | medium | LDM Marzo 2027 |
| [PAEMARMAX27](PAEMARMAX27) | Mar 2027 (dry) | maximum | LDM Marzo 2027 |

`source/` (shared by the six snapshots) holds the PSS®E v33 `.raw` files,
the AMM `Nomenclatura` (bus names) and the two LDM spreadsheets, all xz.
Regenerate one snapshot with:

```bash
psse2gtopt -i source/PAESEPMED26.raw.xz -o PAESEPMED26/case \
  --nomenclatura source/Nomenclatura.xls.xz \
  --ldm "source/LDM Septiembre 2026.xlsx.xz" --rating-set A
```

Caveats: DC OPF only.  PSS®E RAW carries no costs: the LDM gives a
rank-based merit order (about half of the generators match by name).
Area 8 = Mexico is an EOR equivalent (27–35 GW), not Guatemalan load
(1.3–2.3 GW in area 1).

Each snapshot README has a **How to run** section (small LPs of about
950 rows; any machine); results go outside the repository.
