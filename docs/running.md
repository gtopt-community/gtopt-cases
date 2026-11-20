# Running a case

A case is a gtopt planning JSON plus the files it references (PAMPL, CSV,
solver parameter files), run **together with its application profile**
when it has one: the case file goes first and the profile second (its
options win).  Run from an output directory **outside** the repository
and point `input_directory` at the case, so nothing is written into the
checkout:

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)
C=$REPO/chile/daily_scheduling/pcp_2025-10-19/case
OUT=~/gtopt-cases-out/chile/daily_scheduling/pcp_2025-10-19
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pcp_2025-10-19.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$C" -d . --set solver_options.threads=8
```

Every case README has its exact command, the expected resources and how
to regenerate the case from `source/`; `catalog.json` → `run` holds the
same command per case.  Resource classes: **large** — the 14 Chilean
daily cases (MIPs of 0.8–1.3 M rows, 5–30 GB RAM), the Chilean and
Peruvian SDDP cases;
**medium** — the Guatemalan NCP and SDDP cases (~0.2 M rows); **small** — the
PSS®E snapshots (~1 k rows), the Polish DC OPF and the Australian ISP
week (~0.13 M rows).

## Cloning

The repository holds input data only and is kept small.  A shallow clone
is enough to use the cases:

```bash
git clone --depth 1 https://github.com/gtopt-community/gtopt-cases.git
```
