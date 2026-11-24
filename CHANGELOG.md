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

- **Benchmarks**: a new top-level collection, `benchmarks/`, for standard
  test systems, example systems of other tools and published case
  studies, grouped by family (catalog entries with
  `"collection": "benchmarks"` and a `family`; the country entries get
  `"collection": "countries"`):
  - `benchmarks/ieee/`: 9 single-hour DC OPF cases from PGLib-OPF v23.07
    (CC BY 4.0): PJM 5-bus, IEEE 14, 30, 57, 118 and 300 buses, IEEE
    RTS-79 (24 buses) and RTS-96 (73 buses), New England 39-bus; source
    `.m` files kept (xz), converted with `pp2gtopt`;
  - `benchmarks/unitcommitment_jl/`: 3 unit-commitment MIPs from the
    UnitCommitment.jl test fixtures (BSD-3-Clause): `case14`,
    `case14_profiled`, `case118_initcond`; converted with
    `tools/ucjl2gtopt.py --mip`;
  - recipes only, no data redistributed (the sources have no licence):
    `benchmarks/nrel/nrel118_2024w01` (NREL-118, first week, from Sienna
    PowerSystemsTestData, `nrel118_to_gtopt`), 7 Sienna PowerSimulations.jl
    5-bus systems in `benchmarks/sienna/` (`sienna_to_gtopt`), and the two
    clustered unit-commitment case studies of Morales-España and
    Tejada-Arango (2019) in `benchmarks/papers/morales_espana_2019_cuc/`
    (CUC-data; converter `cucdata2gtopt` in progress).
  Licence texts `LICENSES/CC-BY-4.0.txt` and `LICENSES/BSD-3-Clause.txt`.
- `tools/get_case.py`: plain-file and sha256-manifest downloads from a
  pinned upstream commit, cases whose converter fetches its own data
  (`"fetched_by": "converter"`), converters with their own command line
  (`converter.argv`, placeholders `{input}`, `{out_json}`, `{gtopt_src}`),
  `.xz`/`.gz` source decompression and `flatten` of a converter's
  time-series folder.
- This changelog.
- **Chile**: 14 source-only CEN PCP days, with no gtopt case built:
  test days for the study of negative nodal prices (2024-09-01,
  2024-10-03, 2024-12-15, 2025-02-17, 2025-04-10, 2025-04-27, 2025-06-26,
  2025-09-16) and for the comparison of line-loss models (2021-10-17,
  2021-10-24, 2026-05-10, 2026-05-25, 2026-11-03, 2026-11-09).  The four
  2026 days keep their PLEXOS input (`DATOS*.zip.xz`) in `source/`; the
  other ten are fetched on demand from the public `PLEXOS<date>.zip`
  files on www.coordinador.cl (sha256 in `catalog.json`), to keep the
  repository under its 400 MB limit.  PLEXOS databases 8.100 (2021),
  9.000 (2024) and 10.000 (2025-2026); they need `plexos2gtopt` from
  gtopt master of November 2026 or later.
- `tools/get_case.py fetch`: CEN PCP days (public PLEXOS file, or the
  bundle in `source/` plus the portal), `cache_members` extracted into
  the download cache, a default `case_json` for source-only entries, and
  the gtopt run command printed after each conversion.
- **Australia**: a first expansion-planning case,
  `australia/expansion/isp2026_sc_exp_fy28_3y`, from the AEMO 2026 ISP
  Step Change database: generation, storage and network-augmentation
  candidates over FY2028-FY2030 (plus a fill year), one representative
  day of 24 hourly blocks per month, solved as one monolithic LP.
  `source/` keeps the scenario XML only (the trace archives are not
  kept; see `source/NOT_KEPT.txt`).  Needs a gtopt build newer than the
  current release.
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

- **Chile PCP cases** (the 14 `pcp_*` weeks): rebuilt with
  `plexos2gtopt` from gtopt master `1d112feb1` (public `3dfa808d8`),
  flags unchanged.  The rebuild picks up the converter changes since the
  earlier development revision:
  - the end-of-horizon water values move from
    `monolithic_options.boundary_cuts_file` to `system.future_cost_array`
    (same `boundary_cuts.csv`);
  - BESS reserves are modelled natively (default `--bess-reserve
    native`) in the 12 weeks from 2025-11-09 on: the batteries that offer
    reserve carry `reserve_sustain_hours: 1`, their reserve provisions
    use provision factor 1 (instead of the hourly PLEXOS factors, e.g.
    0.2-0.82), and the PLEXOS `*_CF_GEN_COMP`, `*_CF_LOAD_COMP` and
    `UP/DOWNStorageBound_*` constraints that emulated them are kept but
    inactive;
  - the inactive constraint `Quintero_priority2` moves from
    `uc_operational.pampl` to the planning JSON (still inactive).
  The converter fix in this revision (battery charge power taken from the
  `Gen_Rating` data file instead of the 2 MW `Max Load` placeholder) has
  no effect on the published inputs, which predate the regression: every
  battery keeps `pmax_charge = pmax_discharge`.
  3 of 14 checked with CPLEX (`gtopt --lp-only`, gtopt `ef27b5f59`):
  `pcp_2025-10-05` (LP unchanged), `pcp_2026-04-22` and `pcp_2026-05-17`
  (4,440 and 4,400 fewer rows, same columns: the deactivated BESS
  constraints); `catalog.json` `size.lp` and the README LP rows are
  updated for those three only.
