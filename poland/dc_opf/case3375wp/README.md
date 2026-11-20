# case3375wp — Polish system, winter 2007-08 evening peak (DC OPF)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case was
> built with gtopt's own conversion tools and verified only as far as the
> gtopt authors can; it has **not** been validated by the author of the
> original data or by the MATPOWER developers and comes **with no
> warranty**.  It must **never** be used as a reference for analysing the
> operation of the Polish power system or for financial analysis.  All
> rights to the original data belong to their authors.  See
> [DISCLAIMER.md](../../../DISCLAIMER.md).

The MATPOWER test case `case3375wp`: the Polish 400, 220 and 110 kV
transmission network during the winter 2007-08 evening peak, including
equivalents of the German, Czech and Slovak networks.  It is a
**single-hour snapshot** (one block), converted to a gtopt DC optimal power
flow with Kirchhoff (DC power flow) constraints and the branch ratings of
the source.  A good large-network, small-LP case.

| Field | Value |
|---|---|
| Case id | `poland/dc_opf/case3375wp` |
| Snapshot | winter 2007-08 evening peak (1 block of 1 h, 1 stage, 1 scenario) |
| Network | 3374 buses, 4161 branches (lines, transformers, 2 phase shifters, 4 impedance branches) |
| Units | 489 generators: 479 in-service MATPOWER units + 10 fixed injections (buses with negative load) |
| Demand | 2414 loads, 52,099.2 MW |
| LP (`--lp-only`) | 4,162 rows, 7,064 cols (gtopt development revision `8cfe33d44`) |
| Method / profile | monolithic LP, no profile (self-contained JSON) |
| Source | [`source/case3375wp.m.xz`](source/case3375wp.m.xz) (MATPOWER 8.1, sha256 of the `.m`: `f814bc31845cfbfb…`) |
| Converter | `pp2gtopt` from gtopt; rebuild with gtopt master of November 2026 or later (MATPOWER-fidelity fixes listed below; development revision used: `catalog.json`) |

## Files

- `source/case3375wp.m.xz` — the MATPOWER case file `data/case3375wp.m`
  exactly as distributed with MATPOWER 8.1, xz-compressed.
- `case/case3375wp.json` — the gtopt case (single self-contained JSON).
- `case/case3375wp.provenance.json` — source URL, commit, hashes, converter
  revision and command.

## Source and licence

