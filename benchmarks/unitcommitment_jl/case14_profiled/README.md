# case14_profiled — IEEE 14-bus unit commitment with profiled renewables (UnitCommitment.jl test fixture)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by Argonne National Laboratory or the UnitCommitment.jl developers
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../DISCLAIMER.md).

The UnitCommitment.jl test fixture `case14-profiled.json.gz`: case14 plus two profiled (time-varying) renewable units.
UnitCommitment.jl (Argonne National Laboratory) extends the MATPOWER
IEEE systems with unit-commitment data (cost curves, ramps, minimum
up/down times, start-up costs, reserves, contingencies).  Converted with
gtopt's `ucjl2gtopt` to a gtopt **unit-commitment MIP** (binary
commitment, `--mip`), with the network as DC power flow and the N-1
contingencies as soft line-outage (LODF) constraints.

| Field | Value |
|---|---|
| Case id | `benchmarks/unitcommitment_jl/case14_profiled` |
| Network | 14 buses, 20 lines |
| Units | 8 generators, 6 with unit commitment |
| Demands | 12 |
| Time | 4 block(s), 1 stage(s), 1 scenario(s), 4 h |
| User constraints | 324 (N-1 contingencies, interfaces) |
| LP | 1,578 rows, 1,608 cols, 4,798 nonzeros (gtopt `0794d659fc37`, `--lp-only`) |
| Method / profile | monolithic MIP, no profile (self-contained JSON) |
| Source | [`source/case14-profiled.json.gz`](source/case14-profiled.json.gz) (UnitCommitment.jl `dev`, commit `3e4fd1b6370900b4`) |
| Converter | `tools/ucjl2gtopt.py --mip` (gtopt `211c82db7`) |

## Files

- `source/case14-profiled.json.gz` — `test/fixtures/case14-profiled.json.gz` exactly as published in
  UnitCommitment.jl (gzip, as upstream).
- `case/case14_profiled.json` — the gtopt case (single self-contained JSON).

## Source and licence

| | |
|---|---|
| Data | UnitCommitment.jl test fixture `case14-profiled.json.gz` |
| Published by | UnitCommitment.jl, Argonne National Laboratory, <https://github.com/ANL-CEEESA/UnitCommitment.jl>, branch `dev`, commit `3e4fd1b6370900b4053eb04856d534dc72e37012` |
| Copyright | © 2020-2022, UChicago Argonne, LLC |
| Licence | **BSD-3-Clause** (UnitCommitment.jl `LICENSE.md`; reproduced in [`source/NOTICE.md`](source/NOTICE.md), which must accompany redistributed copies) |
| sha256 (`case14-profiled.json.gz`) | `db00c8b08a6b2aac7327ee9b80ede0db3ae9affc27354effb813a6b5c5db8a73` |

The fixture is part of the UnitCommitment.jl repository and so covered
by its licence.  It derives from MATPOWER data (IEEE test systems of the
University of Washington archive).  UnitCommitment.jl's benchmark
library (the 365-day instances on its website) is **not** included:
those files are distributed outside the licensed repository.

**Citation.**  UnitCommitment.jl asks users to cite it:
A. S. Xavier, A. M. Kazachkov, O. Yurdakul, J. He and F. Qiu,
*UnitCommitment.jl: A Julia/JuMP Optimization Package for Security-Constrained
Unit Commitment (Version 0.4)* (software), Zenodo, 2024, doi:
[10.5281/zenodo.4269874](https://doi.org/10.5281/zenodo.4269874).

Suggested attribution: *"UnitCommitment.jl test fixture case14-profiled.json.gz (© 2020-2022 UChicago Argonne, LLC; BSD-3-Clause); converted to gtopt by the gtopt authors."*

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/unitcommitment_jl/case14_profiled/case
OUT=~/gtopt-cases-out/benchmarks/unitcommitment_jl/case14_profiled
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/unitcommitment_jl/case14_profiled/case/case14_profiled.json" --set input_directory="$C" -d . --solver highs
```

- Self-contained case: no profile.
- MIP (unit commitment): use a MIP-capable solver (HiGHS, CBC, CPLEX, Gurobi, …), never CLP.
- Expected resources: small MIP; seconds, < 1 GB RAM.

### Rebuild `case/` from `source/`

```bash
GTOPT_SRC=<gtopt checkout> tools/get_case.py rebuild case14_profiled --out /tmp/case14_profiled
# or by hand:
gunzip -k source/case14-profiled.json.gz
python3 <gtopt checkout>/tools/ucjl2gtopt.py source/case14-profiled.json --mip -o case/case14_profiled.json
```

Without `--mip` the converter writes the LP relaxation of the commitment.

## Limitations

- A test fixture: short horizon, synthetic extensions of an IEEE system.
- Converter mapping (cost curves to piecewise segments, reserves, soft
  N-1 constraints with LODF coefficients below 0.10 dropped) is gtopt's;
  objective values are not directly comparable with UnitCommitment.jl's.
