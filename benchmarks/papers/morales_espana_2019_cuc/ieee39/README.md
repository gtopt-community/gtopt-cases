# ieee39 — Clustered unit commitment case study: Modified New England IEEE 39-bus system (Morales-España and Tejada-Arango, 2019)

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  This case is
> built with gtopt's own conversion tools and checked only as far as the
> gtopt authors can; it has **not** been validated by the authors of the paper
> and comes **with no warranty**.  It is a benchmark / test system, not a
> model of any real power system's operation, and must **never** be used
> as a reference for operational or financial analysis.  All rights to the
> original data belong to their authors.  See
> [DISCLAIMER.md](../../../../DISCLAIMER.md).

> [!NOTE]
> **Converter in progress.**  `cucdata2gtopt` is being written in gtopt
> (branch `feat/cucdata2gtopt`) and is not in gtopt master yet; the
> command line below is provisional and `tools/get_case.py fetch` stops at
> the conversion step until it is merged.

**Recipe only: nothing of this case is redistributed here.**  The
upstream data have no licence, so this folder holds only this README
(and, where needed, a sha256 manifest); `tools/get_case.py fetch` downloads
the pinned upstream files, checks their sha256 and converts them on your
machine into the git-ignored `source/` and `case/`.

One of the two case studies of **G. Morales-España and D. A.
Tejada-Arango, "Modeling the Hidden Flexibility of Clustered Unit
Commitment," IEEE Trans. Power Systems 34(4), 2019**, published by the
authors in the `CUC-data` repository: the Modified New England IEEE 39-bus system with
clustered (integer) unit commitment.  The paper's own model is the GAMS
code `StarGenLite_Clustered-UC.gms` of the same repository.  See the
[paper folder README](../README.md).

| Field | Value |
|---|---|
| Case id | `benchmarks/papers/morales_espana_2019_cuc/ieee39` |
| Size | recorded in `catalog.json` once the case can be built |
| Method / profile | monolithic, no profile |
| Converter | `cucdata2gtopt` (in progress) |

## Source and licence

| | |
|---|---|
| Data | `CUC_IEEE39-busSystem.xlsx`, <https://github.com/datejada/CUC-data>, commit `624abbbdc9f83095c02b34174e52c76f77ddfa36` |
| sha256 | `665c1cdb4776beff0acc19e0ab6808896294006e469c5a57583ffefe6ef89514` (76,923 bytes) |
| Licence | **None stated**: the `CUC-data` repository has no licence file, so the data are **not redistributed** here (the converted case is not either) |

Cite the paper (doi:
[10.1109/TPWRS.2019.2908051](https://doi.org/10.1109/TPWRS.2019.2908051);
preprint [arXiv:1811.02622](https://arxiv.org/abs/1811.02622)).

## Get and build the case

```bash
pip install -e <gtopt checkout>/scripts     # the gtopt converters
tools/get_case.py fetch benchmarks/papers/morales_espana_2019_cuc/ieee39
```

`fetch` downloads `CUC_IEEE39-busSystem.xlsx` into `source/`, checks its sha256 and
runs (provisional command line):

```bash
cucdata2gtopt source/CUC_IEEE39-busSystem.xlsx -o case/cuc_ieee39.json
```

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/benchmarks/papers/morales_espana_2019_cuc/ieee39/case
OUT=~/gtopt-cases-out/benchmarks/papers/morales_espana_2019_cuc/ieee39
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$REPO/benchmarks/papers/morales_espana_2019_cuc/ieee39/case/cuc_ieee39.json" --set input_directory="$C" -d . --solver highs
```

- Self-contained case: no profile.
- MIP (unit commitment): use a MIP-capable solver (HiGHS, CBC, CPLEX, Gurobi, …), never CLP.
- Expected resources: unit-commitment MIP; size to be recorded once the converter is merged.

## Limitations

- The gtopt conversion is not available yet (see the note above).
- Any figures quoted from the paper are the paper's own results, obtained
  with the authors' GAMS model, not gtopt results.
