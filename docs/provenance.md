# Provenance

* **Daily scheduling**: CEN PCP bundles `PLEXOS<YYYYMMDD>.zip` from the CEN
  "Programa de Operación" portal.  `source/` keeps the PLEXOS input
  (`DATOS*.zip.xz`).  The PLEXOS solution (`RES*.zip`) is a result and is
  not redistributed; it is needed only to rebuild a case (block layout) and
  is fetched from the CEN portal by `tools/get_case.py`.  Ten source-only
  PCP days (2021 to September 2025) are not kept: `tools/get_case.py fetch`
  downloads their public `PLEXOS<YYYYMMDD>.zip` from
  `www.coordinador.cl/wp-content/uploads/` and checks the sha256 pinned
  in `catalog.json`.
* **Medium/long term**: CEN PLP input sets, kept in `source/` (xz) and
  converted with `plp2gtopt` from gtopt.
* **Chile, transmission planning (PLP-PET27)**: PLP bases of the CEN
  *Propuesta de Expansión de Transmisión del SEN 2027*, Diagnóstico,
  Anexo IV.1 (`Anexo-4.1-Base-PLP.zip`, coordinador.cl), kept in
  `source/` (xz; the IPLP `.xlsm` workbooks are not included) and
  converted with `plp2gtopt`; the Anexo II methodology PDF is kept as
  published in `plp_pet27/methodology/`.
* **Guatemala**: AMM PSR NCP models and PSS®E study files, converted with
  `sddp2gtopt` / `psse2gtopt` in the gtopt repository; inputs kept in
  `source/` (xz).
* **Guatemala, long-term SDDP programmes**: AMM PSR SDDP databases
  (`Base_de_datos_Programacion_<years>_Definitiva.rar`, AMM programmes
  portal), converted with `sddp2gtopt`; converter inputs kept in `source/`
  (xz), archives not redistributed.
* **Peru**: COES PSR SDDP base cases (`DatosSDDP_CasoBase.zip`, Anexo D of
  the MRFO 2026-2029 study), converted with `sddp2gtopt`; converter inputs
  kept once in `source/` (xz), archive not redistributed.

* **Australia**: AEMO 2026 ISP PLEXOS model (`2026 ISP Model.zip` and the
  Solar, Wind, Hydro and Timeslice trace zips, AEMO ISP page); the Step
  Change scenario XML kept unchanged in `source/` (xz) and the trace files
  read cut to the case week, converted with `plexos2gtopt.aemo_isp`
  (gtopt 1.1.0 or later).

* **Ireland**: SEM Committee publication SEM-25-010 (SEM PLEXOS Forecast
  Model 2024-2032, public version, and two CSV archives).  **Not
  redistributed**: `tools/get_case.py fetch sem_2025w03` downloads the
  archives (URLs and sha256 in `catalog.json`) and converts them with
  `plexos2gtopt --plexos-model` (gtopt 1.1.0 or later).

* **Poland**: MATPOWER 8.1 `data/case3375wp.m` (data by R. Korab),
  kept unchanged in `source/` (xz) and converted with `pp2gtopt` (gtopt,
  `matpower` extra of the scripts).

* **Benchmarks** (`benchmarks/`): PGLib-OPF v23.07 `.m` files (CC BY
  4.0) and UnitCommitment.jl test fixtures (BSD-3-Clause), kept unchanged
  in `source/` (xz; the fixtures gzip as published) and converted with
  `pp2gtopt` and `tools/ucjl2gtopt.py`.  Sources without a licence (Sienna
  `PowerSystemsTestData` for NREL-118 and the Sienna 5-bus systems, the
  `CUC-data` workbooks of Morales-España and Tejada-Arango 2019) are **not
  redistributed**: `tools/get_case.py fetch <case>` downloads the files of
  a pinned upstream commit, checks their sha256 (in `catalog.json`, the
  case `upstream.sha256` manifest, or the converter's own manifest) and
  converts them with `nrel118_to_gtopt`, `sienna2gtopt` or
  `cucdata2gtopt`.

* Every case was converted with the named tool (`plexos2gtopt`,
  `plp2gtopt`, `sddp2gtopt`, `psse2gtopt`, `pp2gtopt`,
  `plexos2gtopt.aemo_isp`) from gtopt; rebuild with gtopt master of
  November 2026 or later (`plexos2gtopt.aemo_isp`: gtopt 1.1.0 or later).
* The exact flags and file hashes of each case are in `catalog.json`.  Its
  `gtopt_revision` (and `converter_last_change`) fields record the gtopt
  development revision used for the conversion (pre-publication history;
  may not exist in the public repository); the same holds for the gtopt
  revisions quoted in the case READMEs.

The CEN portal only serves Chilean IP addresses; from abroad, download
through a relay/VPN in Chile or copy the files by hand (`DATOS*.zip.xz`
into the case `source/`, the solution bundle via `--res`).
