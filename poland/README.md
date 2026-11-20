# Poland — Polish transmission system

> [!WARNING]
> **Provided AS IS — not validated by the data authors.**  These cases
> were built with gtopt's own conversion tools and verified only as far as
> the authors can; they have **not** been validated by the authors or
> distributors of the source data and come **with no warranty**.  They
> must **never** be used as a reference for analysing official operation
> scheduling or for financial analysis.  All rights to the original data
> belong to their authors.  See [DISCLAIMER.md](../DISCLAIMER.md).

Cases of the Polish power system built from the Polish test systems
distributed with **[MATPOWER](https://matpower.org)**, with data prepared
by **Roman Korab** (Silesian University of Technology).

| Application | Folder | Source | Converter |
|---|---|---|---|
| DC OPF snapshot | [dc_opf/case3375wp](dc_opf/case3375wp/README.md) | MATPOWER 8.1 `case3375wp.m`: winter 2007-08 evening peak, 3374 buses | `pp2gtopt` |

The source is a single-hour snapshot: MATPOWER publishes no time series,
unit-commitment or ramp data for it.  With hourly load and renewable
profiles from another source, `pp2gtopt --profiles` builds the full
one-week or one-year case from the same network (see the case README,
"Building the full case yourself").

## Provenance and rights

* **Data author: Roman Korab**, Silesian University of Technology;
  distributed with MATPOWER *"with the permission of Roman Korab"*.
  This repository claims no ownership of the data (see
  [DISCLAIMER.md](../DISCLAIMER.md)).
* **No explicit licence**: MATPOWER's BSD-3-Clause licence does **not**
  cover its case files.  The `.m` file is redistributed unchanged
  (xz-compressed in `source/`), with attribution, and will be removed on
  request of the rights holder.
* Cite MATPOWER (R. D. Zimmerman, C. E. Murillo-Sánchez, R. J. Thomas,
  IEEE Trans. Power Systems 26(1), 2011,
  doi: [10.1109/TPWRS.2010.2051168](https://doi.org/10.1109/TPWRS.2010.2051168))
  and credit R. Korab for the Polish data; see
  [`../THIRD_PARTY_DATA.md`](../THIRD_PARTY_DATA.md) for the full
  attribution.
* Converter, gtopt revision and file hashes:
  [`catalog.json`](../catalog.json).
