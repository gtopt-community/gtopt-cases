# sem_2025w29 — Irish Single Electricity Market, one week of July 2025 (unit commitment)

> [!WARNING]
> Provided **AS IS**, not validated by the SEM Committee, the CRU, the
> Utility Regulator or NERA.  See the [disclaimer](../../../DISCLAIMER.md).

> [!IMPORTANT]
> **Recipe only: no SEM data here.**  This folder holds no source data and
> no converted case.  `tools/get_case.py fetch sem_2025w29` downloads the
> public files from the SEM Committee and builds the case on your machine
> (see [Why the data are not here](#why-the-data-are-not-here)).
> Requires gtopt 1.1.0 or later.

One week (Monday 14 to Sunday 20 July 2025, 168 hourly blocks) of the
**SEM PLEXOS Forecast Model 2024-2032**, the public validation model of
the all-island Single Electricity Market (Ireland and Northern Ireland)
published by the SEM Committee in March 2025 (SEM-25-010).  The PLEXOS
model *"Opt A2 24-32 (Avail, No Uplift, No Wheeling)--MIP"* is resolved
for that week and weather sample 1 by `plexos2gtopt --plexos-model` and
converted into a mixed-integer unit-commitment and dispatch problem on a
three-node transport network (SEM, Great Britain, France).

This is the summer week of four seasonal weeks of 2025 (`sem_2025w03`,
`w16`, `w29` and `w42`) built from the same archives; see the [Ireland
README](../../README.md).  The four weeks share the download cache, so the
archives are fetched once.

| Field | Value |
|---|---|
| Case id | `ireland/unit_commitment/sem_2025w29` |
| Horizon | 2025-07-14 to 2025-07-20: 168 blocks of 1 h, 1 stage, 1 scenario |
| Network | 3 buses (`SEM`, `BETTA` = Great Britain, `France`); 3 HVDC interconnectors SEM–GB in service (East-West, Moyle, Greenlink); transport model, lossless |
| Units | 116 generators (incl. GB and France price-bid generators and 5 demand-side bid bands); 65 unit commitments (min up/down, start costs, ramps) |
| Storage | 24 batteries: 23 grid batteries plus Turlough Hill pumped storage as one battery |
| Demand | 3 loads: SEM (all-island demand, weather sample 1, minus fixed embedded generation); GB and France flat |
| Constraints | 4 daily hydro energy limits (Ardnacrusha, Erne, Lee, Liffey) |
| LP / MIP | 105,724 rows, 94,608 cols, 336,223 nonzeros, 10,920 binaries |
| Method / profile | monolithic MIP, no profile (self-contained JSON) |
| Converter | `plexos2gtopt --plexos-model`, gtopt 1.1.0 or later (revision used: `7d92e51ea`) |

## Source

| | |
|---|---|
| Publisher | SEM Committee (Commission for Regulation of Utilities (CRU), Ireland, and Utility Regulator (UR), Northern Ireland) |
| Publication | SEM-25-010, *"SEM PLEXOS Model Validation 2024-2032 and Backcast Report"*, 24 March 2025, <https://www.semcommittee.com/publications/sem-25-010-sem-plexos-model-validation-2024-2032-and-backcast-report> |
| Model author | NERA Economic Consulting, for the CRU and the UR; PLEXOS is a product of Energy Exemplar |
| Files used | `SEM PLEXOS Forecast Model 2024-2032( Public Version).zip` (the XML) and `(CSV Files 1 of 2).zip`, `(CSV Files 2 of 2).zip` (6 demand / wind / solar Data Files); URLs, sizes, sha256 and member names in [`catalog.json`](../../../catalog.json) |

Cite: SEM Committee, *SEM PLEXOS Model Validation 2024-2032 and Backcast
Report*, SEM-25-010, 24 March 2025; model by NERA Economic Consulting.

## Why the data are not here

The publication page and the archives state no licence, and the SEM
Committee site has no terms of its own.  The CRU's terms have no reuse
clause; the Utility Regulator's terms restrict reuse of its site content
to personal, non-commercial use without prior written permission; the
NERA report in the same publication carries a NERA copyright notice.  So
redistribution of the model, or of cases derived from it, needs the
publishers' written permission (CRU, <info@cru.ie>).  Until then this
repository only describes how to fetch and convert the public files.

## Get and convert

With the gtopt Python tools of gtopt 1.1.0 or later installed
(`pip install -e <gtopt>/scripts`):

```bash
tools/get_case.py fetch sem_2025w29
```

This downloads the three archives into `$GTOPT_CASES_CACHE` (default
`~/.cache/gtopt-cases`, outside the repository), checks their sha256,
extracts the XML and the 6 CSVs into `source/`, runs `plexos2gtopt` with
the flags in `catalog.json` and writes `case/sem_2025w29.json` (the
converter's `options.solver_options.param_file` is removed so the JSON is
self-contained).  `source/` and `case/` are git-ignored.  Use `--out DIR`
to write the case elsewhere.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/ireland/unit_commitment/sem_2025w29/case
OUT=~/gtopt-cases-out/ireland/unit_commitment/sem_2025w29
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/sem_2025w29.json" --set input_directory="$C" -d . \
    --solver highs --mip-gap 0.001
```

- Solver: any MIP solver plugin (`--solver highs|cbc|…`; `gtopt
  --solvers` lists them).  Add `--no-mip` for the LP relaxation.
- **Use a tight MIP gap (0.1 %).**  The SEM value of lost load is
  500 €/MWh (from the PLEXOS model), so several hundred MWh of unserved
  energy cost less than 1 % of the weekly objective: at a 1 % gap the
  solver may stop at a commitment that leaves load unserved and sets
  prices at 500 €/MWh.  At 0.1 % no load is shed.  Check the unserved
  energy of the solution if you change the gap.
- Expected resources: **small** — a ~106k-row MIP with 11k binaries;
  minutes with HiGHS or CBC at a 0.1 % gap, under 1 GB of RAM.

## Limitations

- **One week, one weather sample, deterministic.**  PLEXOS runs the model
  over 2024–2032 with five weather samples and random outages; this case
  is one week of sample 1 with scheduled outages only.
- **Public version.**  NERA removed VO&M costs, mark-ups and battery
  cycling limits from the public model.
- **Neighbours as bids.**  GB and France are single nodes with a flat load
  and a price-bid generator, as in PLEXOS; France is not connected in
  July 2025.
- **Not converted:** forced outages, marginal loss factors and line
  losses, battery charging fees, yearly hours-of-operation limits, line
  ramp limits, uplift and price cap / floor, and the trading-day offset
  (PLEXOS days start at 23:00; block *k* is trading-day period *k*).
  `case/sem_2025w29.plexos_model.json` lists every unconverted property.
