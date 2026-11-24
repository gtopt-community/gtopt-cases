# ieee118 — Clustered unit commitment case study: Modified IEEE 118-bus system (Morales-España and Tejada-Arango, 2019)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by the authors of the paper
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../../DISCLAIMER.md).

**Recipe only: nothing of this case is redistributed here.**  The
upstream data have no licence, so this folder holds only this README
(and, where needed, a sha256 manifest); `tools/get_case.py fetch` downloads
the pinned upstream files, checks their sha256 and converts them on your
machine into the git-ignored `source/` and `case/`.

One of the two case studies of **G. Morales-España and D. A.
Tejada-Arango, "Modeling the Hidden Flexibility of Clustered Unit
Commitment," IEEE Trans. Power Systems 34(4), 2019**, published by the
authors in the `CUC-data` repository: the Modified IEEE 118-bus system with
clustered (integer) unit commitment.  The paper's own model is the GAMS
code `StarGenLite_Clustered-UC.gms` of the same repository.  See the
[paper folder README](../README.md).

| Field | Value |
|---|---|
| Case id | `benchmarks/papers/morales_espana_2019_cuc/ieee118` |
| Size | 118 buses, 540 units with commitment, 24 hourly blocks, 3780 user constraints |
| Method / profile | monolithic, no profile |
| Converter | `cucdata2gtopt --system 118 --reserve 5` |

## Source and licence

| | |
|---|---|
| Data | `CUC_IEEE118-busSystem.xlsx`, <https://github.com/datejada/CUC-data>, commit `624abbbdc9f83095c02b34174e52c76f77ddfa36` |
| sha256 | `f4e87590261a80c45c29a9ea2fa759f4c9cc92a3256c07fa89d603a52034f2a3` (145,652 bytes) |
| Licence | **None stated**: the `CUC-data` repository has no licence file, so the data are **not redistributed** here (the converted case is not either) |

Cite the paper (doi:
[10.1109/TPWRS.2019.2908051](https://doi.org/10.1109/TPWRS.2019.2908051);
preprint [arXiv:1811.02622](https://arxiv.org/abs/1811.02622)).

## Get and build the case

```bash
pip install -e <gtopt checkout>/scripts     # the gtopt converters
tools/get_case.py fetch benchmarks/papers/morales_espana_2019_cuc/ieee118
```

`fetch` downloads `CUC_IEEE118-busSystem.xlsx` into `source/`, checks its sha256 and
runs, in effect:

```bash
cucdata2gtopt --system 118 --reserve 5 --input source/CUC_IEEE118-busSystem.xlsx -o case/
```

and saves the planning JSON as `case/cuc_ieee118.json`.  `--reserve 5`
is the paper's 5 % up / down reserve case; the converter's other
defaults are the paper formulation (the GAMS start-up / shut-down
capability and reserve-coupled ramps as user constraints) and an
individual-unit commitment of the clustered units on one chronological
stage (`cucdata2gtopt --help`).

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/papers/morales_espana_2019_cuc/ieee118/case
OUT=~/gtopt-cases-out/benchmarks/papers/morales_espana_2019_cuc/ieee118
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/papers/morales_espana_2019_cuc/ieee118/case/cuc_ieee118.json" --set input_directory="$C" -d . --mip-gap 1e-4
```

- Self-contained case: no profile.
- MIP (unit commitment): use a MIP-capable solver (CPLEX, Gurobi, HiGHS, CBC, …; add `--solver <name>`), never CLP.
- Expected resources: individual-unit UC MIP; about 12 min with CPLEX (6 threads, 10⁻³ gap), 40–60 min at 10⁻⁴; HiGHS is much slower.

## Limitations

- Any figures quoted from the paper are the paper's own results, obtained
  with the authors' GAMS model, not gtopt results.
