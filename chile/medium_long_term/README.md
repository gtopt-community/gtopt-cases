# Chile — medium / long term (CEN PLP, hydrothermal SDDP)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

Cases derived from the CEN **PLP** (*Programa de Largo Plazo*) model with
`plp2gtopt`: weekly/monthly stages, many hydrologies, reservoirs with
irrigation agreements, solved with SDDP (`method: sddp`).  One folder per
PLP input set, each with one case:

```
plp_<n>/
├── README.md   case summary, how to run, regeneration command, variants
├── source/     PLP input files as used by the CEN (xz-compressed)
└── case/       the gtopt case converted from ../source (plp2gtopt)
```

| Case | Source (PLP) | Case content | LP rows (`--lp-only`) |
|---|---|---|---:|
| [plp_2y](plp_2y) | 52 weekly/monthly stages, 68 hydrologies, 245 buses | `gtopt_case_2y`: full horizon, 4 hydrologies (2, 17, 52, 67), 20 apertures | 4,279,344 |
| [plp_5y](plp_5y) | 72 weekly/monthly stages (~4.5 years), 65 hydrologies, 241 buses | `gtopt_case_5y`: full horizon, 4 hydrologies (16, 17, 19, 48), 34 apertures | 3,593,820 |
| [plp_23y](plp_23y) | 276 monthly stages (23 years), 28 hydrologies, 339 buses | `cen_long_term_1y`: first 12 stages, hydrology 1, no apertures | 673,493 |

Every case is self-contained (no profile: method and SDDP options are in
the case JSON) and loads the PLP boundary cuts through
`system.future_cost_array` (`case/boundary_cuts.csv`).  Other horizons,
hydrology sets or methods are one `plp2gtopt` command away from
`source/`: see the **Variants** section of each case README (e.g. the
full 23-year horizon of `plp_23y`, or the former `gtopt_case_2y_fs`
first-scenario variant of `plp_2y`).

Run a case as its README shows, with results outside the repository
(`~/gtopt-cases-out/<case id>`).  `tools/get_case.py rebuild plp_<n>
--out <dir>` reconverts `case/` from the committed `source/` with the
flags of `catalog.json`.

## New PLP cases from the CEN portal

```bash
tools/get_case.py plp 2026-05-15 --dry-run      # which IPLP bundle?
tools/get_case.py plp 2026-05-15                # download + plp2gtopt
```

PLP runs are not published daily: `cen2gtopt-pcp-archive plp-in-force`
(called by the script) takes the latest `IPLP*` bundle dated on or before
the given date (`--name` forces one).  The CEN bucket only serves Chilean IP
addresses; with a local copy, put its PLP files in
`chile/medium_long_term/plp_<date>/source/` and the download is skipped.
The flags come from `catalog.json` (`converter_defaults.medium_long_term`,
plus `--plp2gtopt-arg`).  The inputs land in
`chile/medium_long_term/plp_<date>/{source,case}/`.  Run the case as the
case READMEs show (results outside the repository), e.g. with
`--set sddp_options.max_iterations=20`.
