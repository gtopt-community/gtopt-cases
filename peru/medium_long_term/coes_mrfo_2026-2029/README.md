# coes_mrfo_2026-2029 — Peru SEIN, COES SDDP base cases 2026–2029

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

Four one-year hydrothermal cases of the Peruvian SEIN, converted with
`sddp2gtopt` from the PSR SDDP base cases of the COES study *Estudio de
Verificación del Margen de Reserva Firme Objetivo 2026-2029* (Anexo D,
`DatosSDDP_CasoBase.zip`).  Each year has 12 monthly stages with 5 load
blocks, **56 historical hydrologies** (1966–2021) and a DC network with
losses, solved with SDDP (one phase per month, one scene per hydrology).

| Case | Horizon | Buses | Lines | Generators | Reservoirs | LP (`--lp-only`) |
|---|---|---:|---:|---:|---:|---|
| [2026](2026) | 2026-01 … 2026-12, 60 blocks | 270 | 312 | 157 | 60 | 6,457,304 rows, 13,086,584 cols, 31,659,488 nnz over 672 LPs |
| [2027](2027) | 2027-01 … 2027-12, 60 blocks | 270 | 331 | 162 | 60 | 6,640,984 rows, 13,472,984 cols, 32,955,888 nnz over 672 LPs |
| [2028](2028) | 2028-01 … 2028-12, 60 blocks | 270 | 346 | 162 | 60 | 6,915,664 rows, 14,069,384 cols, 34,964,048 nnz over 672 LPs |
| [2029](2029) | 2029-01 … 2029-12, 60 blocks | 270 | 394 | 163 | 60 | 7,514,584 rows, 15,384,824 cols, 39,129,048 nnz over 672 LPs |

The four source studies differ **only** in `sddp.dat` (start year and
one parameter line), so the inputs are stored once:

```
coes_mrfo_2026-2029/
├── README.md            this file
├── source/              PSR SDDP input files sddp2gtopt reads (xz), common to all years
│   ├── blrenw005pe.dat.{1..4}.xz   renewable profiles, split in 4 xz streams (< 10 MB each)
│   └── <year>/sddp.dat.xz          the only per-year file
└── <year>/              2026, 2027, 2028, 2029
    ├── README.md
    └── case/            coes_mrfo_<year>.json + Parquet schedules
```

Files of the original study that the converter does not read are not
included: hourly chronology (`hrrenw*`, `hrload*`, `hrbmap*`), gas
network, clustering files and PSR outputs.

## Source and data terms

- **Rights holder: COES** (*Comité de Operación Económica del Sistema
  Interconectado Nacional*, Peru), <https://www.coes.org.pe>.  All rights
  to the original data belong to COES; this repository claims no
  ownership of them.  Cite COES as the source and check its terms of use
  before any further redistribution.
