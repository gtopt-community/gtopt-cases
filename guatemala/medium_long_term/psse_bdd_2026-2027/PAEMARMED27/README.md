# PAEMARMED27 — Guatemala (medium long term)

> [!WARNING]
> **Provided AS IS — not validated by the publishing institutions.**  These
> cases were built with gtopt's own conversion tools and verified only as
> far as the authors can; they have **not** been validated by the
> institutions that published the source data and come **with no warranty**.
> They must **never** be used as a reference for analysing official
> operation scheduling or for financial analysis.  All rights to the
> original data belong to their authors and/or the publishing institutions.
> See [DISCLAIMER.md](../../../../DISCLAIMER.md).

| Field | Value |
|---|---|
| Case id | `guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMED27` |
| Horizon | 1 blocks covering 1 h, 1 stage, 1 scenario |
| Network | 877 buses, 948 lines |
| Units | 114 generators, 0 batteries |
| LP (`--lp-only`) | 949 rows, 1,323 cols, 2,745 nnz (gtopt development revision `3b70b4ee9eca`, local build) |
| Method / profile | monolithic, no profile (self-contained JSON) |
| Source | `../source/LDM Marzo 2027.xlsx.xz`, `../source/Nomenclatura.xls.xz`, `../source/PAEMARMED27.raw.xz` |
| Origin | AMM long-term study 'BDD ESO PLP AE MAY26-ABR27 Definitiva.7z' (PSS/E v33 network + AMM spreadsheets; archive not redistributed) |
| Converter | `psse2gtopt` from gtopt; rebuild with gtopt master of November 2026 or later (development revision used: `catalog.json`) |
| Flags | `--nomenclatura Nomenclatura.xls.xz --ldm LDM Marzo 2027.xlsx.xz --rating-set A` |

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMED27/case
OUT=~/gtopt-cases-out/guatemala/medium_long_term/psse_bdd_2026-2027/PAEMARMED27
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/PAEMARMED27.json" \
    --set input_directory="$C" -d .
```

To check that your gtopt build reads the case as intended, compare its LP
size with `catalog.json` (`gtopt_check_cases` ships with the gtopt Python
tools):

```bash
gtopt_check_cases --repo "$REPO" --only PAEMARMED27    # LP only: rows/cols/nnz
```

- Self-contained case: no profile; all options are in the case JSON.
- `--set input_directory="$C"` makes the case's relative input files
  (PAMPL, CSV, solver parameter files) resolve against the case directory
  while the run happens in the output directory, so solver side files
  (e.g. CPLEX `clone*.log`) never land in the repository.
- Solver: gtopt picks the best available plugin (`--solver highs|cplex|…`
  to choose); `gtopt --solvers` lists them.
- Expected resources: **small** — ~1k-row LP; well under 1 GB RAM, any machine.
- Tested with a gtopt build that includes FutureCost (`system.future_cost_array`).

### Regenerate `case/` from `source/`

The case JSON was produced with an earlier gtopt development revision.  To
regenerate it with the installed converter and the
flags pinned in `catalog.json`:

```bash
tools/get_case.py rebuild PAEMARMED27 --out <dir>
```

The converters have evolved since this case was produced, so a rebuild may
differ from the committed case; check it with `gtopt_check_cases`.

## Notes

- Self-contained case (no application profile); run as is.
- Single-period DC-OPF network snapshot from the AMM long-term study (PLP May-2026..Apr-2027): Mar 2027 (dry), medium demand; 1 stage / 1 block / 1 scenario.
- Costs are rank-based merit order from the LDM spreadsheet (PSS/E RAW has no costs; about half the generators match by name).
