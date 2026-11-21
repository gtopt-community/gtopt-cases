# Guatemala — daily scheduling (PSR NCP → gtopt)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

Multi-bus DC OPF of the Guatemalan SNI converted with `sddp2gtopt` from the
PSR NCP `.dat` collection (the AMM's economic-dispatch model, with costs):
single stage over the dispatch horizon, one block per hour.  About 830
buses, 955 lines, 220 generators and 240 demand nodes.

| Case | Content | Blocks | Economics |
|---|---|---:|---|
| [ncp_pdd_2026-06-22](ncp_pdd_2026-06-22) | daily program PDD 22-Jun-2026 (`PDD_DIARIO`) | 168 | thermal merit costs, per-plant water values, inflow-limited run-of-river, Mexico import cap 200 MW, terminal FutureCost |
| [ncp_week_2026-06-21](ncp_week_2026-06-21) | weekly NCP dispatch 21–27 Jun 2026 (short-term weekly program) | 168 | thermal merit costs, import cap (no water-value file shipped) |

The weekly case is a short-term (one-week) dispatch; it is kept here
because it has the same hourly structure as the daily program.

**Interconnection imports.** An import is available only in the hours
where it has an offer.  `ncp_pdd` reads the hourly offer prices from
`PRECIOSMEX.csv`: a blank or zero price closes the import in that hour,
and fixed `RESTMEX.csv` schedules are kept.  `ncp_week` has no
`PRECIOSMEX.csv`, so an import unit whose fuel costs $0 has no offer and
is left out.  Neither case adds an aggregate import limit, because the
sources set none (`sddp2gtopt --import-limit` is opt-in).

**Single-stage model.** Each case is one stage over the dispatch horizon;
the inter-temporal water-value floor of PSR's multi-stage model is only
approximated (terminal FutureCost in `ncp_pdd`, none in `ncp_week`).

Each case README has a **How to run** section; results go outside the
repository.
