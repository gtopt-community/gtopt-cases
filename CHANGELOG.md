# Changelog

All notable changes to gtopt-cases are recorded here.  The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and releases
are numbered with [Semantic Versioning](https://semver.org/):

- **major**: a case is removed or moved to another path, or the case
  format needs a newer gtopt major version;
- **minor**: new cases, countries or applications, or a case rebuilt
  with different results (new source data, converter flags or profile);
- **patch**: documentation, metadata and tooling fixes that leave every
  `case/` unchanged.

Each release states the minimum gtopt version its cases need.

## [Unreleased]

### Added

- This changelog.
- **Australia**: three more weekly dispatches from the AEMO 2026 ISP
  Step Change database, so there is one week per season of 2027:
  `isp2026_sc_2027w16` (19-25 April), `isp2026_sc_2027w29` (19-25 July)
  and `isp2026_sc_2027w42` (18-24 October), each with its own `source/`
  (scenario XML and the trace files it reads, cut to the week) and
  `case/`.
- **Ireland**: three more weekly unit-commitment recipes from the SEM
  PLEXOS Forecast Model 2024-2032, one week per season of 2025:
  `sem_2025w16` (14-20 April), `sem_2025w29` (14-20 July) and
  `sem_2025w42` (13-19 October).  From April 2025 the model includes the
  Greenlink interconnector.  As for `sem_2025w03`, the data are not
  redistributed; `tools/get_case.py fetch <case>` builds them locally.

### Fixed

- **Hydro cascade topology of the `sddp2gtopt` cases** (Peru and
  Guatemala).  PSR SDDP gives each hydro plant two downstream plants:
  `TAA` receives the turbined water and `VAA` the spilled water.  Earlier
  `sddp2gtopt` swapped them (SDDP cases) or read only `VAA` (NCP cases),
  so water reached the wrong plants.  Rebuilt with gtopt master
  `16d307666` or later:
  - **Peru** `coes_mrfo_2026-2029/2026` … `2029`: Machupicchu now turbines
    into Santa Teresa and Mantaro into Restitución, and cascades pass
    through plants not yet in service (Sibinacocha → … → Machupicchu).
    6 turbines and 24 spill paths change destination; the LPs keep their
    rows and gain 20,160 columns (spill arcs to the next plant).
  - **Guatemala** `sddp_plp_2021-2022` … `sddp_plp_2026-2027`: 5 turbines
    and 5 spill paths change destination (e.g. `MTO-H` now turbines into
    `REC-H`, and `CAN-H` spills past `MTO-H`); LP size unchanged.
  - **Guatemala** `ncp_week_2026-06-21`: the parallel units of a plant
    (`CHX-H1`…`H5`, `JUR-H1`…`H3`, `LVA-H1`…`H4`, …) spill into the next
    unit but turbine to the river, so the same water is no longer
    turbined several times; the `JUR-H` units now turbine into `HSM-H`.  This
    rebuild also picks up the converter changes since the earlier
    development revision (the `--import-limit` cap now covers every
    interconnection import, bus voltages), so its LP grows from 160,608
    to 192,024 rows.

### Changed

- `tools/get_case.py fetch`: cases that use the same archives share one
  download folder (`source.cache` in `catalog.json`), so the four Irish
  weeks download the SEM archives once.

## [1.0.0] - 2026-11-20

First public release: 41 real power-system cases from six countries, from
a one-hour DC OPF to a 23-year hydrothermal SDDP.  Needs gtopt **1.1.0
or later**.

### Added

- **Australia** (NEM · AEMO): one weekly dispatch converted from the
  PLEXOS model of the 2026 Integrated System Plan, Step Change scenario.
- **Chile** (SEN · CEN):
  - 14 daily operation programmes (PCP), each scheduling one week, as
    unit commitment MIPs converted from the published PLEXOS databases;
  - three SDDP cases of 2, 5 and 23 years from the PLP medium/long-term
    programme inputs, with the Laja and Maule irrigation agreements and
    selectable hydrologies;
  - three SDDP bases of the 2027 Transmission Planning Process
    (PET 2027, scenarios E01, E02 and E03) with the planned line works.
- **Guatemala** (SNI · AMM, EOR): two daily/weekly NCP dispatches, six
  annual long-term SDDP programmes (2021-2022 to 2026-2027) and six
  PSS®E network snapshots.
- **Ireland** (SEM · SEM Committee): one weekly unit commitment
  (116 units, 61 with commitment) from the SEM PLEXOS model.  Recipe
  only: the data are not redistributed, and `tools/get_case.py fetch
  sem_2025w03` downloads them from the official source and converts them
  locally.  The case runs at a 0.1 % MIP gap.
- **Peru** (SEIN · COES): four annual SDDP cases from the 2026-2029
  reserve-margin study.
- **Poland** (R. Korab / MATPOWER): a 3,374-bus DC OPF (case3375wp).
- Per case: `source/` with the data as published (xz-compressed),
  `case/` with the gtopt case, and a README with the commands to run
  it and to rebuild it with gtopt's converters (`plexos2gtopt`,
  `plp2gtopt`, `sddp2gtopt`, `psse2gtopt`, `pp2gtopt`).
- `catalog.json` with provenance (converter, flags, SHA-256 and size of
  every source file) and model size for every case, and the
  [case index](docs/cases.md).
- `tools/get_case.py` to download the source of a case and convert or
  rebuild it with the pinned flags, and `tools/check_repo.sh` to keep the
  repository inputs-only and small.
- Disclaimer, licensing (REUSE annotations; third-party data keep their
  publishers' rights) and contribution guide.

### Notes

- The 23-year Chilean cases (`plp_23y`, PET 2027) ship the full
  276-stage source, but their `case/` holds only the first year to keep
  the repository small; each README gives the command that builds the
  full horizon.
- The cases are inputs only; no gtopt results are published.

[Unreleased]: https://github.com/gtopt-community/gtopt-cases/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/gtopt-community/gtopt-cases/releases/tag/v1.0.0
