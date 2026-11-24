# Morales-España and Tejada-Arango (2019) — clustered unit commitment

> [!WARNING]
> Provided **AS IS**, not validated by the authors of the paper or of the
> data, who keep all rights over the data.  See the
> [disclaimer](../../../DISCLAIMER.md).

> [!NOTE]
> **Converter in progress.**  The gtopt converter for these data,
> `cucdata2gtopt`, is being written (gtopt branch `feat/cucdata2gtopt`)
> and is not in gtopt master yet.  The cases below are recipes whose
> conversion step will work once it is merged.

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
