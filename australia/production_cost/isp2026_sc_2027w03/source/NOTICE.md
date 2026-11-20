# Notice: third-party data

This directory holds third-party data used by
`australia/production_cost/isp2026_sc_2027w03`.

- **Origin:**
  - AEMO 2026 Integrated System Plan (ISP) PLEXOS model and trace files,
    <https://www.aemo.com.au/energy-systems/major-publications/integrated-system-plan-isp/2026-integrated-system-plan-isp>;
    scenario XML `2026 ISP Step Change/2026 ISP Step Change Model.xml`,
    uncompressed sha256
    19cc3451f1ee00955019bb501d800e629bb740e3bb51e270020ef2dd7485a849
    (archive hashes in the case README)
- **Rights holder(s):**
  - Australian Energy Market Operator (AEMO), <https://www.aemo.com.au>
- **Licence:** AEMO's copyright permissions
  (<https://aemo.com.au/privacy-and-legal-notices/copyright-permissions>):
  "AEMO confirms its general permission for anyone to use AEMO Material
  for any purpose, but only with accurate and appropriate attribution of
  the relevant AEMO Material and AEMO as its author.  You do not need to
  obtain specific permission to use AEMO Material in this way."
  Confidential documents and reports commissioned by third parties are
  excluded.  This repository grants no further licence over these files;
  all rights remain with AEMO.
- **Modifications:** the scenario XML is unmodified except xz compression;
  the trace files under `traces/` are cut to the rows of the case week
  (2027-01-18 to 2027-01-24), see `NOT_KEPT.txt`.  File hashes (sha256)
  and sizes are in `traces.sha256` and
  [`catalog.json`](../../../../catalog.json).
- **No affiliation:** the gtopt project is not affiliated with or endorsed
  by AEMO.
- **Attribution:** Source: Australian Energy Market Operator (AEMO), 2026
  Integrated System Plan PLEXOS model (Step Change), © AEMO, used under
  AEMO's copyright permissions; converted to gtopt format.
- **Removal requests:** e-mail <marcelomatusacuna@gmail.com> with the
  subject "gtopt-cases removal request"; see
  [`DISCLAIMER.md`](../../../../DISCLAIMER.md#removal-requests).

Details: [`THIRD_PARTY_DATA.md`](../../../../THIRD_PARTY_DATA.md) and
[`LICENSING.md`](../../../../LICENSING.md).  This notice is not legal
advice.
