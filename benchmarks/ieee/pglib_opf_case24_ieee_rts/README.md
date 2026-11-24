# pglib_opf_case24_ieee_rts — IEEE Reliability Test System 1979 (24 buses) (DC OPF)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by the data authors or the PGLib-OPF maintainers
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../DISCLAIMER.md).

The IEEE Reliability Test System 1979 (24 buses) as distributed by the **IEEE PES Power Grid Library —
Optimal Power Flow** (PGLib-OPF v23.07, file `pglib_opf_case24_ieee_rts.m`), converted to a
gtopt **single-hour DC optimal power flow**: DC power flow (Kirchhoff)
constraints, the branch ratings of the source and the linear cost
coefficient of each generator.  PGLib-OPF revises the original test
system for OPF benchmarking ("typical operations" variant: generator
costs, line ratings and limits); the original system is
IEEE RTS Task Force, "IEEE Reliability Test System," IEEE Trans. PAS-98(6), 1979, pp. 2047-2054, doi:10.1109/TPAS.1979.319398.

| Field | Value |
|---|---|
| Case id | `benchmarks/ieee/pglib_opf_case24_ieee_rts` |
| Network | 24 buses, 38 lines |
| Units | 33 generators |
| Demands | 17 |
| Time | 1 block(s), 1 stage(s), 1 scenario(s), 1 h |
| LP | 39 rows, 88 cols, 204 nonzeros (gtopt `0794d659fc37`, `--lp-only`) |
| Method / profile | monolithic LP, no profile (self-contained JSON) |
| Source | [`source/pglib_opf_case24_ieee_rts.m.xz`](source/pglib_opf_case24_ieee_rts.m.xz) (PGLib-OPF v23.07, commit `dc6be4b2f85c`) |
| Converter | `pp2gtopt` (gtopt `211c82db7`), see below |

## Files

- `source/pglib_opf_case24_ieee_rts.m.xz` — `pglib_opf_case24_ieee_rts.m` exactly as published in PGLib-OPF
  v23.07, xz-compressed (sha256 of the `.m`: `5d4fc2d4a1a282f700c51747e592f5a5ac15fa6d5eadb7df7ae937bbe3063374`).
- `case/pglib_opf_case24_ieee_rts.json` — the gtopt case (single self-contained JSON).

## Source and licence

| | |
|---|---|
| Data | IEEE Reliability Test System 1979 (24 buses): IEEE RTS Task Force, "IEEE Reliability Test System," IEEE Trans. PAS-98(6), 1979, pp. 2047-2054, doi:10.1109/TPAS.1979.319398 |
| Distributed by | PGLib-OPF, <https://github.com/power-grid-lib/pglib-opf>, tag `v23.07`, commit `dc6be4b2f85ca0e776952ec22cbd4c22396ea5a3` |
| Copyright (file header) | The Institute of Electrical and Electronics Engineers (IEEE) |
| Licence | **CC BY 4.0** (<https://creativecommons.org/licenses/by/4.0/>): PGLib-OPF's data licence; the file header states the same.  Text: [`LICENSES/CC-BY-4.0.txt`](../../../LICENSES/CC-BY-4.0.txt) |
| sha256 (`.m.xz`) | `74e7fbb6254363afc8b1a5e5398b9a24e3695f1ed31529a559025158ebde45f2` |

**Changes** (as CC BY 4.0 asks): `source/` is unmodified except xz
compression; `case/` is a conversion by `pp2gtopt`: DC approximation
(no reactive power, voltages or losses) and linear costs only (the
quadratic terms of the PGLib-OPF cost curves are dropped).

**Citation.**  PGLib-OPF asks users to cite:

1. S. Babaeinejadsarookolaee et al., "The Power Grid Library for
   Benchmarking AC Optimal Power Flow Algorithms," arXiv:1908.02788,
   2019, <https://arxiv.org/abs/1908.02788>.
2. The original source of the system: IEEE RTS Task Force, "IEEE Reliability Test System," IEEE Trans. PAS-98(6), 1979, pp. 2047-2054, doi:10.1109/TPAS.1979.319398.

Suggested attribution: *"IEEE Reliability Test System 1979 (24 buses), pglib_opf_case24_ieee_rts.m from PGLib-OPF v23.07 (© 1979 The Institute of Electrical and Electronics Engineers (IEEE); CC BY 4.0); converted to gtopt by the gtopt authors (DC OPF, linear costs)."*

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/ieee/pglib_opf_case24_ieee_rts/case
OUT=~/gtopt-cases-out/benchmarks/ieee/pglib_opf_case24_ieee_rts
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/ieee/pglib_opf_case24_ieee_rts/case/pglib_opf_case24_ieee_rts.json" --set input_directory="$C" -d .
```

- Self-contained case: no profile.
- Any LP solver plugin works (`gtopt --solvers` lists them).
- Expected resources: single-hour DC OPF; well under a second, < 1 GB RAM.

### Rebuild `case/` from `source/`

```bash
tools/get_case.py rebuild pglib_opf_case24_ieee_rts --out /tmp/pglib_opf_case24_ieee_rts   # or by hand:
xz -dk source/pglib_opf_case24_ieee_rts.m.xz
pp2gtopt -f source/pglib_opf_case24_ieee_rts.m -o case/pglib_opf_case24_ieee_rts.json --solver monolithic --no-check
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
