# IEEE and standard test systems (PGLib-OPF)

> [!WARNING]
> Provided **AS IS**, not validated by the data authors, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

Standard test networks from the **IEEE PES Power Grid Library — Optimal
Power Flow** ([PGLib-OPF](https://github.com/power-grid-lib/pglib-opf)
v23.07), whose data are licensed under **CC BY 4.0**, converted to gtopt
single-hour DC OPF cases with `pp2gtopt`.  PGLib-OPF is used rather than
the MATPOWER copies of the same systems because MATPOWER's licence does
not cover its case files, while PGLib-OPF states an open data licence
for each file.  The Polish system `case3375wp` is in
[`poland/`](../../poland/README.md).

| Case | What | Network | Application | In this repository |
|---|---|---|---|---|
| [pglib_opf_case118_ieee](pglib_opf_case118_ieee/README.md) | IEEE 118-bus test case (PGLib-OPF v23.07) | 118 buses | dc_opf | source + case |
| [pglib_opf_case14_ieee](pglib_opf_case14_ieee/README.md) | IEEE 14-bus test case (PGLib-OPF v23.07) | 14 buses | dc_opf | source + case |
| [pglib_opf_case24_ieee_rts](pglib_opf_case24_ieee_rts/README.md) | IEEE Reliability Test System 1979 (24 buses) (PGLib-OPF v23.07) | 24 buses | dc_opf | source + case |
| [pglib_opf_case300_ieee](pglib_opf_case300_ieee/README.md) | IEEE 300-bus test case (PGLib-OPF v23.07) | 300 buses | dc_opf | source + case |
| [pglib_opf_case30_ieee](pglib_opf_case30_ieee/README.md) | IEEE 30-bus test case (PGLib-OPF v23.07) | 30 buses | dc_opf | source + case |
| [pglib_opf_case39_epri](pglib_opf_case39_epri/README.md) | New England 39-bus system (PGLib-OPF v23.07) | 39 buses | dc_opf | source + case |
| [pglib_opf_case57_ieee](pglib_opf_case57_ieee/README.md) | IEEE 57-bus test case (PGLib-OPF v23.07) | 57 buses | dc_opf | source + case |
| [pglib_opf_case5_pjm](pglib_opf_case5_pjm/README.md) | PJM 5-bus system (PGLib-OPF v23.07) | 5 buses | dc_opf | source + case |
| [pglib_opf_case73_ieee_rts](pglib_opf_case73_ieee_rts/README.md) | IEEE Reliability Test System 1996 (73 buses, three areas) (PGLib-OPF v23.07) | 73 buses | dc_opf | source + case |

Licence, citation and the exact converter command of each case are in its
README; machine-readable provenance is in [`catalog.json`](../../catalog.json).
