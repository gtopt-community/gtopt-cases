# Getting and rebuilding cases

This repository keeps a single, minimal script; all real tooling
(converters, the CEN downloader, checks and analysis) lives in gtopt and
is installed with its Python tools from a gtopt checkout:

```bash
pip install -e <gtopt checkout>/scripts      # plexos2gtopt, plp2gtopt, ...
```

| Command | Purpose |
|---|---|
| `tools/get_case.py pcp <date>` | CEN PCP day: download `DATOS`/`RES` (only if not local), convert with `plexos2gtopt` and the flags/line lifts of `catalog.json` |
| `tools/get_case.py plp <date>` | CEN PLP bundle in force on a date: download, compress into `source/`, convert with `plp2gtopt` |
| `tools/get_case.py rebuild <case>` | reconvert a catalogued case from its `source/` (`--out` to write elsewhere) |
| `tools/get_case.py fetch <case>` | case whose data are not kept here (`"redistributed": false`, e.g. `sem_2025w03`, `pcp_2024-09-01`): download the archives from the publisher into `$GTOPT_CASES_CACHE`, check their sha256, extract the members it uses and convert (`--out` to write elsewhere); on a PCP day with its bundle in `source/` (e.g. `pcp_2026-05-10`), check its sha256 and run `pcp`.  Prints the gtopt command to run the case |

`get_case.py` uses the Python standard library only and calls the gtopt
console scripts `cen2gtopt-pcp-archive`, `plexos2gtopt`, `plp2gtopt`,
`plp_compress_case`, `sddp2gtopt` and `psse2gtopt`.  Downloads not kept in
git (the PLEXOS solution bundle, archives of non-redistributable cases) go to `$GTOPT_CASES_CACHE` (default
`~/.cache/gtopt-cases`).  Install the gtopt tools editable (or from a
revision whose wheel ships their data files): without the converter data
files (CEN hard user constraints, emission factors, cogeneration list)
`plexos2gtopt` builds a different model.

Related gtopt tools:

| gtopt command | Purpose |
|---|---|
| `gtopt_check_cases --repo <this checkout>` | `gtopt --lp-only` on every case and compare rows/cols/nnz with the catalog (checks that your gtopt reads the inputs as intended); `--solve` runs the cases with output outside the repository |
| `plexos2gtopt-line-lifts <case.json> <output>` | rank the binding lines of a gtopt solution, to choose line lifts |
| `cen2gtopt-pcp-solution summary --res <RES bundle> --output <dir>` | summarise a PLEXOS solution bundle (for your own comparisons; keep the output outside the repository) |
| `cen2gtopt-pcp-archive plp-in-force <date>` | which CEN PLP input bundle is in force on a date |

Style of `tools/`: `ruff format tools && ruff check tools`.
