# pglib_opf_case118_ieee — IEEE 118-bus test case (DC OPF)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by the data authors or the PGLib-OPF maintainers
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../DISCLAIMER.md).

The IEEE 118-bus test case as distributed by the **IEEE PES Power Grid Library —
Optimal Power Flow** (PGLib-OPF v23.07, file `pglib_opf_case118_ieee.m`), converted to a
gtopt **single-hour DC optimal power flow**: DC power flow (Kirchhoff)
constraints, the branch ratings of the source and the linear cost
coefficient of each generator.  PGLib-OPF revises the original test
system for OPF benchmarking ("typical operations" variant: generator
costs, line ratings and limits); the original system is
University of Washington Power Systems Test Case Archive (ieee118cdf.txt), IEEE Common Data Format, 1962 AEP system.

| Field | Value |
|---|---|
| Case id | `benchmarks/ieee/pglib_opf_case118_ieee` |
| Network | 118 buses, 186 lines |
| Units | 54 generators |
| Demands | 99 |
| Time | 1 block(s), 1 stage(s), 1 scenario(s), 1 h |
| LP | 187 rows, 339 cols, 1,021 nonzeros (gtopt `0794d659fc37`, `--lp-only`) |
| Method / profile | monolithic LP, no profile (self-contained JSON) |
| Source | [`source/pglib_opf_case118_ieee.m.xz`](source/pglib_opf_case118_ieee.m.xz) (PGLib-OPF v23.07, commit `dc6be4b2f85c`) |
| Converter | `pp2gtopt` (gtopt `211c82db7`), see below |

## Files

- `source/pglib_opf_case118_ieee.m.xz` — `pglib_opf_case118_ieee.m` exactly as published in PGLib-OPF
  v23.07, xz-compressed (sha256 of the `.m`: `b1af0833849040c04babc3700631cff0d9afa66b79c5d3e13ae79bdf516cec78`).
- `case/pglib_opf_case118_ieee.json` — the gtopt case (single self-contained JSON).

## Source and licence

| | |
|---|---|
| Data | IEEE 118-bus test case: University of Washington Power Systems Test Case Archive (ieee118cdf.txt), IEEE Common Data Format, 1962 AEP system |
| Distributed by | PGLib-OPF, <https://github.com/power-grid-lib/pglib-opf>, tag `v23.07`, commit `dc6be4b2f85ca0e776952ec22cbd4c22396ea5a3` |
| Copyright (file header) | Richard D. Christie, University of Washington Electrical Engineering |
| Licence | **CC BY 4.0** (<https://creativecommons.org/licenses/by/4.0/>): PGLib-OPF's data licence; the file header states the same.  Text: [`LICENSES/CC-BY-4.0.txt`](../../../LICENSES/CC-BY-4.0.txt) |
| sha256 (`.m.xz`) | `5203a227657544190caf63302eefeae234340064e097912ba8425a283b57b383` |

**Changes** (as CC BY 4.0 asks): `source/` is unmodified except xz
compression; `case/` is a conversion by `pp2gtopt`: DC approximation
(no reactive power, voltages or losses) and linear costs only (the
quadratic terms of the PGLib-OPF cost curves are dropped).

**Citation.**  PGLib-OPF asks users to cite:

1. S. Babaeinejadsarookolaee et al., "The Power Grid Library for
   Benchmarking AC Optimal Power Flow Algorithms," arXiv:1908.02788,
   2019, <https://arxiv.org/abs/1908.02788>.
2. The original source of the system: University of Washington Power Systems Test Case Archive (ieee118cdf.txt), IEEE Common Data Format, 1962 AEP system.

Suggested attribution: *"IEEE 118-bus test case, pglib_opf_case118_ieee.m from PGLib-OPF v23.07 (© 1999 Richard D. Christie, University of Washington Electrical Engineering; CC BY 4.0); converted to gtopt by the gtopt authors (DC OPF, linear costs)."*

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/ieee/pglib_opf_case118_ieee/case
OUT=~/gtopt-cases-out/benchmarks/ieee/pglib_opf_case118_ieee
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/ieee/pglib_opf_case118_ieee/case/pglib_opf_case118_ieee.json" --set input_directory="$C" -d .
```

- Self-contained case: no profile.
- Any LP solver plugin works (`gtopt --solvers` lists them).
- Expected resources: single-hour DC OPF; well under a second, < 1 GB RAM.

### Rebuild `case/` from `source/`

```bash
tools/get_case.py rebuild pglib_opf_case118_ieee --out /tmp/pglib_opf_case118_ieee   # or by hand:
xz -dk source/pglib_opf_case118_ieee.m.xz
pp2gtopt -f source/pglib_opf_case118_ieee.m -o case/pglib_opf_case118_ieee.json --solver monolithic --no-check
```

`pp2gtopt` reads MATPOWER `.m` files through pandapower; install the
`matpower` extra of the gtopt scripts (`pip install -e "scripts[matpower]"`).
The committed case was built with gtopt `211c82db7`
(pandapower 3.5.6, matpowercaseframes 2.1.1).

## Limitations

- **Single snapshot**: one hour, no time series, no unit-commitment or
  ramp data.  `pp2gtopt --profiles` can turn the network into a
  multi-hour case if you bring your own profiles (document their origin).
- DC (lossless) approximation of an AC OPF benchmark: results differ from
  the AC OPF figures PGLib-OPF publishes.
- Linear costs only (quadratic terms dropped).
