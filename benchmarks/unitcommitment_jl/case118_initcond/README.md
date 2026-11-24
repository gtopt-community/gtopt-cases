# case118_initcond — IEEE 118-bus unit commitment with initial conditions (UnitCommitment.jl test fixture)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by Argonne National Laboratory or the UnitCommitment.jl developers
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../DISCLAIMER.md).

The UnitCommitment.jl test fixture `case118-initcond.json.gz`: 36 hourly periods; 54 thermal units with initial status, reserves and N-1 contingencies.
UnitCommitment.jl (Argonne National Laboratory) extends the MATPOWER
IEEE systems with unit-commitment data (cost curves, ramps, minimum
up/down times, start-up costs, reserves, contingencies).  Converted with
gtopt's `ucjl2gtopt` to a gtopt **unit-commitment MIP** (binary
commitment, `--mip`), with the network as DC power flow and the N-1
contingencies as soft line-outage (LODF) constraints.

| Field | Value |
|---|---|
| Case id | `benchmarks/unitcommitment_jl/case118_initcond` |
| Network | 118 buses, 186 lines |
| Units | 54 generators, 54 with unit commitment |
| Demands | 99 |
| Time | 36 block(s), 1 stage(s), 1 scenario(s), 36 h |
| User constraints | 4,844 (N-1 contingencies, interfaces) |
| LP | 208,766 rows, 205,956 cols, 655,218 nonzeros (gtopt `0794d659fc37`, `--lp-only`) |
| Method / profile | monolithic MIP, no profile (self-contained JSON) |
| Source | [`source/case118-initcond.json.gz`](source/case118-initcond.json.gz) (UnitCommitment.jl `dev`, commit `3e4fd1b6370900b4`) |
| Converter | `tools/ucjl2gtopt.py --mip` (gtopt `211c82db7`) |

## Files

- `source/case118-initcond.json.gz` — `test/fixtures/case118-initcond.json.gz` exactly as published in
  UnitCommitment.jl (gzip, as upstream).
- `case/case118_initcond.json` — the gtopt case (single self-contained JSON).

## Source and licence

| | |
|---|---|
| Data | UnitCommitment.jl test fixture `case118-initcond.json.gz` |
| Published by | UnitCommitment.jl, Argonne National Laboratory, <https://github.com/ANL-CEEESA/UnitCommitment.jl>, branch `dev`, commit `3e4fd1b6370900b4053eb04856d534dc72e37012` |
| Copyright | © 2020-2022, UChicago Argonne, LLC |
| Licence | **BSD-3-Clause** (UnitCommitment.jl `LICENSE.md`; reproduced in [`source/NOTICE.md`](source/NOTICE.md), which must accompany redistributed copies) |
| sha256 (`case118-initcond.json.gz`) | `503cf688e079ba00a4869d8841aa84e120a2241a6e86da04b35d9e623a237eea` |

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

Suggested attribution: *"UnitCommitment.jl test fixture case118-initcond.json.gz (© 2020-2022 UChicago Argonne, LLC; BSD-3-Clause); converted to gtopt by the gtopt authors."*

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/unitcommitment_jl/case118_initcond/case
OUT=~/gtopt-cases-out/benchmarks/unitcommitment_jl/case118_initcond
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/unitcommitment_jl/case118_initcond/case/case118_initcond.json" --set input_directory="$C" -d . --solver highs
```

- Self-contained case: no profile.
- MIP (unit commitment): use a MIP-capable solver (HiGHS, CBC, CPLEX, Gurobi, …), never CLP.
- Expected resources: MIP with ~54x36 commitment binaries and N-1 contingency rows; minutes with HiGHS, < 2 GB RAM.

### Rebuild `case/` from `source/`

```bash
GTOPT_SRC=<gtopt checkout> tools/get_case.py rebuild case118_initcond --out /tmp/case118_initcond
# or by hand:
gunzip -k source/case118-initcond.json.gz
python3 <gtopt checkout>/tools/ucjl2gtopt.py source/case118-initcond.json --mip -o case/case118_initcond.json
```

Without `--mip` the converter writes the LP relaxation of the commitment.

## Limitations

- A test fixture: short horizon, synthetic extensions of an IEEE system.
- Converter mapping (cost curves to piecewise segments, reserves, soft
  N-1 constraints with LODF coefficients below 0.10 dropped) is gtopt's;
  objective values are not directly comparable with UnitCommitment.jl's.