- Public source (zip not redistributed here):
  [`DatosSDDP_CasoBase.zip`](https://www.coes.org.pe/portal/browser/download?url=Planificaci%C3%B3n%2FEstudios%20de%20Verificacion%20del%20Margen%20de%20Reserva%20Firme%2FMRFO_2026-2029%2FAnexos%2FANEXO%20D%2FDatosSDDP_CasoBase.zip)
  — COES, *Estudio de Verificación del Margen de Reserva Firme Objetivo
  2026-2029*, Anexo D (folders `01_SDDP_Base_Horario_<year>`, SDDP 17.3).
- Only model inputs are published here; PSR results are not
  redistributed.  These cases are **not** an official COES product and
  simplify the PSR model (see below).

## How to run

Results are never written into this repository: run from an output
directory outside it.

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
Y=2026
C=$REPO/peru/medium_long_term/coes_mrfo_2026-2029/$Y/case
OUT=~/gtopt-cases-out/peru/medium_long_term/coes_mrfo_2026-2029/$Y
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/coes_mrfo_$Y.json" --set input_directory="$C" -d . \
    --set sddp_options.max_iterations=15 --set sddp_options.num_apertures=8
```

- `options.method` is `sddp`: one phase per month, one scene per
  hydrology.  The objective is in $ (`scale_objective` = 1000); the 12 %
  annual discount rate comes from `sddp.dat`.
- Each SDDP iteration solves about 56 × 12 forward LPs and 56 × 11 ×
  apertures backward LPs; reduce the work with
  `--set sddp_options.num_apertures=N`, or regenerate with fewer series
  (`--num-scenarios`, below).
- Expected resources: **large** — plan for 8+ cores and 16+ GB RAM.
- Check that your gtopt reads the case as intended (LP size vs
  `catalog.json`): `gtopt_check_cases --repo "$REPO" --only coes_mrfo_2026-2029`.

## How to regenerate

The cases were converted with `sddp2gtopt` from gtopt; rebuild with gtopt
master `16d307666` or later (the hydro cascade fix, see the CHANGELOG).  Running the cases needs only a recent
gtopt.

```bash
tools/get_case.py rebuild peru/medium_long_term/coes_mrfo_2026-2029/2027 --out <dir outside the repo>
```

reproduces `<year>/case/` byte for byte: it stages `source/` with
`source/<year>/sddp.dat.xz` on top and joins the split parts.  By hand,
from this folder:

```bash
Y=2027; IN=$(mktemp -d)
for f in source/*.xz; do ln -s "$PWD/$f" "$IN/"; done
rm "$IN"/blrenw005pe.dat.?.xz
cat source/blrenw005pe.dat.{1,2,3,4}.xz > "$IN/blrenw005pe.dat.xz"   # xz streams concatenate
ln -sf "$PWD/source/$Y/sddp.dat.xz" "$IN/sddp.dat.xz"
sddp2gtopt -i "$IN" -o <dir>/coes_mrfo_$Y                    # all 56 series, SDDP
sddp2gtopt -i "$IN" -o <dir>/small --num-scenarios 8         # first 8 series
sddp2gtopt -i "$IN" -o <dir>/mono --method monolithic        # single LP
```

## What is modelled

| PSR SDDP | gtopt |
|----------|-------|
| Demand: `deme05pe` (GWh per block and class) × `dbf005pe` bus weights | `Demand` per bus (MW per block) |
| `dbus`, `dcirc`/`mcirc` (R, X in % at 100 MVA; dated changes), losses flag | `Bus`, `Line` (Ω, `tmax`, `active`), Kirchhoff + piecewise losses (3 segments) |
| Thermal plants `ctermipe`/`mtermipe`, fuels `ccombupe` | `Generator`: `gcost` = CEsp × fuel + CVaria; `pmax` = GerMax × maintenance (`pmtrmepe`) × (1−Teif)(1−Ih) × reserve derating (`rrme05pe`); must-run `pmin` |
| Generation constraints `rgme05pe` | `<` caps `pmax`; `>` floors become a soft `pmin` penalised at the deficit cost |
| Hydro `chidrope`/`mhidrope`, `htopol`, maintenance `pmhimepe` | `Junction`, `Turbine` (FPMed, QMax), `Reservoir` with state (VMin/VMax; `VInic` p.u.), turbined/spilled `Waterway`s |
| `vminmepe`, `vmxomepe`, `mntomepe`, `mxtbmepe`, `riegmepe` | soft reservoir minimum, `emax`, soft minimum outflow, turbine cap, irrigation |
| `hinflw` | `Flow` inflows per scenario (historical year 1965 + *s*, calendar month).  Inflow of plants that never operate in the case year goes to the next downstream plant |
| Renewables `cgndpe`/`mgndpe`/`gndsitepe`, profiles `blrenw005pe`(`0`) | `Generator` + `GeneratorProfile` (scenario × stage × block) |
| Batteries `cbatterype`/`mbatterype` | `Battery` (none in service in 2026–2029) |
| Deficit 6000 $/MWh, spill penalty | `demand_fail_cost`, spill `fcost` |

Existence flags work as follows.  A *future* element (`Tipo`/`I` = 1)
enters service at the date of its first modification record.  A future
element with no modification record never operates.

## Simplified or not modelled

- **Hourly chronology.**  The PSR run uses an hourly model with 168-h
  sub-stages.  This case keeps the 5 load blocks per month.
- **Thermal unit commitment.**  Start-ups, minimum up/down times and
  ramps (`opectrpe`) are relaxed.  GerMin applies only to must-run units.
- **Hydro physics.**  Production factor vs. head, evaporation, filtration
  and non-controllable spill are not modelled; the mean factor (FPMed) is
  used.
- **Network extras.**  Maximum total outflow (`mxtomepe`), joint and individual reserves (`rsme05pe`/`resgerpe`),
  the gas network, sum-of-flow limits (`csumcirc`/`msumcirc005`),
  contingencies and transmission-outage sampling are not modelled.
- **Outages and emissions.**  Random generator outages are not sampled;
  only the Teif/Ih derating is applied.  Emission costs are not included.
- **Policy.**  PSR simulated an external future-cost function, which is
  not part of the case data.  gtopt builds its own SDDP policy over the
  12 months, with no boundary future cost.
