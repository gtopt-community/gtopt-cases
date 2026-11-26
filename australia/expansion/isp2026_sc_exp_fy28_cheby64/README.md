# isp2026_sc_exp_fy28_cheby64 — Australian NEM, AEMO 2026 ISP Step Change, generation and storage expansion FY2028 (12 typical weeks, 64 Chebyshev nodes)

> [!WARNING]
> Provided **AS IS**, not validated by AEMO, which keeps all rights over
> the data.  See the [disclaimer](../../../DISCLAIMER.md).

> [!NOTE]
> **Prototype.**  A one-year expansion planning case built from the ISP
> capacity-outlook database with
> `python -m plexos2gtopt.aemo_isp_expansion --week-sampler chebyshev:64`.
> Each month is one chronological typical week sampled at 64 Chebyshev
> nodes; see [Time representation](#time-representation) and
> [Limitations](#limitations).

This case plans the generation and storage builds of the National
Electricity Market for the financial year 2027-28 (FY2028).  The source
is the **Step Change** scenario of AEMO's **2026 Integrated System Plan
(ISP)** PLEXOS model (the "DLT" capacity-outlook database), the same
database as
[`isp2026_sc_exp_fy28_3y`](../isp2026_sc_exp_fy28_3y/README.md).  The
two cases differ in the time representation: that case uses one
representative day of 24 hourly blocks per month over three years,
this one a typical week per month over one year, with storage and
ramps on a real 168-hour week.

## Time representation

- **Stages.**  One stage per calendar month, 12 stages from July 2027
  to June 2028.  Each stage is one **typical week**: the 168 hours from
  Wednesday 12:00 to the next Wednesday 12:00 (the weekend sits in the
  middle of the window) that hold the month's net-load peak.
- **Chebyshev nodes.**  The week is sampled at the Chebyshev-Gauss-
  Lobatto nodes of order 64 (`Stage.sampling = "point"`).  The week is
  periodic, so the first and last node are the same instant and each
  stage has 64 blocks (768 in total).  A block value is the trace value
  **at** the node (not a block mean), and the block duration is its
  Clenshaw-Curtis quadrature weight times `days_in_month / 7`, so
  energy, costs and the investment annuities are month totals
  (durations sum to 8,784 h, FY2028 has 29 February).  Nodes cluster
  towards the ends of the window and are about 4 h apart at its centre.
- **Storage rule `cc`.**  Batteries and reservoirs integrate their
  level between nodes with the Clenshaw-Curtis rule
  (`model_options.battery_storage_integration =
  reservoir_storage_integration = "cc"`): one balance row per node with
  the node's quadrature weight, as sparse as a block balance, so the
  weekly storage total uses the same quadrature as energy and cost.
  This is the converters' default on point stages.
- **Method.**  The sampling follows Matus, Cáceres, Puschel-Lovengreen
  and Moreno, "Chebyshev based continuous time power system operation
  approach", IEEE PES GM 2015, DOI
  [10.1109/PESGM.2015.7286570](https://doi.org/10.1109/PESGM.2015.7286570).
  The GTOpt method note,
  [typical-week sampling](https://github.com/gtopt-community/gtopt/blob/master/docs/methods/typical-week-sampling.md),
  describes the samplers, the storage rules and a comparison of this
  year at several node counts against an hourly week.

## Model

- **Existing fleet.**  Every month is converted from the weekly
  dispatch model with a window equal to the whole month.  Commissioning,
  dated retirements, dated line limits, fuel prices and traces follow
  the month; the profiles of the typical week are cut from the traces.
- **Candidates.**  Every generator or battery with `Units = 0` and
  `Max Units Built > 0` in FY2028: new-entrant REZ and ODR solar and
  wind, gas, storage, and the network-augmentation pseudo-units (REZ
  transmission, DNSP voltage and system strength).  Builds happen at the
  start of the financial year.  The annualised cost is
  `Build Cost · CRF(WACC, Economic Life) + FO&M`.  Batteries expand on a
  power axis and an energy axis linked by their `energy_power_ratio`.
- **Constraints.**  The capacity and build limits (`RHS Year` in MW)
  become stage-scope user constraints on the installed capacity, with a
  slack cost of 1e7 $/MW (`--capacity-penalty 1e7`).  Operational
  constraints keep their per-block RHS, and daily energy limits become
  stage energy sums.
- **Storage.**  Batteries close their cycle within each typical week.
  Hydro reservoir volumes are a state coupled across the 12 months and
  end free at the horizon.  Pondages, the upper reservoirs of pumped
  hydro and storages with a PLEXOS `Target Week` or `End Effects Method`
  = Recycle cycle within the week.

| Field | Value |
|---|---|
| Case id | `australia/expansion/isp2026_sc_exp_fy28_cheby64` |
| Horizon | 2027-07-01 to 2028-06-30: 12 monthly stages × 64 Chebyshev nodes of one typical week (768 blocks, durations = quadrature weights scaled to the month), 1 scenario, 1 phase; no fill year |
| Network | 15 sub-regional buses, 18 notional inter-sub-regional flow paths with dated limits; transport model, lossless |
| Existing fleet | 626 generators in total (existing and candidate).  Maximum existing capability over the year: coal 20,017 MW, gas 11,084 MW, hydro 8,271 MW, liquid fuel 539 MW, wind 15,225 MW, utility solar plus rooftop PV 38,634 MW, DSP 514 MW |
| Candidates | 80: 45 energy (REZ / ODR / DREZ solar and wind, gas), 24 network augmentations, 11 battery types |
| Storage | 138 batteries (127 existing, 11 candidates); 22 hydro reservoirs (15 cycled within the week, 7 coupled across months), 36 waterways, 95 turbines, 11 pumps, 13 inflow series |
| Demand | 15 sub-regional loads (219.4 TWh in FY2028; peak node value 33,071 MW; POE10 operational sent-out traces) plus 11 flexible pump loads |
| Constraints | 178 user constraints (capacity / build limits, REZ and transmission-group limits per block, daily energy sums), 8 decision variables |
| LP | one LP: 932,417 rows, 1,320,403 columns, 3,046,077 non-zeros |
| Method / profile | monolithic LP, no profile; discount rate 7 % (ISP `Discount Rate`); storage rule `cc` |
| Converter | `python -m plexos2gtopt.aemo_isp_expansion --first-fy 2028 --years 1 --fill-years 0 --capacity-penalty 1e7 --week-sampler chebyshev:64` (revision used: `8f34712be789`) |

## Files

- `case/isp2026_sc_exp_fy28_cheby64.json`: the gtopt planning.
- `case/Battery/{emin,emax}.parquet`,
  `case/Demand/lmax.parquet`, `case/Flow/discharge.parquet`,
  `case/Generator/{pmax,gcost}.parquet`,
  `case/GeneratorProfile/profile.parquet`,
  `case/Line/{tmax_ab,tmax_ba}.parquet`,
  `case/UserConstraint/rhs.parquet`: schedules in long format
  (`[scenario,] stage, block, uid, value`).
- `case/isp2026_sc_exp_fy28_cheby64.stats.json`: converter statistics
  (constraint groups converted or skipped, candidate categories,
  installed capacity of every existing unit per month, the window start
  of each typical week) and the converter command and revision.
- `case/isp2026_sc_exp_fy28_cheby64.provenance.json`: archive hashes,
  converter revision and arguments.
- `source/2026 ISP Step Change Model.xml.xz`: the scenario database,
  unchanged, xz-compressed (the same file as in
  `isp2026_sc_exp_fy28_3y/source/`).
- `source/NOT_KEPT.txt`: what was downloaded but is not kept here.  The
  trace files are not redistributed: the case reads one year of several
  hundred half-hourly traces.

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
excluded.  This folder redistributes AEMO material (the scenario XML)
and derived data under that permission.  See
[LICENSING.md](../../../LICENSING.md).

**Attribution:** "Source: Australian Energy Market Operator (AEMO), 2026
Integrated System Plan PLEXOS model (Step Change), © AEMO, used under
AEMO's copyright permissions; converted to gtopt format."

AEMO's notices say that the package had confidential data removed.  They
also say that AEMO gives no warranty on the model and that the model may
not reproduce AEMO's published outcomes.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/australia/expansion/isp2026_sc_exp_fy28_cheby64/case
OUT=~/gtopt-cases-out/australia/expansion/isp2026_sc_exp_fy28_cheby64
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/isp2026_sc_exp_fy28_cheby64.json" --set input_directory="$C" -d . \
  --solver highs
```

- No profile; the case reads its Parquet schedules from `case/`.
- Needs a GTOpt build from master of 26 November 2026 or later (newer
  than the 1.2.0 release): point-sampled stages and the `cc` storage
  rule.
- Solver: any LP solver works (`gtopt --solvers` lists them).
- Expected resources: **medium** — 0.9 M rows and 1.3 M columns; about
  2 GB of RAM.

### Reference result (HiGHS)

Solved once with HiGHS 1.16.0 (default LP settings, `--solver highs`),
GTOpt master of 26 November 2026, on an 18-core shared virtual machine
while other jobs were running, so the times are indicative only:

| Item | Value |
|---|---|
| Status | optimal |
| Objective | 4,079,392,300 $ (4.0794e9) |
| LP | 932,417 rows, 1,320,403 columns, 3,046,077 non-zeros |
| Simplex iterations | 706,181 |
| LP build | 382 s |
| Solve | 1,564 s |
| Peak memory | 1.7 GB |

For comparison, the same year converted with 168 hourly blocks per
typical week (`--week-sampler uniform:1`, 3.46 M columns, 2.44 M rows)
has objective 4.1176e9 with HiGHS: the 64-node week is 0.93 % below
it with about 38 % of its columns (method note, §7a).

### Rebuild `case/`

Download the five archives listed above from the AEMO ISP page and
extract them.  The trace folder layout the converter expects is the one
of the archives: `Traces/demand` and `Traces/rooftop PV` inside the
scenario folder of the model archive, and the `solar`, `wind`, `hydro`
and `timeslice` folders of the trace archives (pass each root with
`-t`).  From a directory that holds the extracted archives and this
case's `source/`:

```bash
xz -dk "source/2026 ISP Step Change Model.xml.xz"
python -m plexos2gtopt.aemo_isp_expansion \
  "source/2026 ISP Step Change Model.xml" \
  -t "2026 ISP Model/2026 ISP Step Change" -t "2026 ISP Solar traces" \
  -t "2026 ISP Wind traces" -t hydro -t "2026 ISP Timeslice traces" \
  --first-fy 2028 --years 1 --fill-years 0 --capacity-penalty 1e7 \
  --week-sampler chebyshev:64 -o case -n isp2026_sc_exp_fy28_cheby64
```

(`hydro` is the folder extracted from `2026 ISP Hydro traces.zip`.)
The storage rule is the converter default on point stages
(`--point-storage-integration cc`) and the week window its default
(`--week-start wed:12`, `--week-rule peak`).  Other node counts:
`--week-sampler chebyshev:N`; the hourly week: `--week-sampler
uniform:1`.  With the converter revision listed above, this rebuild
reproduces the JSON and every Parquet file exactly.

## Limitations

- **Typical weeks.**  One week per month, chosen by the month's
  net-load peak and scaled to the month: no chronology across weeks,
  so monthly energy is the typical week's energy times `days / 7`, and
  storage cycles within the week (batteries) or carries a monthly state
  (7 reservoirs).
- **Chebyshev sampling.**  The 64 nodes sample the week at instants,
  about 4 h apart at its centre, so short ramps and intra-day battery
  cycling between nodes are only approximate.  Against the same year
  with 168 hourly blocks per week the objective is about 1 % lower (see
  the reference result).  Provisional: the method note is the reference
  for its accuracy.
- **Expansion scope.**  Generation, battery and REZ / network
  augmentation candidates are decisions.  Inter-regional transmission
  (the ISP CDP augmentations) is an input, and retirements are dated
  inputs, not decisions.  One year with no fill year: the investment
  annuities of FY2028 builds are charged for that year only.
- **Long-period targets.**  Yearly energy targets (VRET and other policy
  targets) are not enforced across months; emission budgets are not
  modelled.  Purchasers and hydrogen demand are not converted.
- **Capacity limits.**  The ISP yearly capacity and build limits are
  stage-scope user constraints; the existing fleet is folded into the
  RHS as its FY-mean installed capacity.  The onboarding / connection
  limits (`OCLimit_*`) keep their PLEXOS Penalty Price and are soft;
  the other yearly limits are soft at 1e7 $/MW.  The existing fleet
  already exceeds some of the `OCLimit_*` limits (the excess is in
  `UserConstraint/slack_sol`, as PLEXOS would pay it too).
- **Network.**  Transport model over the ISP notional flow paths, no
  losses, no marginal loss factors.
- **Battery self-discharge.**  The case sets no battery
  `annual_standing_loss`, so GTOpt applies its default of 4 %/month to
  all 138 batteries.
- **Units.**  No outages, no unit commitment, no reserves.
- **Not validated against AEMO.**  The public package contains no PLEXOS
  solution.

## Provenance

- Converter: `plexos2gtopt.aemo_isp_expansion`, GTOpt revision
  `8f34712be789`; flags above.
- Archive hashes, converter arguments and file checksums:
  `case/isp2026_sc_exp_fy28_cheby64.provenance.json` and
  [`catalog.json`](../../../catalog.json).
