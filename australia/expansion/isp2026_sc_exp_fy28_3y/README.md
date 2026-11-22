# isp2026_sc_exp_fy28_3y — Australian NEM, AEMO 2026 ISP Step Change, generation and storage expansion FY2028-FY2030 (monthly representative days)

> [!WARNING]
> Provided **AS IS**, not validated by AEMO, which keeps all rights over
> the data.  See the [disclaimer](../../../DISCLAIMER.md).

> [!NOTE]
> **Prototype.**  A multi-year expansion planning case built from the ISP
> capacity-outlook database with
> `python -m plexos2gtopt.aemo_isp_expansion` (default flags).  Each month
> is one representative day; see [Limitations](#limitations).

This case plans the generation and storage builds of the National
Electricity Market for the financial years 2027-28, 2028-29 and 2029-30
(FY2028-FY2030), plus one unreported fill year (FY2031) that damps the
end effect.  The source is the **Step Change** scenario of AEMO's **2026
Integrated System Plan (ISP)** PLEXOS model (the "DLT" capacity-outlook
database).

- **Time.**  One stage per calendar month, 48 stages from July 2027 to
  June 2031.  Each stage is one representative day of 24 hour-of-day
  blocks.  A block value is the month mean of that hour, and its
  duration is the number of days in the month, so energy, costs and
  reservoir balances are exact monthly totals.
- **Existing fleet.**  Every month is converted from the weekly
  dispatch model with a window equal to the whole month.  Commissioning,
  dated retirements, dated line limits, fuel prices and traces therefore
  follow the month.
- **Candidates.**  Every generator or battery with `Units = 0` and
  `Max Units Built > 0` in the horizon.  This covers new-entrant REZ and
  ODR solar and wind, DREZ, gas and storage, and the network-augmentation
  pseudo-units (REZ transmission, DNSP voltage and system strength).
  Builds happen at the start of each financial year (`expmod` from
  `Max Units Built`).  The annualised cost is
  `Build Cost · CRF(WACC, Economic Life) + FO&M`.  Batteries expand on a
  power axis and an energy axis linked by their `energy_power_ratio`.
- **Constraints.**  The capacity and build limits (`RHS Year` in MW)
  become stage-scope user constraints on the installed capacity, active
  in their years.  Operational constraints keep their per-block RHS
  (hour-of-day mean), and daily energy limits become stage energy sums.
- **Storage.**  Batteries close a daily cycle within each representative
  day.  Hydro reservoir volumes are a state coupled across all 48 months
  and end free at the horizon.  Pondages, the upper reservoirs of pumped
  hydro and storages with a PLEXOS `Target Week` or `End Effects Method`
  = Recycle cycle within each day.

| Field | Value |
|---|---|
| Case id | `australia/expansion/isp2026_sc_exp_fy28_3y` |
| Horizon | 2027-07-01 to 2031-06-30: 48 monthly stages × 24 hour-of-day blocks (1,152 blocks, durations = days of the month), 1 scenario, 1 phase; FY2031 is a fill year |
| Network | 15 sub-regional buses, 18 notional inter-sub-regional flow paths with dated limits; transport model, lossless |
| Existing fleet | 765 generators in total (existing and candidate).  Maximum existing capability over the horizon: coal 20,017 MW, gas 11,711 MW, hydro 10,807 MW, liquid fuel 539 MW, wind 14,156 MW, utility solar plus rooftop PV 41,912 MW, DSP 581 MW |
| Candidates | 204: 118 energy (REZ / ODR / DREZ solar and wind, gas), 52 network augmentations, 34 battery types |
| Storage | 223 batteries (189 existing, 34 candidates); 22 hydro reservoirs (15 cycled within the day, 7 coupled across months), 42 waterways, 101 turbines, 17 pumps, 13 inflow series |
| Demand | 15 sub-regional loads (219 / 226 / 236 TWh in FY2028 / FY2029 / FY2030, 246 TWh in the fill year; peak monthly hour-of-day mean 34,699 MW; POE10 operational sent-out traces) plus 17 flexible pump loads |
| Constraints | 352 user constraints (capacity / build limits per year, REZ and transmission-group limits per block, daily energy sums), 8 decision variables |
| LP | one LP: 1,681,763 rows, 2,660,630 columns, 6,105,878 non-zeros |
| Method / profile | monolithic LP, no profile; discount rate 7 % (ISP `Discount Rate`) |
| Converter | `python -m plexos2gtopt.aemo_isp_expansion`, default flags (revision used: `a8c270a91037`) |

## Files

- `case/isp2026_sc_exp_fy28_3y.json`: the gtopt planning.
- `case/Battery/{emin,emax}.parquet`,
  `case/Demand/lmax.parquet`, `case/Flow/discharge.parquet`,
  `case/Generator/{pmax,gcost}.parquet`,
  `case/GeneratorProfile/profile.parquet`,
  `case/Line/{tmax_ab,tmax_ba}.parquet`,
  `case/UserConstraint/rhs.parquet`: schedules in long format
  (`[scenario,] stage, block, uid, value`).
- `case/isp2026_sc_exp_fy28_3y.stats.json`: converter statistics (constraint
  groups converted or skipped, candidate categories, installed capacity
  of every existing unit per month).
- `case/isp2026_sc_exp_fy28_3y.provenance.json`: archive hashes, converter
  revision and arguments.
- `source/2026 ISP Step Change Model.xml.xz`: the scenario database,
  unchanged, xz-compressed.
- `source/NOT_KEPT.txt`: what was downloaded but is not kept here.  The
  trace files are not redistributed: the case reads four years of
  several hundred half-hourly traces.

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
C=$REPO/australia/expansion/isp2026_sc_exp_fy28_3y/case
OUT=~/gtopt-cases-out/australia/expansion/isp2026_sc_exp_fy28_3y
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/isp2026_sc_exp_fy28_3y.json" --set input_directory="$C" -d . \
  --solver highs
```

- No profile; the case reads its Parquet schedules from `case/`.
- Needs gtopt with battery power expansion, user-constraint
  `active_stages` and pump loads that enter service during the horizon
  (not yet in a gtopt release).
- Solver: any LP solver works (`gtopt --solvers` lists them).  A barrier
  method (`--set solver_options.algorithm=barrier` with CPLEX or HiGHS) is the
  practical choice at this size.
- Expected resources: **medium** — 1.7 M rows and 2.7 M columns; a few
  GB of RAM.

### Rebuild `case/`

Download the five archives listed above from the AEMO ISP page and
extract them.  The trace folder layout the converter expects is the one
of the archives: `Traces/demand` inside the model folder, and the
`solar`, `wind`, `hydro` and `timeslice` folders of the trace archives
(pass each root with `-t`).  Then:

```bash
xz -dk "source/2026 ISP Step Change Model.xml.xz"
python -m plexos2gtopt.aemo_isp_expansion \
  "source/2026 ISP Step Change Model.xml" \
  -t <model folder> -t <solar traces> -t <wind traces> -t <hydro> \
  -t <timeslice traces> -o case -n isp2026_sc_exp_fy28_3y
```

With the converter revision listed above, this rebuild reproduces the
JSON and every Parquet file exactly.

## Limitations

- **Representative days.**  One day per month: no chronology across days
  within a month, so multi-day storage (weekly hydro cycling, long
  battery durations) is only approximate.  Batteries close their cycle
  within each day.
- **Expansion scope.**  Generation, battery and REZ / network
  augmentation candidates are decisions.  Inter-regional transmission
  (the ISP CDP augmentations) is an input, and retirements are dated
  inputs, not decisions.
- **Long-period targets.**  Yearly energy targets (VRET and other policy
  targets) are not enforced across months; emission budgets are not
  modelled.  Purchasers and hydrogen demand are not converted.
- **Capacity limits.**  The ISP yearly capacity and build limits are
  stage-scope user constraints enforced at each FY's first month; the
  existing fleet is folded into the RHS as its FY-mean installed
  capacity (units commissioned during the year count pro rata).  The
  PLEXOS Penalty Price is kept: the onboarding / connection limits
  (`OCLimit_*`, 5e5 to 1e6 $/MW) are soft, and the existing fleet
  already exceeds some of them (the excess is in
  `UserConstraint/slack_sol`, as PLEXOS would pay it too).
- **Network.**  Transport model over the ISP notional flow paths, no
  losses, no marginal loss factors.
- **Battery self-discharge.**  The case sets no battery `annual_loss`, so
  gtopt applies its default of 4 %/month to all 223 batteries (and adds
  the battery power-envelope rows); run with
  `--set model_options.battery_annual_loss=0` for lossless storage.
- **Units.**  No outages, no unit commitment, no reserves.
- **Not validated against AEMO.**  The public package contains no PLEXOS
  solution.

## Provenance

- Converter: `plexos2gtopt.aemo_isp_expansion` (default flags), gtopt
  revision `a8c270a91037`.
- Archive hashes, converter arguments and file checksums:
  `case/isp2026_sc_exp_fy28_3y.provenance.json` and
  [`catalog.json`](../../../catalog.json).
