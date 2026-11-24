# Disclaimer

**Read this before using any case in this repository.**

## What these cases are

The cases in this repository were **built by the gtopt authors with gtopt's
own conversion tools** (`plp2gtopt`, `plexos2gtopt`, `sddp2gtopt`,
`psse2gtopt`, and others) from data published by third parties: system
operators, coordinators, regulators and other institutions.

- They have been checked **only as far as the authors are able to**, for
  example by comparing selected results against the outputs the source
  institutions published.
- They have **not** been reviewed, validated or endorsed by the institutions
  or entities that published the source data. Those institutions bear no
  responsibility for them.
- A converted case is **not** the original model. Conversion involves
  simplifications, assumptions, interpretation of file formats and
  modelling choices that may differ from those of the original tool and its
  operator. Results can and will differ from the official ones.

## What they must not be used for

The cases are provided for **research, education, software testing and
benchmarking** only.

They **must not be used, in any case, as a reference** for:

- the analysis, review or audit of the official operation scheduling,
  dispatch, marginal costs or prices of any power system;
- financial, commercial, investment, regulatory or legal analysis or
  decisions, including the valuation of assets, contracts, bids or
  settlements;
- any claim about the conduct or results of the institutions that published
  the source data.

For any of those purposes, use the official data and results published by
the competent institutions.

## No warranty

THE CASES, DATA, SCRIPTS AND DOCUMENTATION IN THIS REPOSITORY ARE PROVIDED
"AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF ACCURACY, COMPLETENESS, MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. THE ENTIRE RISK AS TO THE
QUALITY, ACCURACY AND USE OF THE CASES IS WITH YOU.

IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY OR CONSEQUENTIAL (INCLUDING, BUT NOT LIMITED TO, LOSS OF
DATA, PROFITS OR BUSINESS OPPORTUNITIES), WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE CASES OR THE
USE OR OTHER DEALINGS IN THE CASES, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

## Ownership of the source data

All rights to the original cases, models and data belong to their authors
and/or to the institutions that published them: Australian Energy Market
Operator (AEMO), Australia; Coordinador Eléctrico Nacional (CEN), Chile;
Administrador del Mercado Mayorista (AMM), Guatemala; Ente Operador Regional
(EOR); Comité de Operación Económica del Sistema Interconectado Nacional
(COES), Peru; Roman Korab, Silesian University of Technology, whose data
are distributed by MATPOWER; and, for the benchmark cases (`benchmarks/`),
the authors named in each data file (IEEE, University of Washington,
UChicago Argonne, LLC, NREL / Alliance for Sustainable Energy, and the
authors of published papers).  This repository claims no ownership of them
and grants no licence over them; benchmark data published under an open
licence (CC BY 4.0, BSD-3-Clause) keep that licence, granted by their
authors.  `source/` holds the data as published (unmodified
except for compression and splitting into parts; the AEMO traces are cut to
the case week); `case/` holds gtopt conversions derived from it, which remain
subject to the publishers' rights.  See [`LICENSING.md`](LICENSING.md) and
[`THIRD_PARTY_DATA.md`](THIRD_PARTY_DATA.md); the source data remain subject
to the terms of use of those institutions.

## No affiliation; trademarks

The gtopt project is not affiliated with, sponsored by or endorsed by AEMO,
CEN, AMM, EOR, COES, the SEM Committee, CRU, Utility Regulator, NERA, Energy
Exemplar, PSR, Siemens, IBM, MATPOWER / PSERC, the IEEE, PGLib-OPF, Argonne
National Laboratory (UnitCommitment.jl) or NREL (Sienna). Mentioning an
institution or a product does not imply any such relationship.

PLEXOS® is a registered trademark of Energy Exemplar.  SDDP and NCP are
products of PSR.  PSS®E is a registered trademark of
Siemens.  CPLEX is a trademark of IBM.  MATPOWER is a project originally
developed at PSERC (Cornell University).  These and other product names
are used only nominatively, to identify the file formats and tools the
data come from or that gtopt can read; all trademarks belong to their
respective owners.

## Removal requests

If you are a rights holder and object to the redistribution of any
material here, e-mail <marcelomatusacuna@gmail.com> with the subject
**"gtopt-cases removal request"**; for non-confidential requests you may
instead open an issue with the
[data removal form](https://github.com/gtopt-community/gtopt-cases/issues/new?template=data-removal.yml).
We acknowledge each request within 5 working days and remove the material
from `main` promptly.  When required, we also rewrite the git history and
ask GitHub Support to purge cached views; the maintainers bypass the
main-branch protection ruleset only for that purpose.

This disclaimer is not legal advice.

---

## Aviso (español)

Los casos de este repositorio fueron **construidos por los autores de gtopt
con sus propias herramientas de conversión**, a partir de datos publicados
por terceros (coordinadores, operadores, reguladores y otras instituciones).
Se han verificado **solo hasta donde los autores pueden llegar** y **no
cuentan con la validación** de las instituciones o entidades que publicaron
los datos de origen.

Se entregan **"TAL CUAL" (AS IS), sin garantía de ningún tipo**, expresa o
implícita. **En ningún caso deben usarse como referencia** para el análisis
de la programación o la operación oficial de un sistema eléctrico, ni para
análisis o decisiones financieras, comerciales, de inversión, regulatorias o
legales. Para esos fines se deben usar los datos y resultados oficiales
publicados por las instituciones competentes. Los autores no asumen
responsabilidad alguna por el uso de estos casos.

Todos los derechos sobre los casos, modelos y datos originales pertenecen a
sus autores y/o a las instituciones que los publican (AEMO, Australia; CEN,
Chile; AMM, Guatemala; EOR; COES, Perú; Roman Korab, Universidad Tecnológica
de Silesia, con datos distribuidos por MATPOWER). Este repositorio no reclama
propiedad sobre ellos ni otorga licencia alguna sobre ellos; solo redistribuye
los insumos tal como fueron publicados (sin modificaciones, salvo compresión y
división en partes; las series de AEMO se recortan a la semana del caso),
junto con las conversiones a gtopt derivadas de ellos, que siguen sujetas a
los derechos de los publicadores.

El proyecto gtopt no está afiliado a AEMO, CEN, AMM, EOR, COES, SEM Committee,
CRU, Utility Regulator, NERA, Energy Exemplar, PSR, Siemens, IBM ni MATPOWER /
PSERC, ni cuenta con su patrocinio o respaldo. PLEXOS® es marca registrada de
Energy Exemplar; SDDP y NCP son productos de PSR; PSS®E es marca registrada de
Siemens; CPLEX es marca de IBM; MATPOWER es un proyecto desarrollado
originalmente en PSERC (Universidad de Cornell). Estos nombres se usan solo
para identificar los formatos de archivo y las herramientas de origen de los
datos; todas las marcas pertenecen a sus respectivos dueños.

Si usted es titular de derechos y se opone a la redistribución de algún
material, escriba a <marcelomatusacuna@gmail.com> con el asunto
**"gtopt-cases removal request"** (para solicitudes no confidenciales
puede usar el formulario de retiro de datos en los issues). Acusamos
recibo dentro de 5 días hábiles y retiramos el material de `main` a la
brevedad; cuando corresponde, reescribimos además el historial de git y
pedimos a GitHub Support purgar las vistas en caché.

Este aviso no constituye asesoría legal.
