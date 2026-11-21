# `sddp_plp_2023-2024` — Guatemala SNI, AMM long-term programme 2023-2024

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

A gtopt version of the AMM PSR SDDP database for the long-term
programme (*Programación de Largo Plazo*) 2023-2024, *Versión Definitiva*.
It was built by `sddp2gtopt`.

The case covers 12 monthly stages from 2023-05 with 9 load blocks per
stage.  It uses 1 historical hydrology (the source study's single
series) and models the DC network with losses.

| Field | Value |
|---|---|
| Case id | `guatemala/medium_long_term/sddp_plp_2023-2024` |
| Horizon | 12 monthly stages = 12 SDDP phases, 108 blocks, 8,784 h, from 2023-05 |
| Scenarios | 1 (the study's single hydrology) |
| Network | 461 buses, 519 lines |
| LP (`--lp-only`) | 190,836 rows, 375,217 cols, 847,405 nnz over 12 phase LPs (gtopt development revision `75d9cec1ce81`) |
| Method / profile | sddp, no profile (options in the case JSON) |
| Converter | `sddp2gtopt` from gtopt; rebuild with gtopt master `16d307666` or later (revision used: `catalog.json`) |

## Source and data terms

- The data was published by the **AMM** (Administrador del Mercado
  Mayorista, Guatemala) on its programmes page.  Source archive (not redistributed):
  <https://www.amm.org.gt/pdfs2/programas_despacho/03_PROGRAMAS_DE_LARGO_PLAZO/2023-2024/Base_de_datos_Programacion_2023-2024_Definitiva.rar>.
- The source file is `Base_de_datos_Programacion_2023-2024_Definitiva.rar` (header: “Programación Anual Estacional 2023-2024 Versión Definitiva, SDDP versión 17.2.1”).
- The data belongs to the AMM.  Only the converter inputs are redistributed
  here (`source/`), to make a public benchmark reproducible.  Check the AMM's terms of use before any
  further redistribution, and cite the AMM as the source.
- This package is **not** an official AMM product.  The conversion
  simplifies the model (see below).
- See the AS-IS terms in [DISCLAIMER.md](../../../DISCLAIMER.md) and
  the Guatemala data terms in [../../README.md](../../README.md).

## Files

- `source/` — the PSR SDDP input files `sddp2gtopt` reads, xz-compressed,
  extracted from the AMM archive (hourly variants, outputs and files the
  converter does not read are not included).
- `case/` — `sddp_plp_2023-2024.json` and its Parquet schedules (long format, global
  block uids).

## How to run

Results are never written into this repository: run from an output
directory outside it.

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/guatemala/medium_long_term/sddp_plp_2023-2024/case
OUT=~/gtopt-cases-out/guatemala/medium_long_term/sddp_plp_2023-2024
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/sddp_plp_2023-2024.json" --set input_directory="$C" -d . \
    --set sddp_options.max_iterations=10
```

- `options.method` is `sddp`, with one phase per month and one scene.
  The objective is in $ (`scale_objective` = 1000); discount rate 12 %.
- Check that your gtopt reads the case as intended (LP size vs
  `catalog.json`): `gtopt_check_cases --repo "$REPO" --only sddp_plp_2023-2024`.

## How to regenerate

With `sddp2gtopt` from gtopt master `16d307666` or later (it reads the `.xz`
files directly), from this folder:

```bash
sddp2gtopt -i source -o <dir outside the repo>/sddp_plp_2023-2024
sddp2gtopt -i source -o <dir>/mono --method monolithic   # single LP variant
```

`tools/get_case.py rebuild sddp_plp_2023-2024 --out <dir outside the repo>`
reproduces `case/`.

## What is modelled

- **Demand.**  `deme09gu` × `dbf009gu` gives demand per bus and block.
  The load classes include the export classes.
- **Network.**  `dbus`/`busconnection`/`dcirc`/`mcirc` give the buses and
  lines: R, X in % at 100 MVA converted to Ω, rating as `tmax`, dated
  changes, and decommissioned circuits dropped.
- **Thermal plants** (`ctermigu`/`mtermigu`):
  - `gcost` = CEsp × fuel price, using the monthly `combmegu`, else
    `ccombugu`, plus CVaria;
  - maintenance from `pmtrmegu` (per-table units/info flags);
  - `rrme09gu` derating;
  - `rgme09gu` caps and soft floors.
- **Hydro plants** (`chidrogu`, `pmhimegu`):
  - turbines with FPMed and QMax;
  - reservoirs with state.  The initial volume comes from the elevation
    `VInic` (`tini` = 1) through the plant's Cota/Vol table;
  - soft minimum volumes (`vminmegu`);
  - inflows from `hinflw` (hydrology year 2018, same calendar month).
- **Renewables.**  `cgndgu`/`gndsitegu`, with the typical-year block
  profile `blrenw009gu0.dat`.

## Simplified or not modelled

- **Deficit cost.**  The PSR curve is piecewise (2 % at 300.7 $/MWh, 3 % at 375.87 $/MWh, 5 % at 451.05 $/MWh, 90 % at 1879.37 $/MWh).  Here a
  single `demand_fail_cost` is used, set to the first segment's cost.
- **Not modelled:**
  - hourly/weekly variants (`*_w`, `hparam_w`, …);
  - unit commitment and ramps;
  - joint reserves (`rsme`, `rxme`, `rpme`);
  - production-factor × volume curves, evaporation and filtration;
  - random outages;
  - the two additional years.
- **Dropped demand.**  None.