| | |
|---|---|
| Original author | **Roman Korab**, Silesian University of Technology (Politechnika Śląska), Gliwice, Poland |
| Title | `case3375wp` — "Power flow data for Polish system - winter 2007-08 evening peak" |
| Year | data 2007-08; added to MATPOWER in 2011 (MATPOWER 4.1); phase-shifter sign corrected 2018-10-16 |
| Distributed by | MATPOWER, <https://matpower.org>, <https://github.com/MATPOWER/matpower> |
| Exact file | [`data/case3375wp.m`](https://github.com/MATPOWER/matpower/blob/1a828c7af590714499284e36ee9c81273388c594/data/case3375wp.m) at tag `8.1`, commit `1a828c7af590714499284e36ee9c81273388c594` (file last changed in `a187db15d1aa`, 2018-10-08) |
| sha256 (`.m`) | `f814bc31845cfbfb7754610f3c9b496a2dfd5eb3f86601ff8be015c21653722f` |
| sha256 (`.m.xz`) | `43c306dba9594d33efa5557e1395a2c33b896791562a28a79718ba6b086de20d` |
| Licence | **No explicit licence.**  MATPOWER's code is under the 3-clause BSD licence, but MATPOWER's `LICENSE` states: *"The MATPOWER case files distributed with MATPOWER are not covered by the BSD license.  In most cases, the data has either been included with permission or has been converted from data available from a public source."*  The file header states: *"This data was graciously provided by, and is distributed with the permission of, Roman Korab"*. |

**Terms that apply.**  The data are redistributed here, unchanged and in
the same form MATPOWER publishes them openly on GitHub, for research,
education, software testing and benchmarking, with full attribution, under
the permission granted by the author for distribution with MATPOWER.  No
additional licence is granted by this repository (see
[LICENSING.md](../../../LICENSING.md)).  If you are the rights holder and
object to this redistribution, please open an issue and the files will be
removed.

**Citation request.**  MATPOWER's `CITATION` file asks that all
publications derived from the use of MATPOWER *or the included data files*
cite the MATPOWER paper; for the Polish data please also credit Roman Korab
and, for the history of the Polish cases, the TPEC 2022 paper:

1. R. D. Zimmerman, C. E. Murillo-Sánchez and R. J. Thomas, "MATPOWER:
   Steady-State Operations, Planning, and Analysis Tools for Power Systems
   Research and Education," *IEEE Transactions on Power Systems*, vol. 26,
   no. 1, pp. 12-19, Feb. 2011,
   doi: [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168).
2. R. D. Zimmerman and C. E. Murillo-Sánchez, *MATPOWER (Version 8.1)*
   [Software], 2025, doi:
   [10.5281/zenodo.15871662](https://doi.org/10.5281/zenodo.15871662).
3. Data: R. Korab, Silesian University of Technology, `case3375wp.m`,
   distributed with MATPOWER.
4. J. Snodgrass, S. Kunkolienkar, U. Habiba, Y. Liu, M. Stevens,
   F. Safdarian, T. Overbye and R. Korab, "Case Study of Enhancing the
   MATPOWER Polish Electric Grid," *2022 IEEE Texas Power and Energy
   Conference (TPEC)*, College Station, TX, 2022,
   doi: [10.1109/TPEC54980.2022.9750807](https://doi.org/10.1109/TPEC54980.2022.9750807)
   (describes the origin of the MATPOWER Polish cases; its enhanced data
   set is `case2746wop`, not this case).

Suggested attribution: *"Polish system winter 2007-08 evening peak
(`case3375wp`), data by R. Korab (Silesian University of Technology),
distributed with MATPOWER 8.1 [1, 2]; converted to gtopt by the gtopt
authors (changes listed in the README)."*

**Derived work.**  `case/case3375wp.json` is a derivative of the source
file, distributed under the same terms as the source data (no additional
licence; attribution as above).  The gtopt tools used to produce it are
licensed AGPL-3.0-or-later (with the GTOpt Solver Plugin Exception) or
under the GTOpt Commercial License, see
[LICENSING.md](../../../LICENSING.md); that licence does not extend to the
case data.  Any rights the gtopt authors hold in the conversion layer are
dedicated under CC0-1.0, without granting any right in the source data.
Everything is provided AS IS: see
[DISCLAIMER.md](../../../DISCLAIMER.md).

### Changes made by the conversion

- AC power-flow data dropped: reactive power, voltages, shunts (`Gs`,
  `Bs`), line charging, resistances (the DC model is lossless), branch
  ratings B/C and angle limits.
- Out-of-service generators (117 of 596, `status = 0`) and their costs are
  omitted.  Generator `Pmin`/`Pmax` are kept (5 units have `Pmin < 0`).
- Costs: MATPOWER polynomial `gencost` (model 2, `c2 = 0`) → linear
  `gcost = c1` [$/MWh]; the constant term `c0` is dropped.
- Buses with negative real load (`Pd < 0`, 10 buses, 3,736.2 MW in total)
  become fixed generators (`pmin = pmax = −Pd`, zero cost).
- Branches: reactance on the 100 MVA base; transformer ratio → `tap_ratio`
  (effective reactance `x·τ`); the 2 phase shifters (+3° in MATPOWER,
  from bus 10135 to 10134) are written as `phase_shift_deg = −3` on the
  reversed orientation 10134 → 10135 (same physics); `rateA = 0`
  (unlimited) → 9,999 MW.  Per-bus generation limits and costs, and
  per-branch susceptance, rating and shift were checked to match the `.m`
  file.
- Unserved demand is allowed at `demand_fail_cost = 1000` $/MWh;
  `scale_objective = 1000`.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/poland/dc_opf/case3375wp/case
OUT=~/gtopt-cases-out/poland/dc_opf/case3375wp
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/case3375wp.json" --set input_directory="$C" -d .
```

- Self-contained case: no profile, no external input files.
- Solver: gtopt picks the best available plugin (`--solver highs|clp|…`);
  `gtopt --solvers` lists them.  Any LP solver works.
- Expected resources: **small** — a ~4k-row LP; seconds and well under
  1 GB of RAM.

### Rebuild `case/` from `source/`

```bash
xz -dk source/case3375wp.m.xz
pp2gtopt -f source/case3375wp.m -o case/case3375wp.json \
    --solver monolithic --no-check
```

`pp2gtopt` reads MATPOWER `.m` files through pandapower; install the
`matpower` extra of the gtopt scripts (`pip install -e "scripts[matpower]"`,
which brings `matpowercaseframes`).  The case was produced with a gtopt
development revision (`8cfe33d44`) whose `pp2gtopt` includes the
MATPOWER-fidelity fixes, as does gtopt master of November 2026 or later: skip out-of-service units/branches, keep pandapower static
generators (`sgen`, every MATPOWER generator after the first on a bus) and
negative-reactance and `impedance` branches, use the series reactance
`x = √(vk² − vkr²)` of transformers instead of `|z|`, undo pandapower's
phase-shifter sign flip, and write reactances in per unit (no
`voltage: 10`, which pushed 47 low-impedance branches below gtopt's 1e-6
p.u. reactance floor and dropped their Kirchhoff rows).  A `pp2gtopt`
without these fixes produces a **different** (incomplete) case.

## Limitations

- **Single snapshot.**  MATPOWER provides only this one operating point
  (winter 2007-08 evening peak): there are no load or renewable time
  series, no unit-commitment data (minimum up/down times, start-up costs)
  and no ramp limits, so this is a one-hour DC OPF, not a daily or annual
  scheduling case.
- DC (lossless) approximation of an AC power-flow case; results differ from
  an AC OPF.
- Generator costs are the linear MATPOWER coefficients, not market data.

## Building the full case yourself

The source has no time series, so there is no longer horizon to build from
it alone.  If you have hourly load / generation profiles for the Polish
system from another source, the time-series mode of `pp2gtopt` (gtopt
master of November 2026 or later) turns this network into one
multi-block case:

```bash
# profiles.csv: one row per hour; columns e.g. load@all (system MW),
# load@bus:<n> (MW at MATPOWER bus n), gen:<name> (MW or p.u.)
pp2gtopt --matpower source/case3375wp.m --profiles profiles.csv \
    --hours 0:168 --stage-hours 24 -o case3375wp_week.json   # one week
pp2gtopt --matpower source/case3375wp.m --profiles profiles.csv \
    --stage-hours 24 -o case3375wp_year.json                 # full year
gtopt case3375wp_week.json
```

Such a case is no longer this catalogued case; document the origin and
licence of the profiles you add.
