# Chile — transmission planning (CEN PET, PLP)

> [!WARNING]
> Provided **AS IS**, not validated by the publishers, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

Model bases of the CEN annual **transmission planning process**
(*Propuesta de Expansión de Transmisión del SEN*), converted with
`plp2gtopt`.  The CEN simulates the long-term hydrothermal operation with
PLP and evaluates each transmission project by with/without runs; the
bases carry the transmission plan of works but no investment costs, so
these are operation (SDDP) cases, not expansion-optimization cases.

| Case group | Process | Cases | Content |
|---|---|---|---|
| [plp_pet27](plp_pet27/README.md) | **PLP-PET27 — Proceso de Planificación de la Transmisión 2027** (Diagnóstico, Anexo IV.1) | [e01](plp_pet27/e01), [e02](plp_pet27/e02), [e03](plp_pet27/e03): one per energy scenario, configuration CS_I | 276 monthly stages, 25 hydrologies, 292 buses; committed cases: first year, hydrology 1; methodology PDF in `plp_pet27/methodology/` |

Each case folder has a `README.md` with a **How to run** section,
`source/` (PLP inputs, xz) and `case/` (gtopt case).  Results go outside
the repository (`~/gtopt-cases-out/<case id>`).
