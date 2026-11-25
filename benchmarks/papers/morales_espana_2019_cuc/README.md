# Morales-España and Tejada-Arango (2019) — clustered unit commitment

> [!WARNING]
> Provided **AS IS**, not validated by the authors of the paper or of the
> data, who keep all rights over the data.  See the
> [disclaimer](../../../DISCLAIMER.md).

G. Morales-España and D. A. Tejada-Arango, "Modeling the Hidden
Flexibility of Clustered Unit Commitment," *IEEE Transactions on Power
Systems*, vol. 34, no. 4, pp. 3294-3296, July 2019, doi:
[10.1109/TPWRS.2019.2908051](https://doi.org/10.1109/TPWRS.2019.2908051)
(preprint [arXiv:1811.02622](https://arxiv.org/abs/1811.02622)).

The paper shows that clustered (integer) unit-commitment formulations hide
flexibility unless the start-up/shut-down and ramping constraints of the
clustered units are formulated tightly, and tests its formulation on two
case studies that the authors publish in
[`datejada/CUC-data`](https://github.com/datejada/CUC-data) (Excel
workbooks read by their GAMS model `StarGenLite_Clustered-UC.gms`, plus
an addendum PDF).

| Case | System | Source workbook | In this repository |
|---|---|---|---|
| [ieee39](ieee39/README.md) | Modified New England IEEE 39-bus system | `CUC_IEEE39-busSystem.xlsx` | recipe only |
| [ieee118](ieee118/README.md) | Modified IEEE 118-bus system | `CUC_IEEE118-busSystem.xlsx` | recipe only |

**Licence.**  The `CUC-data` repository states no licence, so neither the
workbooks nor the cases converted from them are redistributed here:
`tools/get_case.py fetch` downloads the workbook of the pinned commit
`624abbbdc9f83095c02b34174e52c76f77ddfa36`, checks its sha256 and
converts it locally.

## Comparing with the paper

gtopt reproduces the GAMS model the authors published
(`StarGenLite_Clustered-UC.gms`), but its individual-unit UC costs come
out 0.8–2.6 % below Table I of the paper:

| Case | Reserve | Paper [M EUR] | Published GAMS model / gtopt [M EUR] | Difference |
|---|---|---|---|---|
| ieee39 | 10 % | 1.0070 | 0.980823 | −2.60 % |
| ieee39 | 5 % | 0.9901 | 0.977186 | −1.30 % |
| ieee118 | 5 % | 14.4787 | 14.253323 | −1.56 % |
| ieee118 | 2.5 % | 13.9725 | 13.861865 | −0.79 % |

The difference is not a missing constraint, the solver tolerance or the
data:

- gtopt's optimum satisfies an independent transcription of the
  published GAMS model and has the same objective (to the cent for
  ieee39, and on ieee118 at 2.5 %).
- The paper solved to 10⁻⁴ % (ieee39) and 0.01 % (ieee118) relative
  gap, so its values are optima.
- The paper's own clustered relaxation (0.9998 / 0.9826 M EUR for
  ieee39) already costs more than the exact individual-unit optimum of
  the published model, so the extra cost sits in a term that every
  model of Table I shares.
- The only change to the upstream data (2018-10-24) rescaled the
  reserve column and removed a ±1 % cost noise on ieee118; solving with
  the earlier costs does not move the result towards the paper.

The gap behaves like a reserve price: divided by the total reserve
requirement of each case it is 4.6–4.7 EUR/MWh in all four cases,
while the published GAMS prices reserve at below 0.1 EUR/MW.  The model
behind Table I evidently priced reserve differently, but its formula
cannot be recovered from the published material, so the converter keeps
the published model.  Details in the gtopt
[`cucdata2gtopt` documentation](https://github.com/gtopt-community/gtopt/blob/master/docs/scripts/cucdata2gtopt.md).
