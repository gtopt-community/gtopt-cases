# NREL Sienna test systems

> [!WARNING]
> Provided **AS IS**, not validated by the data authors, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

Small test systems of NREL's Sienna
(PowerSimulations.jl / PowerSystemCaseBuilder.jl), each exercising one
modelling feature, ported by gtopt's `sienna_to_gtopt`.  Their data
(`PowerSystemsTestData`) have no licence: every case here is a recipe,
built locally by `tools/get_case.py fetch` (the converter downloads the
pinned, sha256-checked files itself).

| Case | What | Network | Application | In this repository |
|---|---|---|---|---|
| [batt_test_case_b](batt_test_case_b/README.md) | Sienna batt_test_case_b_sys: single-bus battery test system (wind, load, one battery), subcase b | 1 buses | production_cost | recipe only |
| [c_sys5_dc](c_sys5_dc/README.md) | Sienna c_sys5_dc: PJM 5-bus system with one branch as an HVDC link (no Kirchhoff row) | 5 buses | production_cost | recipe only |
| [c_sys5_hy_cascading](c_sys5_hy_cascading/README.md) | Sienna c_sys5_hy_cascading_turbine_energy: PJM 5-bus system with three hydro units in cascade (reservoirs, waterways, turbines) | 5 buses | production_cost | recipe only |
| [c_sys5_il](c_sys5_il/README.md) | Sienna c_sys5_il: PJM 5-bus system with an interruptible load | 5 buses | production_cost | recipe only |
| [c_sys5_ml](c_sys5_ml/README.md) | Sienna c_sys5_ml: PJM 5-bus system with a single monitored line (only its thermal limit is enforced) | 5 buses | production_cost | recipe only |
| [c_sys5_phes_ed](c_sys5_phes_ed/README.md) | Sienna c_sys5_phes_ed: PJM 5-bus system with a pumped-storage hydro plant | 5 buses | production_cost | recipe only |
| [c_sys5_re_fuel_cost](c_sys5_re_fuel_cost/README.md) | Sienna c_sys5_re_fuel_cost: PJM 5-bus system with time-varying fuel prices | 5 buses | production_cost | recipe only |

Licence, citation and the exact converter command of each case are in its
README; machine-readable provenance is in [`catalog.json`](../../catalog.json).
