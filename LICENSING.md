# Licensing

This repository holds third-party data and a thin layer added by the gtopt
authors; they are under different terms.

- **`source/`**: third-party data, redistributed as published and
  unmodified except for xz compression and, for large files, splitting
  into numbered parts (the AEMO trace files are also cut to the rows of
  the case week).  **No licence is granted** by this repository.  The
  exceptions are benchmark data published under an open licence
  (`benchmarks/`: PGLib-OPF files under CC BY 4.0, UnitCommitment.jl
  fixtures under BSD-3-Clause), which you receive under that licence from
  their authors, not from this repository.
- **`case/`**: derived from that data by the gtopt conversion tools; the
  cases remain subject to the rights and terms of the publishers.
- **Rights holders**: Australian Energy Market Operator (AEMO),
  Australia; Coordinador Eléctrico Nacional (CEN), Chile;
  Administrador del Mercado Mayorista (AMM), Guatemala; Ente Operador
  Regional (EOR), Central America; SEM Committee (CRU, Ireland, and
  Utility Regulator, Northern Ireland; data not redistributed here,
  fetched on demand); Comité de Operación Económica del
  Sistema Interconectado Nacional (COES), Peru; Roman Korab, Silesian
  University of Technology, whose data are distributed by MATPOWER; for
  `benchmarks/`, the authors named in each PGLib-OPF file (IEEE,
  University of Washington) and UChicago Argonne, LLC (UnitCommitment.jl),
  and, for the recipe-only benchmarks whose data are not redistributed,
  NREL / Alliance for Sustainable Energy (Sienna PowerSystemsTestData)
  and G. Morales-España and D. A. Tejada-Arango (CUC-data).
  Sources, terms and the attribution to give:
  [`THIRD_PARTY_DATA.md`](THIRD_PARTY_DATA.md).
- **Conversion layer**: to the extent the gtopt authors hold any rights in
  what they add (the file layout, `profiles/`, line lifts, solver
  parameter files, `catalog.json`, the READMEs, `NOTICE.md` files and
  other documentation and metadata), they dedicate those rights to the
  public domain under **CC0-1.0**
  ([`LICENSES/CC0-1.0.txt`](LICENSES/CC0-1.0.txt)).  This dedication
  grants no right in the third-party data.
- **Tools** (`tools/`, `.githooks/`): the gtopt licence,
  AGPL-3.0-or-later with the GTOpt Solver Plugin Exception, or the GTOpt
  Commercial License.

This statement is not legal advice.  Everything is provided **AS IS**,
without warranty of any kind; see [`DISCLAIMER.md`](DISCLAIMER.md).

| Part | Terms | SPDX |
|---|---|---|
| `**/source/**` | third-party data, no licence granted | `LicenseRef-third-party-no-licence` |
| `**/case/**` | third-party rights; CC0-1.0 for the conversion layer only | `LicenseRef-third-party-no-licence AND CC0-1.0` |
| `benchmarks/ieee/**/source/**` | PGLib-OPF data, CC BY 4.0 from their authors | `CC-BY-4.0` |
| `benchmarks/ieee/**/case/**` | adapted PGLib-OPF data (CC BY 4.0); CC0-1.0 for the conversion layer | `CC-BY-4.0 AND CC0-1.0` |
| `benchmarks/unitcommitment_jl/**/source/**` | UnitCommitment.jl fixtures, BSD-3-Clause from UChicago Argonne, LLC | `BSD-3-Clause` |
| `benchmarks/unitcommitment_jl/**/case/**` | converted fixtures (BSD-3-Clause); CC0-1.0 for the conversion layer | `BSD-3-Clause AND CC0-1.0` |
| `tools/`, `.githooks/` | gtopt dual licence | `AGPL-3.0-or-later OR LicenseRef-gtopt-commercial` |
| `profiles/`, `catalog.json`, line lifts, documentation, repository metadata | CC0-1.0 | `CC0-1.0` |

The per-file annotations are in [`REUSE.toml`](REUSE.toml); the licence
texts are in [`LICENSES/`](LICENSES/).  Each `source/` and `case/`
directory also carries a `NOTICE.md` with its origin and rights holder,
and every `catalog.json` entry has a `terms` object.

## Tools: dual licence

You may use the tools under **either** of:

1. the **GNU Affero General Public License v3.0 or later**
   ([`LICENSES/AGPL-3.0-or-later.txt`](LICENSES/AGPL-3.0-or-later.txt))
   together with the **GTOpt Solver Plugin Exception**
   ([`LICENSES/LicenseRef-gtopt-solver-plugin-exception.md`](LICENSES/LicenseRef-gtopt-solver-plugin-exception.md));
   or
2. the **GTOpt Commercial License**
   ([`LICENSES/LicenseRef-gtopt-commercial.md`](LICENSES/LicenseRef-gtopt-commercial.md)).

Source files carry the SPDX identifier

```
SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-gtopt-commercial
```

See the gtopt repository's
[`LICENSING.md`](https://github.com/gtopt-community/gtopt/blob/master/LICENSING.md)
for the full explanation of the dual licence.

## Third-party data

The third-party data (`source/`) and the cases derived from it (`case/`)
are **not** licensed by this repository (benchmark data under an open
licence keep that licence, granted by their authors): see the statement above,
[`THIRD_PARTY_DATA.md`](THIRD_PARTY_DATA.md) and
[`LICENSES/LicenseRef-third-party-no-licence.txt`](LICENSES/LicenseRef-third-party-no-licence.txt).
Read [`DISCLAIMER.md`](DISCLAIMER.md) before using any case.

## Removal requests

If you are a rights holder and object to the redistribution of any
material here, e-mail <marcelomatusacuna@gmail.com> with the subject
**"gtopt-cases removal request"**; for non-confidential requests you may
instead open an issue with the
[data removal form](https://github.com/gtopt-community/gtopt-cases/issues/new?template=data-removal.yml).
We acknowledge each request within 5 working days and remove the material
from `main` promptly.  When required, we also rewrite the git history and
ask GitHub Support to purge cached views; the maintainers bypass the
main-branch protection ruleset only for that purpose.
