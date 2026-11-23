# PCP 2024-10-03 — CEN daily unit commitment (source only, fetched on demand)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../../DISCLAIMER.md).

> [!IMPORTANT]
> **Source only, fetched on demand: no CEN data and no gtopt case here.**
> `tools/get_case.py fetch pcp_2024-10-03` downloads the public CEN file,
> checks its sha256 and builds the case on your machine (see [Why the data
> are not here](#why-the-data-are-not-here)).  No gtopt case has been
> built or checked for this day by the gtopt authors.

> These cases try to reproduce the conditions under which PLEXOS is run for
> the CEN daily program.  That configuration (model settings, constraints,
> line ratings and expansions, solver settings, …) is defined by the CEN,
> not by gtopt; the profile, flags and line lifts here only aim to
> replicate it and are not gtopt's recommended defaults.

Kept as a test day for the study of negative nodal prices (marginal costs)
in the CEN daily programme.

| Field | Value |
|---|---|
| Case id | `chile/daily_scheduling/pcp_2024-10-03` |
| Program date | 2024-10-03 (horizon starts 00:00 of this day) |
| Purpose | negative nodal prices |
| Source | public CEN file `PLEXOS20241003.zip`, <https://www.coordinador.cl/wp-content/uploads/2024/10/PLEXOS20241003.zip> |
| Source sha256 | `9a0f5c0983336ad0fa7c5f1a8fa86270da6387c8e4fa93ef47fba7b878338df1` (27,089,500 bytes) |
| PLEXOS input | `DATOS20241003.zip` inside it (sha256 `8c6626990feb7f3f…`, 5,071,014 bytes); the PLEXOS solution `RES20241003.zip` in the same file is a result and is not published |
| PLEXOS version | 9.000 (database `DBSEN_PRGDIARIO.xml`) |
| Converter | `plexos2gtopt` from gtopt master of November 2026 or later (PLEXOS 8.100, 9.000 and 10.000 databases; `--source-version 9.000`) |
| Flags | `--no-check --write-out all --plexos-legacy --no-battery-efin-pin --line-losses-mode piecewise --loss-cost-eps 0 --source-version 9.000` |
| Line lifts | `--lifts common`: the 35 `common` lines of [`line_lifts.json`](../line_lifts.json) (no per-case list for this day) |
| Method / profile | monolithic MIP, [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json) |

## Why the data are not here

The CEN terms are the same as for the PCP days whose input bundle is kept
in this repository ([`THIRD_PARTY_DATA.md`](../../../THIRD_PARTY_DATA.md)).
This day is fetched instead only to keep the repository under its 400 MB
size limit (`tools/check_repo.sh`): the CEN publishes the file at a stable
public URL on `www.coordinador.cl`, which, unlike the
`programa.coordinador.cl` download bucket, is reachable from any country,
so `fetch` gets the exact file and checks it against the sha256 above.

## Get and convert

With the gtopt Python tools of gtopt master of November 2026 or later
installed (`pip install -e <gtopt>/scripts`):

```bash
tools/get_case.py fetch pcp_2024-10-03
```

This downloads `PLEXOS20241003.zip` into `$GTOPT_CASES_CACHE/20241003/`
(default `~/.cache/gtopt-cases`, outside the repository), checks its
sha256, extracts the PLEXOS input into `source/DATOS20241003.zip` and the
PLEXOS solution into the cache as `RES20241003.zip` (needed only for the
variable-length block layout), runs `plexos2gtopt` with the flags and line
lifts in [`catalog.json`](../../../catalog.json), writes
`case/pcp_2024-10-03.json` and prints the gtopt command to run it.
`source/` and `case/` are git-ignored; use `--out DIR` to write the case
elsewhere and `--lifts {case,common,union,none}` to choose other line
lifts.

## How to run

Results are never written into this repository: run from an output
directory outside it (here `~/gtopt-cases-out/<case id>`).

```bash
ulimit -c unlimited
REPO=$(git rev-parse --show-toplevel)      # this checkout
C=$REPO/chile/daily_scheduling/pcp_2024-10-03/case
OUT=~/gtopt-cases-out/chile/daily_scheduling/pcp_2024-10-03
mkdir -p "$OUT/output" && cd "$OUT/output"
gtopt "$C/pcp_2024-10-03.json" "$REPO/profiles/daily_scheduling.json" \
    --set input_directory="$C" -d . --set solver_options.threads=8
```

- The case JSON goes first and the profile
  [`profiles/daily_scheduling.json`](../../../profiles/daily_scheduling.json)
  second (its options win).  Monolithic MIP: MIP gap 0.5 %, time limit
  7200 s, MIP start.
- `--set input_directory="$C"` makes the case's relative input files
  resolve against the case directory while the run happens in the output
  directory, so nothing lands in the repository.
- Expected resources: not measured for this day (no case is catalogued);
  the catalogued PCP cases are 0.8–1.3 M-row MIPs that need a multi-core
  machine and 5–30 GB of RAM.
