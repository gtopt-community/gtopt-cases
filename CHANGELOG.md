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

## [1.0.0] - 2026-11-20

First public release.  Real power-system cases from six countries, from
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
