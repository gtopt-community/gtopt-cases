# isp2026_sc_2027w29 — Australian NEM, AEMO 2026 ISP Step Change, one week of July 2027 (hourly dispatch)

> [!WARNING]
> Provided **AS IS**, not validated by AEMO, which keeps all rights over
> the data.  See the [disclaimer](../../../DISCLAIMER.md).

> [!NOTE]
> **Prototype.**  An operational week of the ISP capacity-outlook
> database, built with `python -m plexos2gtopt.aemo_isp` (gtopt 1.1.0 or
> later).  There is no expansion, and the PLEXOS constraint set is not
> converted (see [Limitations](#limitations)).

This case covers one week, Monday 19 to Sunday 25 July 2027 (168 hourly
blocks).  The source is the **Step Change** scenario of AEMO's **2026
Integrated System Plan (ISP)** PLEXOS model, which is the "DLT" (Detailed
Long-Term) capacity-outlook database.  The week is dispatched with the fleet
in service on 19 July 2027:

- 15 sub-regional buses;
- 18 notional inter-sub-regional flow paths;
- the ISP half-hourly demand, solar, wind and rooftop-PV traces, averaged to
  hourly values;
- the Snowy, Tasmanian, Victorian and Queensland hydro storages with their
  natural inflows;
- 100 battery and coordinated consumer-storage aggregates.

This is the winter week of four seasonal weeks of 2027
(`isp2026_sc_2027w03`, `w16`, `w29` and `w42`), converted from the same
database; see the [Australia README](../../README.md).

| Field | Value |
|---|---|
| Case id | `australia/production_cost/isp2026_sc_2027w29` |
| Horizon | 2027-07-19 00:00 to 2027-07-25 24:00: 168 blocks of 1 h, 1 stage, 1 scenario |
| Network | 15 buses (sub-regions NQ, CQ, GG, SQ, NNSW, CNSW, SNW, SNSW, VIC: MEL, SEV, WNV, TAS, CSA, NSA, SESA); 18 flow paths with seasonal (timesliced) limits; transport model, lossless |
| Units | 540 generators.  Maximum hourly capability: coal 20,017 MW, gas 11,024 MW, hydro 7,592 MW, liquid fuel 539 MW, wind 12,375 MW, utility solar plus rooftop PV 27,943 MW, DSP 404 MW |
| Storage | 100 batteries (14,456 MW, 39,974 MWh); 22 hydro reservoirs (19,810 hm³ capacity), 25 waterways, 95 turbines, 13 inflow series |
| Demand | 15 sub-regional loads; 20,010 to 32,710 MW; 4,540,091 MWh in the week (POE10 operational sent-out "PVLITE" traces) |
| Constraints | 14 daily energy limits (`daily_sum`): 2 DSP `Max Energy Day` (NSW, VIC) and 12 non-storage hydro units (Bogong, McKay, West Kiewa) `Max Energy Year` / 365 |
| LP | 143,792 rows, 264,232 cols, 500,204 nonzeros |
| Method / profile | monolithic LP, no profile |
| Converter | `python -m plexos2gtopt.aemo_isp`, gtopt 1.1.0 or later (revision used: `7d92e51ea`) |

## Files

- `case/isp2026_sc_2027w29.json`: the gtopt planning.
- `case/Generator/pmax.parquet`, `case/Demand/lmax.parquet`,
  `case/Line/tmax_ab.parquet`, `case/Line/tmax_ba.parquet` and
  `case/Flow/discharge.parquet`: hourly schedules in long format
  (`[scenario,] stage, block, uid, value`).
- `case/isp2026_sc_2027w29.stats.json`: converter statistics, including the
  list of PLEXOS trace files read.
- `case/isp2026_sc_2027w29.provenance.json`: archive hashes, converter
  revision and arguments.
- `source/2026 ISP Step Change Model.xml.xz`: the scenario database,
  unchanged, xz-compressed.
- `source/traces/`: the 263 trace files read for this week, cut to the
  week's rows.  `source/traces.sha256` lists their checksums.
- `source/NOT_KEPT.txt`: what was downloaded but is not kept here.

## Source and licence

| | |
|---|---|
| Publisher | Australian Energy Market Operator (AEMO) |
| Dataset | 2026 Integrated System Plan (ISP): PLEXOS model and trace files |
| Page | <https://www.aemo.com.au/energy-systems/major-publications/integrated-system-plan-isp/2026-integrated-system-plan-isp> |
| `2026 ISP Model.zip` | 116,917,347 bytes, sha256 `d25ad3905dd6e8bffcdd53f323d6caccd4d188f2e10c600d5a97a35d9616e6f2` |
| `2026 ISP Solar traces.zip` | 103,470,007 bytes, sha256 `ce364d7c6eddfebaf23a56569732fb90bdb93f051007df79d3d6dda6d50fb689` |
| `2026 ISP Wind traces.zip` | 159,258,886 bytes, sha256 `7a14094b68437356c20da1048714b62c1a082b030573531e690b3bf6df22d844` |
| `2026 ISP Hydro traces.zip` | 4,976,828 bytes, sha256 `e66ce0f94dd13a7414d6defa5b5405b479bae86c4db82d5323e9591f66e2dc5c` |
| `2026 ISP Timeslice traces.zip` | 12,204 bytes, sha256 `66c21860a84de67f7164b4010e0fdb04df6bd03746878264e3c514358d40c3bd` |
| Scenario XML | `2026 ISP Step Change/2026 ISP Step Change Model.xml`, sha256 `19cc3451f1ee00955019bb501d800e629bb740e3bb51e270020ef2dd7485a849` (PLEXOS MasterDataSet; confidential data removed by AEMO) |
| Copyright | © AEMO |

**Terms.**  AEMO's copyright permissions
(<https://aemo.com.au/privacy-and-legal-notices/copyright-permissions>)
say:

> "AEMO confirms its general permission for anyone to use AEMO Material
> for any purpose, but only with accurate and appropriate attribution of
> the relevant AEMO Material and AEMO as its author. You do not need to
> obtain specific permission to use AEMO Material in this way."

Confidential documents and reports that third parties commissioned are
excluded.  This folder redistributes AEMO material (the scenario XML and a
cut-down copy of its traces) and derived data under that permission.  See
[LICENSING.md](../../../LICENSING.md).

**Attribution:** "Source: Australian Energy Market Operator (AEMO), 2026
Integrated System Plan PLEXOS model (Step Change), © AEMO, used under
AEMO's copyright permissions; converted to gtopt format."

AEMO's notices say that the package had confidential data removed.  They
also say that AEMO gives no warranty on the model and that the model may
not reproduce AEMO's published outcomes.

## What is converted

| ISP / PLEXOS | gtopt |
|---|---|
| `Node` (15 sub-regions) | `Bus` |
| `Node.Load` → `Traces\demand\<SUB>_RefYear_5000_STEP_CHANGE_POE10_OPSO_MODELLING_PVLITE.csv` | `Demand.lmax` (hourly mean of the half-hours) |
| `Generator` with `Units > 0` on 2027-07-19 (540 of 1,194; candidates, network-augmentation pseudo-units and load subtracters skipped) | `Generator`: `pmax = Units × (Rating trace or timesliced Rating, else Max Capacity) × Rating Factor × (1 − Aux Incr)`; `gcost = Heat Rate × Fuel Price (dated) + VO&M` |
| `Battery` with `Units > 0` (100 of 432) | `Battery`: `Capacity × Units`, Max/Min SoC, charge/discharge efficiency, power = window maximum of `Max Power`; SoC 50 % at start and end |
| `Line` Max/Min Flow, rows set by season timeslice (`<STATE> Hot Day / Typical Summer / Winter`) and date | `Line.tmax_ab` / `tmax_ba` per hour |
| `Storage` (ML → hm³), `Waterway` (Max Flow), generator `Head/Tail Storage` + `Efficiency Incr` (MW per m³/s), `Natural Inflow` traces (m³/s) | `Reservoir` (end ≥ start), `Junction` (drain allowed), `Waterway`, `Turbine`, `Flow` |
| `Max Energy Day` (DSP, GWh); `Max Energy Year` (hydro units with no storage, GWh) | daily-sum `UserConstraint` |
| `Region.VoLL` | `demand_fail_cost` = 36,356 |

Timeslices come from three sources:

- `M1`..`M12`;
- the `Summer` / `Not Summer` month patterns;
- `Traces\timeslice\timeslice_RefYear5000.csv`, which gives state changes
  per day.

All traces are the AEMO "RefYear5000" stitched rolling-reference-year
series of the Step Change scenario.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/australia/production_cost/isp2026_sc_2027w29/case
OUT=~/gtopt-cases-out/australia/production_cost/isp2026_sc_2027w29
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/isp2026_sc_2027w29.json" --set input_directory="$C" -d . --solver clp
```

- No profile; the case reads its Parquet schedules from `case/`.
- Solver: any LP solver works (`gtopt --solvers` lists them); the command
  above uses CLP.
- Expected resources: **small** — a ~144k-row LP; a few minutes with CLP
  and well under 1 GB of RAM.

### Rebuild `case/` from `source/`

With gtopt 1.1.0 or later:

```bash
xz -dk "source/2026 ISP Step Change Model.xml.xz"
python -m plexos2gtopt.aemo_isp "source/2026 ISP Step Change Model.xml" \
  -t source/traces -s 2027-07-19 -d 7 -o case -n isp2026_sc_2027w29
```

This rebuild reproduces the JSON and every Parquet file exactly.

## Limitations

- **No expansion.**  The candidate builds (`Max Units Built`, `Build Cost`,
  `WACC`, `Economic Life`), retirement and the REZ transmission
  augmentation pseudo-generators are not used.  The fleet is the one in
  service on the first day.
- **No PLEXOS constraints.**  None of the 590 `Constraint` objects is
  converted.  That covers REZ export and import limits, transmission group
  limits, renewable and emission policy, gas-offtake limits and system
  strength.
- **Network.**  Transport model over the ISP notional flow paths.  No losses
  (the PLEXOS quadratic loss and MLF data are not converted) and no
  marginal loss factors on units.
- **Units.**  No forced or planned outages, no minimum stable levels, no
  unit commitment.
- **Hydro.**  Pumping is not modelled: pumped-hydro units only generate from
  their upper storage.  End volume is at least the start volume, and there
  are no water values.
- **Not modelled:** purchasers (electrolyser loads), DSP bid bands, reserves
  and emission prices.
- **Not validated against AEMO.**  The public package contains no PLEXOS
  solution.

## Provenance

- Converter: `plexos2gtopt.aemo_isp`, gtopt revision
  `7d92e51ea` (gtopt master after the 1.1.0 release); in gtopt 1.1.0 or later.
- Archive hashes, converter arguments and file checksums:
  `case/isp2026_sc_2027w29.provenance.json` and
  [`catalog.json`](../../../catalog.json).
