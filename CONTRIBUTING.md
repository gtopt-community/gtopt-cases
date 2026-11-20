# Contributing to gtopt-cases

This repository publishes **inputs only**: third-party source data
(`source/`), the gtopt cases converted from them (`case/`), shared
profiles and instructions.  It never holds results.

## Proposing a case

1. Open an issue with the
   [new case form](https://github.com/gtopt-community/gtopt-cases/issues/new?template=new-case.yml)
   before preparing a pull request, so the data terms can be checked
   first.
2. Lay the case out as `<country>/<application>/<case>/` with `source/`,
   `case/` and a `README.md` that follows the existing ones (AS-IS banner,
   provenance, how to run, how to rebuild).
3. Add the case to `catalog.json` (including the `terms` object) and write
   `source/NOTICE.md` and `case/NOTICE.md` like the existing ones.
4. Run `bash tools/check_repo.sh tree` (CI runs it on every pull request;
   `git config core.hooksPath .githooks` runs it before each commit).
   Pull requests are squash-merged.

## Data provenance and licence checklist

- [ ] The data are publicly available from the publisher; the public
      source URL (or publication reference) is in `catalog.json` and the
      README.
- [ ] The publisher's licence or terms of use were checked and are quoted
      or linked (or "no licence stated by the publisher" is recorded).
- [ ] The rights holder is named in `catalog.json`, the README, the
      `NOTICE.md` files, `REUSE.toml` and `THIRD_PARTY_DATA.md`.
- [ ] No personal data.
- [ ] Inputs only: no results, solutions, logs, LP dumps or caches.
- [ ] `source/` files are unmodified except for compression: every file
      fits the size rules of `tools/check_repo.sh` (≤ 10 MB per file,
      `xz -6`, or split into `<name>.<N>.xz` parts; tracked tree ≤ 400 MB).
- [ ] Every `source/` file is listed in `catalog.json` with its `sha256`
      and `bytes` (`check_repo.sh` verifies both).
- [ ] No absolute home paths in text files.

Data contributions are accepted under the terms in
[`LICENSING.md`](LICENSING.md): the third-party data keep their
publishers' rights, and what you add to the conversion layer (README,
metadata, NOTICE files, profiles) is dedicated under CC0-1.0.

## Size and hygiene rules

`tools/check_repo.sh` runs in CI on every push and pull request (and,
after `git config core.hooksPath .githooks`, before each local commit).
It rejects:

- a `source/` file whose sha256 or size differs from `catalog.json`, or a
  tracked `source/` file missing from the catalog (`NOTICE.md` excepted);

- any file larger than 10 MB (compress with `xz -6`, or split the file
  into `<name>.<N>.xz` parts, which `tools/get_case.py` joins back);
- results, logs and caches (`results/`, `output/`, `logs/`, `*.log`,
  `*.sol`, `__pycache__`): the repository publishes inputs only;
- absolute home paths (`/home/...`, Windows user folders) in text files;
- a tracked tree larger than 400 MB.

When a case is updated, its files are replaced in place rather than added
as a new copy next to the old one.  Pull requests are squash-merged.

## Tools

Changes to `tools/` are under the gtopt licence (AGPL-3.0-or-later with
the GTOpt Solver Plugin Exception, or the GTOpt Commercial License) and
need the gtopt Contributor License Agreement:
[gtopt `CLA.md`](https://github.com/gtopt-community/gtopt/blob/master/CLA.md).
Keep `tools/` minimal; converters and analysis tools belong in
[gtopt](https://github.com/gtopt-community/gtopt).

## Removal requests

Rights holders: see [`DISCLAIMER.md`](LICENSING.md#removal-requests).
