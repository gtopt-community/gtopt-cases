# UnitCommitment.jl test fixtures

> [!WARNING]
> Provided **AS IS**, not validated by the data authors, who keep all
> rights over the data.  See the [disclaimer](../../DISCLAIMER.md).

Unit-commitment test fixtures of
[UnitCommitment.jl](https://github.com/ANL-CEEESA/UnitCommitment.jl)
(Argonne National Laboratory, BSD-3-Clause), converted with gtopt's
`tools/ucjl2gtopt.py` to unit-commitment MIPs.

| Case | What | Network | Application | In this repository |
|---|---|---|---|---|
| [case118_initcond](case118_initcond/README.md) | IEEE 118-bus unit commitment with initial conditions (UnitCommitment.jl test fixture) | 118 buses | unit_commitment | source + case |
| [case14](case14/README.md) | IEEE 14-bus unit commitment (UnitCommitment.jl test fixture) | 14 buses | unit_commitment | source + case |
| [case14_profiled](case14_profiled/README.md) | IEEE 14-bus unit commitment with profiled renewables (UnitCommitment.jl test fixture) | 14 buses | unit_commitment | source + case |

Licence, citation and the exact converter command of each case are in its
README; machine-readable provenance is in [`catalog.json`](../../catalog.json).
