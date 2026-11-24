# nrel118_2024w01 — NREL-118 extended IEEE 118-bus system, first week (hourly)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by NREL or the authors of the NREL-118 data
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../DISCLAIMER.md).

**Recipe only: nothing of this case is redistributed here.**  The
upstream data have no licence, so this folder holds only this README
(and, where needed, a sha256 manifest); `tools/get_case.py fetch` downloads
the pinned upstream files, checks their sha256 and converts them on your
machine into the git-ignored `source/` and `case/`.

The **NREL-118** test system of Peña, Martinez-Anido and Hodge (2018):
the IEEE 118-bus network extended with a modern generation fleet (327
units, high wind and solar share) and a year of hourly load and
renewable profiles.  This case is the **first week** (168 hourly blocks
in 7 daily stages) as an LP economic dispatch over the full 118-bus DC
network, built by gtopt's `nrel118_to_gtopt` with its default options
(no unit commitment, NREL-Sienna fuel prices).

| Field | Value |
|---|---|
| Case id | `benchmarks/nrel/nrel118_2024w01` |
| Network | 118 buses, 186 lines |
| Units | 327 generators |
| Demands | 91 |
| Time | 168 block(s), 7 stage(s), 1 scenario(s), 168 h |
| LP | 54,096 rows, 124,152 cols, 263,088 nonzeros (gtopt `0794d659fc37`, `--lp-only`) |
| Method / profile | monolithic, no profile |
| Converter | `nrel118_to_gtopt` (gtopt `211c82db7`) |

## Source and licence

| | |
|---|---|
| Data | I. Peña, C. B. Martinez-Anido and B.-M. Hodge, "An Extended IEEE 118-Bus Test System With High Renewable Penetration," *IEEE Trans. Power Systems* 33(1), 2018, pp. 281-289, doi: [10.1109/TPWRS.2017.2695963](https://doi.org/10.1109/TPWRS.2017.2695963) |
| Files | Sienna `PowerSystemsTestData`, folder `118-Bus/`, <https://github.com/Sienna-Platform/PowerSystemsTestData>, commit `a2ecae9ff3cfe6d219744f1b10e4edd4eeecabc9`: the 125 files listed with their sha256 in [`upstream.sha256`](upstream.sha256) (~27 MB) |
| Licence | **None stated**: `PowerSystemsTestData` has no licence file, so the data are **not redistributed** here (the converted case is not either) |

Cite the paper above when you use the data.

## Get and build the case

```bash
pip install -e <gtopt checkout>/scripts     # the gtopt converters
tools/get_case.py fetch benchmarks/nrel/nrel118_2024w01
```

`fetch` runs, in effect:

```bash
# download the files of upstream.sha256 into source/ (flat), check sha256
nrel118_to_gtopt --week 1 --cache-dir source --no-download -o case/nrel118_2024w01.json
```

(`nrel118_to_gtopt` writes the time series into `case/nrel118_2024w01/`;
`get_case.py` moves them next to the JSON.)  Other windows, unit
commitment (`--commitment mip`) or block aggregation are
`nrel118_to_gtopt` options; such a case is no longer this catalogued case.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/nrel/nrel118_2024w01/case
OUT=~/gtopt-cases-out/benchmarks/nrel/nrel118_2024w01
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/nrel/nrel118_2024w01/case/nrel118_2024w01.json" --set input_directory="$C" -d .
```

- Self-contained case: no profile.
- Any LP solver plugin works (`gtopt --solvers` lists them).
- Expected resources: LP of one week, 118 buses, 327 units; seconds, < 2 GB RAM.

## Limitations

- One week of a synthetic test system; LP dispatch without unit
  commitment, ramps or reserves (the converter defaults).
- Hydro is modelled from the dataset's availability profiles, not as
  reservoirs.
- Fuel prices are the NREL-Sienna loader's defaults.
