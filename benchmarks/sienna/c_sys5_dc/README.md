# c_sys5_dc — Sienna c_sys5_dc: PJM 5-bus system with one branch as an HVDC link (no Kirchhoff row)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by NREL or the Sienna developers
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

A test system of NREL's **Sienna** PowerSimulations.jl /
PowerSystemCaseBuilder.jl, built on the PJM 5-bus system (F. Li and R. Bo,
2010) with Sienna's time series: one branch is an HVDC link, mapped to a gtopt line without reactance (no Kirchhoff row).  gtopt's
`sienna2gtopt` ports it to a gtopt LP (variant `hvdc`).

| Field | Value |
|---|---|
| Case id | `benchmarks/sienna/c_sys5_dc` |
| Network | 5 buses, 7 lines |
| Units | 5 generators |
| Demands | 3 |
| Time | 24 block(s), 1 stage(s), 1 scenario(s), 24 h |
| LP | 168 rows, 360 cols, 648 nonzeros (gtopt `0794d659fc37`, `--lp-only`) |
| Method / profile | monolithic, no profile |
| Converter | `sienna2gtopt` (gtopt `211c82db7`) |

## Source and licence

| | |
|---|---|
| Data | Sienna `PowerSystemsTestData`, `5-Bus/` (12 files) and `psy_data/data_5bus_pu.jl`, <https://github.com/Sienna-Platform/PowerSystemsTestData>, commit `a2ecae9ff3cfe6d219744f1b10e4edd4eeecabc9`; the file list and the sha256 of every file are pinned in gtopt `scripts/sienna2gtopt/_bundle.py` |
| System definitions | PowerSystemCaseBuilder.jl (BSD-3-Clause), <https://github.com/Sienna-Platform/PowerSystemCaseBuilder.jl> |
| Licence | **None stated**: `PowerSystemsTestData` has no licence file, so the data are **not redistributed** here (the converted case is not either) |

The 5-bus network is the PJM 5-bus system of F. Li and R. Bo, "Small
Test Systems for Power System Economic Studies," IEEE PES General
Meeting 2010, doi: 10.1109/PES.2010.5589973.

## Get and build the case

```bash
pip install -e <gtopt checkout>/scripts     # the gtopt converters
tools/get_case.py fetch benchmarks/sienna/c_sys5_dc
```

`fetch` runs, in effect:

```bash
sienna2gtopt hvdc -o case/c_sys5_dc.json
```

`sienna2gtopt` downloads the 13 files from the pinned commit on first
use, checks every sha256 and caches them in `~/.cache/gtopt/sienna/`
(`GTOPT_OFFLINE=1` forbids downloads; `GTOPT_SIENNA_DATA_DIR` points at a
pre-staged copy).

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/sienna/c_sys5_dc/case
OUT=~/gtopt-cases-out/benchmarks/sienna/c_sys5_dc
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/sienna/c_sys5_dc/case/c_sys5_dc.json" --set input_directory="$C" -d .
```

- Self-contained case: no profile.
- Any LP solver plugin works (`gtopt --solvers` lists them).
- Expected resources: tiny LP; well under a second.

## Limitations

- A small test fixture for one modelling feature, not a model of a
  real system.
- The port maps Sienna's formulation onto gtopt elements as the
  converter documents; objective values are not directly comparable with
  PowerSimulations.jl's.
