# Benchmark cases

> [!WARNING]
> Provided **AS IS**, not validated by the authors of the data, who keep
> all rights over them.  See the [disclaimer](../DISCLAIMER.md).

Standard test systems, example systems of other tools and published case
studies, converted to gtopt with gtopt's own converters.  Unlike the
country folders they describe no real system's operation: they are
reference problems for research, teaching and software testing.

Each source's licence was checked before anything was copied here:

- **open licence** (CC BY 4.0, BSD-3-Clause): `source/` keeps the
  upstream files unmodified (xz/gzip) and `case/` the gtopt case, with
  the attribution the licence asks for;
- **no licence**: the folder holds only a README (and a sha256 manifest
  where needed); `tools/get_case.py fetch <case>` downloads the files of
  a pinned upstream commit, checks every sha256 and converts them on your
  machine into the git-ignored `source/` and `case/`.

| Family | Cases | Source · licence | In this repository |
|---|---|---|---|
| [ieee/](ieee/README.md) | 9 single-hour DC OPF (5 to 300 buses) | PGLib-OPF v23.07 · CC BY 4.0 | source + case |
| [unitcommitment_jl/](unitcommitment_jl/README.md) | 3 unit-commitment MIPs (IEEE 14 and 118 buses) | UnitCommitment.jl test fixtures · BSD-3-Clause | source + case |
| [nrel/](nrel/README.md) | 1 one-week dispatch of the NREL-118 system | Sienna PowerSystemsTestData · no licence | recipe only |
| [sienna/](sienna/README.md) | 7 small PowerSimulations.jl test systems (PJM 5-bus) | Sienna PowerSystemsTestData · no licence | recipe only |
| [papers/](papers/README.md) | 2 clustered unit-commitment case studies (Morales-España and Tejada-Arango, 2019) | CUC-data · no licence | recipe only |

Layout: `benchmarks/<family>/<case>/` (papers:
`benchmarks/papers/<author_year_topic>/<case>/`) with a `README.md`,
`source/` and `case/` as in the country folders.  Inputs only: no gtopt
results.  A paper folder may quote the paper's own published figures,
labelled as the paper's.

## Not included (yet)

- **SDDP examples.**  The SDDP.jl examples (MPL-2.0) have no gtopt
  converter (gtopt's `cases/` holds hand-adapted versions), and the PSR
  SDDP samples of PSRClassesInterface.jl (MPL-2.0) convert with the
  current `sddp2gtopt` only as trivial dispatches (no reservoirs; costs
  dropped on the `psrclasses.json` path).  A `sddp/` family will be added
  when the conversion is faithful.
- **RTS-GMLC** (NREL data-use agreement, redistribution allowed with the
  notice): `rts_gmlc_to_gtopt` currently builds a single-bus emission
  fixture with a synthetic load shape, not the RTS-GMLC system.
- **UnitCommitment.jl `case14-storage`**: the converted MIP is infeasible
  in gtopt (the LP relaxation solves); under investigation in gtopt.
- **UnitCommitment.jl benchmark library** (365-day instances on its
  website): distributed outside the licensed repository, licence unclear.
- **MATPOWER case files** (e.g. the WSCC 9-bus `case9`): MATPOWER's
  licence does not cover them; the PGLib-OPF versions are used instead.
  `case3375wp` is already in [`poland/`](../poland/README.md).
- **cn_3266b** (Chinese provincial 3266-bus system, CC BY 4.0): the data
  need an IEEE DataPort subscription to download.

Machine-readable index: [`catalog.json`](../catalog.json) (entries with
`"collection": "benchmarks"`).