- **Chile PLP cases** (`plp_2y`, `plp_5y`, `plp_23y` and the three
  `plp_pet27` scenarios): the irrigation-diversion flow rights
  `RieSur123SCDZ_irrigation_right` and `RieSaltos_irrigation_right`,
  whose PLP `PotMax` is the 9999 "no limit" sentinel, now carry an
  explicit `fmax: 9999`.  Without it gtopt read the missing bound as
  zero and blocked those districts' offtake.  Rebuilt with `plp2gtopt`
  from gtopt master `ef27b5f59`; nothing else changes (the Parquet files
  are identical, and the LP keeps its size).  These sources have no
  `plpess.dat`, so the batteries still carry no `annual_loss` and gtopt
  applies its default battery self-discharge.
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
  - **Guatemala** `ncp_pdd_2026-06-22`: same parallel-unit and Jurún fixes
    as `ncp_week`.
- **Guatemala** `ncp_pdd_2026-06-22` and `ncp_week_2026-06-21`:
  interconnection imports are available only in the hours where they
  have an offer, and neither case adds an aggregate import limit (the
  sources set none; the old `--import-limit 200` is dropped from the
  flags).  Rebuilt with `sddp2gtopt` from gtopt commit `5a4fd2ef8`:
  - `ncp_pdd`: a blank or zero `PRECIOSMEX.csv` price closes the import
    in that hour, so imports run only on 21–22 Jun (`MEX-I`, never
    priced, is left out); `EDC-I` keeps its fixed `RESTMEX.csv` schedule.
    The old cap made the case infeasible, because it cut `EDC-I` below
    that schedule.  `case/boundary_cuts_gtopt_fcf.csv` (gtopt's own FCF,
    A/B alternative) is recomputed from the rebuilt case.  LP: 192,056
    rows, 302,762 columns, 605,654 nnz.
  - `ncp_week`: without `PRECIOSMEX.csv`, import units whose fuel costs
    $0 have no offer and are left out (16 units).  LP: 192,024 rows,
    281,898 columns, 585,262 nnz.

- **Australia** (`isp2026_sc_2027w03`, `w16`, `w29`, `w42`): rebuilt with
  the corrected `plexos2gtopt.aemo_isp` converter and its default flags.
  - **Hydro water units.**  Reservoirs declare
    `flow_conversion_rate = 0.0036` hm³ per m³/s·h.  Older gtopt builds
    assumed 3.6 when it was absent, so turbines moved 1000 times the water
    the inflows supplied.
  - **Pumped storage.**  Kidston, Shoalhaven, Wivenhoe and Tumut 3 pump
    from their tail to their head storage (`Waterway` + `Pump` + flexible
    `Demand`).  Before, they could only generate.
  - **Start and end levels.**  Week-start levels follow the source data
    (horizon-start `Initial Volume`, else `Target Week` / `Target`, else
    mid level), not an empty or arbitrary level.  End levels follow
    `Target Week` and `End Effects Method` Recycle.  Other storages end at
    their start volume, with no water value and no 10,000 $/hm³ penalty.
  - **Fuel cost per sent-out MWh.**  Fuel cost, gas offtake and
    emissions use `Heat Rate / (1 − Aux Incr)`, because the generator
    capacity is already net of auxiliary load.
  - Constraint terms on one flow direction (`Flow Forward` /
    `Flow Back`) use a directional flow variable instead of the signed
    flow.

  The default converter also adds the operational PLEXOS constraints:
  REZ buses with radial export / import lines, transmission group and
  purchaser-network limits, gas-zone daily offtake, electrolyser and
  industrial purchasers with pro-rated hydrogen demand, and emission
  tracking.  Each `source/traces/` therefore also keeps the DNSP and
  gas-zone trace files the case reads, cut to the week.  Objective values
  differ from 1.0.0.

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
