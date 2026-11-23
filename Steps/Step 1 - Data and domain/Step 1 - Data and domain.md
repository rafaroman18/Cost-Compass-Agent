# RAG Agent

## Data and domain

The agent answers questions about the cost of living in Spain from 2020 to 2026, crossing four areas:

1. Housing
2. Employment
3. Prices (food and commodity)
4. Energy

Each area has tables (numbers by quarter or month, loaded into SQL), documents (reports and laws, indexed for RAG) and, where it exists, an API for the latest values.

All files were downloaded between 2026-11-14 and 2026-11-18. Hashes are SHA-256 of the files as stored. Housing and Employment are documented below. Prices and Energy are still pending.

### Housing

#### Table

| Field | Value |
|---|---|
| Title | Housing Price Index (IPV) by autonomous community, 2020-2026 |
| Publisher | INE (Instituto Nacional de Estadística) |
| Retrieved | 2026-11-18 |
| Last updated by INE | 2026-09-07 |
| URL | https://www.ine.es/jaxiT3/Tabla.htm?t=79563&L=0 |
<!-- | Licence | CC BY 4.0 | -->
| File | `Housing/IPV por CCAA 2020_2026.csv` |
| SHA-256 | `9e3546141eb621ceba041cf754b8d58b348ff87c078e613a62a5a57faeb8a6b0` |
| Notes | 2,080 rows, `;` separator, decimal comma. Base 2025 = 100. Latest period 2026T2. |

Licence (INE, https://www.ine.es): reuse with attribution is allowed, commercial use included. Since I process the data, I cite it as "Elaboración propia con datos extraídos del sitio web del INE: www.ine.es", with the last update date. I do not suggest that the INE supports the project.

#### Documents: legislation (BOE and BOJA)

14 files, downloaded on 2026-11-18. Type, dates and repeal status come from each document's BOE record.

"Consolidated" is the text in force on the download date, with later amendments merged in. "Original" is the text as published. The "in force" date is that of the original rule.

| Title | Type | Published | In force | Version | Status | URL | File | SHA-256 |
|---|---|---|---|---|---|---|---|---|
| Ley 11/2020 (Cataluña), rent containment in housing leases | Regional law | 2020-09-29 | 2020-09-22 | Consolidated | Not repealed, but most rent-control articles were annulled by the Constitutional Court (STC 37/2022, e.g. arts. 6 to 13). The text flags each one | https://www.boe.es/buscar/pdf/2020/BOE-A-2020-11363-consolidado.pdf | `Reports/BOE-A-2020-11363-consolidado.pdf` | `d84174e21a43f497005d91ed623cee012c3064c867cc3a6153ef1e06eca28199` |
| Real Decreto-ley 11/2020, urgent COVID-19 measures (rent and eviction moratorium) | Royal decree-law | 2020-04-01 | 2020-04-02 | Consolidated | In force | https://www.boe.es/buscar/pdf/2020/BOE-A-2020-4208-consolidado.pdf | `Reports/BOE-A-2020-4208-consolidado.pdf` | `6a3431fb6a98c26fa2515f0c14ec21372117e8666ab4243812940625e6f57210` |
| Real Decreto 853/2021, residential renovation and social housing | Royal decree | 2021-10-06 | 2021-10-07 | Consolidated | In force | https://www.boe.es/buscar/pdf/2021/BOE-A-2021-16233-consolidado.pdf | `Reports/BOE-A-2021-16233-consolidado.pdf` | `a8cf8081fc3d8cca803a481710f32f584e716f2b566a63916cebe819e513d7a8` |
| Real Decreto-ley 6/2022, Ukraine war measures (cap on rent updates) | Royal decree-law | 2022-03-30 | 2022-03-31 | Consolidated | In force | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-4972-consolidado.pdf | `Reports/BOE-A-2022-4972-consolidado.pdf` | `b6fdcd28e5212a751836006eeab8d274c6c6e0796bab0041b20d9d02424ddee8` |
| Real Decreto 42/2022, Bono Alquiler Joven and State Housing Plan 2022-2025 | Royal decree | 2022-01-19 | 2022-01-20 | Consolidated | In force | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-802-consolidado.pdf | `Reports/BOE-A-2022-802-consolidado.pdf` | `2b0a4816bb766edd4fca19725e5460be2924841d3368337437086715721e83c1` |
| Real Decreto 903/2022, amends RD 42/2022 | Royal decree | 2022-10-26 | 2022-10-27 | Original | Amending text only | https://www.boe.es/boe/dias/2022/10/26/pdfs/BOE-A-2022-17474.pdf | `Reports/BOE-A-2022-17474.pdf` | `bf373ce02d8e0d4aed3c61f2b37defbd75950b16ba920eaa6122e56491d37eac` |
| Ley 12/2023, right to housing | Law | 2023-05-25 | 2023-05-26 | Consolidated | In force | https://www.boe.es/buscar/pdf/2023/BOE-A-2023-12203-consolidado.pdf | `Reports/BOE-A-2023-12203-consolidado.pdf` | `771a3f4ab6f131bf026552b921531f275413866bdb87b9d5fa5143845a82086c` |
| Real Decreto-ley 8/2023, Ukraine and Middle East measures (extension of housing measures) | Royal decree-law | 2023-12-28 | 2023-12-29 | Consolidated | In force | https://www.boe.es/buscar/pdf/2023/BOE-A-2023-26452-consolidado.pdf | `Reports/BOE-A-2023-26452-consolidado.pdf` | `02ad9516bdfd4a0aa4696dfd6e5b11cd9fd15f483748869aa7e6f4b230440376` |
| INE Resolution of 2024-12-18, reference index for annual rent updates | Resolution | 2024-12-20 | 2025-01-01 (BOE gives no date) | Original | In force | https://www.boe.es/boe/dias/2024/12/20/pdfs/BOE-A-2024-26685.pdf | `Reports/BOE-A-2024-26685.pdf` | `c01ce0f0de6d80705870ffa5474a506e4f549263b2725a8913f61f6a2bba10cd` |
| Decreto-ley 1/2025 (Andalucía), urgent housing measures (BOJA no. 41) | Regional decree-law | 2025-03-03 | 2025-03-04 | Original | In force. Private use only | https://www.boe.es/ccaa/boja/2025/041/b00001-00029.pdf | `Reports/BOJA-b-2025-90042.pdf` | `8e49f8cc8689fd23b4c00cffdd8d14e128bae7915a9985e84bcf445c517543a4` |
| Real Decreto-ley 2/2026, social vulnerability, tax and system resources | Royal decree-law | 2026-02-04 | 2026-02-05 | Consolidated | **Repealed on 2026-02-28** by the next row | https://www.boe.es/buscar/pdf/2026/BOE-A-2026-2547-consolidado.pdf | `Reports/BOE-A-2026-2547-consolidado.pdf` | `3bcc7dec8ee105019535a017734ef46e95b620480fc3299a5d8607dcafb9bda0` |
| Congress resolution of 2026-02-26, repeal of RDL 2/2026 | Resolution | 2026-02-28 | 2026-02-28 | Original | Repeals BOE-A-2026-2547 | https://www.boe.es/boe/dias/2026/02/28/pdfs/BOE-A-2026-4667.pdf | `Reports/BOE-A-2026-4667.pdf` | `35b53169fcb92a6ddf3b36a94faf57865229e174945fced5d2601f60991f7f16` |
| Real Decreto 326/2026, State Housing Plan 2026-2030 | Royal decree | 2026-04-23 | 2026-04-24 | Original | In force | https://www.boe.es/boe/dias/2026/04/23/pdfs/BOE-A-2026-8872.pdf | `Reports/BOE-A-2026-8872.pdf` | `3eb6f2495f43852a67402db379243fb7731544e518266a3e8f42ee3df2cd7ce7` |
| Real Decreto-ley 29/2026, social function of housing and affordable supply | Royal decree-law | 2026-10-07 | 2026-10-08 | Consolidated | In force | https://www.boe.es/buscar/pdf/2026/BOE-A-2026-20823-consolidado.pdf | `Reports/BOE-A-2026-20823-consolidado.pdf` | `5ebe02890e2edf3c0e37d9f77d25ce5d3af2c4118465688d30f9206613355f7b` |

I chose one rule per topic instead of one per year. I kept the repealed RDL 2/2026 and the annulled articles of Ley 11/2020 on purpose, so the agent can say a rule is no longer applicable.

Licence (BOE, https://www.boe.es/informacion/aviso_legal/index.php, standard licence of 2024-06-27): reuse is allowed, commercial use and derived works included. My citation is "Basado en datos de la Agencia Estatal Boletín Oficial del Estado", with a link to https://www.boe.es. A reused consolidated text must be labelled as informative only, since only the texts in the official gazette are authentic. I do not suggest that the BOE supports the project.

The BOJA file is published by the Junta de Andalucía and only hosted on the BOE site, so this licence does not cover it. Its legal notice (https://www.juntadeandalucia.es/eboja/sobre-boja/aviso-juridico.html) allows faithful reproduction for private use and forbids modification and extraction of its contents without authorisation. I treat it as private use.

#### Documents: "Vivienda, Consumo y Desigualdad" reports

Series from the Ministerio de Derechos Sociales, Consumo y Agenda 2030, with the Instituto de Filosofía of the CSIC. Authors: Javier Gil (coordinator), Óscar Villas, Miguel García-Duch and Irene Lebrusán. Downloaded on 2026-11-18 from dsca.gob.es. Publication dates come from the Ministry's press notes.

| Title | Published | Pages | URL | File | SHA-256 |
|---|---|---|---|---|---|
| Informe 1. Un mercado dominado por multiarrendadores | 2026-04-22 | 15 | https://www.dsca.gob.es/sites/default/files/prensa/Informe%201%20Multiarrendadores.pdf | `Reports/Informe1-Multiarrendadores.pdf` | `d810bb7e878034239acddc9d85a65a98593436c647f8f0de6398c03e7c5812b2` |
| Informe 2. El problema de la concentración inmobiliaria en España | 2026-04-26 | 15 | https://www.dsca.gob.es/sites/default/files/prensa/Informe_2_concentracion_inmobiliaria.pdf | `Reports/Informe2_concentracion_inmobiliaria.pdf` | `e54f155984187c421be20e7487ca1cc5306c63e2254cb79f2f2ffbd8ae860ee0` |
| Informe 3. Renta, riqueza y régimen de tenencia | 2026-07-06 | 32 | https://www.dsca.gob.es/sites/default/files/consumo_masinfo/renta-riqueza-y-regimen-de-tenencia-%28informe3%29.pdf | `Reports/Informe3-renta-riqueza-y-regimen-de-tenencia-(informe3).pdf` | `f3b5164b79f3ce137a08f36cf33e5c2156cd87a8a1023315f2d2d386ff015b59` |
| Informe 4. El alquiler de temporada: ¿la misma vivienda con menos derechos? | 2026-11-08 | 35 | https://www.dsca.gob.es/sites/default/files/consumo_masinfo/Informe4-El_alquiler_de_temporada.pdf | `Reports/Informe4-El_alquiler_de_temporada.pdf` | `81ddc96ca7e2ee2a4dd1fdb77f65c87d91ca121195553e5ca28b1cb331d8394f` |

Informe 1 is the version currently on the server (modified 2026-04-23). It replaced my first copy, which only differed in minor wording.

Licence: Creative Commons Atribución-NoComercial-CompartirIgual 4.0 (CC BY-NC-SA 4.0), stated inside each report. I will not publish the PDFs, only links and hashes. Any derived material I publish keeps the same licence and credits the Ministry and the IFS-CSIC.

#### Documents: Observatorio de Vivienda y Suelo (8 bulletins)

Publisher: Dirección General de Vivienda y Suelo. Source: https://www.mivau.gob.es/urbanismo-y-suelo/suelo/observatorio-de-vivienda-y-suelo. Seven files are identical (same hash) to the official download. Bulletin 58 was downloaded from the official link on 2026-11-18.

The editions up to June 2023 name the Ministerio de Transportes, Movilidad y Agenda Urbana. From the annual 2023 (June 2024) it is the Ministerio de Vivienda y Agenda Urbana. I cite the name shown on each edition.

| Bulletin | Edition | Period | Pages | URL | File | SHA-256 |
|---|---|---|---|---|---|---|
| Annual 2020 | June 2021 | 2020 | 101 | https://cvp.mitma.gob.es/downloadcustom/sample/1090 | `Reports/ObservatoriodeViviendaySueloBoletnanual2020.pdf` | `2248006b93015d1102465e04a66d9977e9fe6db7afabd6c779dbba649a989b02` |
| Annual 2021 | June 2022 | 2021 | 104 | https://cvp.mitma.gob.es/downloadcustom/sample/1101 | `Reports/ObservatoriodeViviendaySueloBoletnanual2021.pdf` | `caac3565714a70a23c3281d77a21f314f8b309a51bb6b4d78077d5f259d555f9` |
| Annual 2022 | June 2023 | 2022 | 107 | https://cvp.mitma.gob.es/downloadcustom/sample/3292 | `Reports/ObservatoriodeViviendaySueloBoletnanual2022.pdf` | `f6aa21938ea5510ceef64d57ca4ec63b05bffaf7c31a97da6ed3fae29b47a1d2` |
| Annual 2023 | June 2024 | 2023 | 107 | https://publicaciones.transportes.gob.es/downloadcustom/sample/3630 | `Reports/ObservatoriodeViviendaySueloBoletnanual2023.pdf` | `1fcafca1ecb89077b77394e00ae8e626567e54e18c3c30eeb0b34224c6f32b0a` |
| Annual 2024 | June 2025 | 2024 | 110 | https://publicaciones.transportes.gob.es/downloadcustom/sample/3918 | `Reports/ObservatoriodeviviendaysueloBoletnanual2024.pdf` | `dab42ad6c1960a8a3f58632b05874043d7da07624e54f7a3f3f10171c7320c37` |
| Annual 2025 | June 2026 | 2025 | 109 | https://publicaciones.transportes.gob.es/downloadcustom/sample/4130 | `Reports/ObservatoriodeviviendaysueloBoletnanual2025.pdf` | `08e91e69291c440b697fdaedd28bcd2a38860212451099dd4de38f60153eee12` |
| No. 57, Q1 2026 | July 2026 | 2026 T1 | 67 | https://publicaciones.transportes.gob.es/downloadcustom/sample/4146 | `Reports/ObservatoriodeviviendaysueloBoletnnm57primertrimestre2026.pdf` | `beb71145550f033a890cbee7c72195d269dce9b70bc56d34d1e123ec054729c7` |
| No. 58, Q2 2026 | October 2026 | 2026 T2 | 67 | https://publicaciones.transportes.gob.es/downloadcustom/sample/4201 | `Reports/ObservatoriodeviviendaysueloBoletnnm58segundotrimestre2026.pdf` | `da5c92497cbebb376bef7cdc96a8797e48f4ea14dd1ad25a83e4d4fe1f136e5e` |

Text extraction works on all body pages of the eight files. All bulletins share the same chapters: presentation, construction and promotion, housing market (prices and transactions), land, renovation, rent, financing and access, construction sector, and housing stock. Bulletins 57 and 58 replace the housing stock chapter with bad loans and evictions.

I index four chapters: presentation, housing market, rent, and financing and access. About 55 pages per annual bulletin. The rest is left out because it is outside the questions the agent answers. Pages are PDF pages.

| Bulletin | Pages indexed | Pages left out |
|---|---|---|
| Annual 2020 | 4-5, 16-39, 51-79 | 6-15, 40-50, 80-101 |
| Annual 2021 | 4-5, 16-39, 53-82 | 6-15, 40-52, 83-104 |
| Annual 2022 | 4-5, 16-38, 52-82 | 6-15, 39-51, 83-107 |
| Annual 2023 | 4-5, 16-38, 52-82 | 6-15, 39-51, 83-107 |
| Annual 2024 | 4-5, 16-39, 53-85 | 6-15, 40-52, 86-110 |
| Annual 2025 | 4-5, 16-39, 53-84 | 6-15, 40-52, 85-109 |
| No. 57, Q1 2026 | 4, 15-32, 43-59 (includes evictions) | 5-14, 33-42, 60-67 |
| No. 58, Q2 2026 | 4, 15-32, 43-59 (includes evictions) | 5-14, 33-42, 60-67 |

Licence: the ministry website (https://www.mivau.gob.es/ministerio/aviso-legal) allows reuse citing "Origen de los datos: Ministerio de Vivienda y Agenda Urbana" and the update date. But the bulletins themselves say "Todos los derechos reservados". Since the two statements conflict, I treat the PDFs as private use and do not publish them.

#### Cross-source check: Observatorio and IPV

The Observatorio reuses the INE price index, so I checked its tables against the IPV CSV.

1. Bulletin 57, table 2.4 (p. 19, base 2025 = 100) has 25 quarterly values from 2020T1 to 2026T1. All match the national general index in the CSV to the first decimal (largest gap 0.049, rounding). For example, 2020T1 is 70.4 (CSV 70.423) and 2025T4 is 103.8 (CSV 103.805).
2. Bulletin 58 (p. 19) adds 2026T2 = 111.1 (CSV 111.095), the last period of the IPV table.
3. The annual bulletins 2020-2025 give the same index with base 2015 = 100 (2020 = 127.23, 2024 = 159.66, 2025 = 179.90). The CSV uses base 2025 = 100.
4. Rebased, they agree: 127.23 / 179.90 x 100 = 70.72, the average of the four 2020 quarters in the CSV. Same for 2022 (78.76 against 78.75) and 2024 (88.75 against 88.75). The 2025 average of the CSV is exactly 100.0.

### Employment

This block covers unemployment and work income. The table is the EPA unemployment rate, the API gives the latest values, and the documents are INE notes, labour regulation and the SEPE reports.

#### Table

| Field | Value |
|---|---|
| Title | Unemployment rate (EPA) by autonomous community, sex, age group and quarter, 2020T1-2026T3 |
| Publisher | INE |
| Retrieved | 2026-11-14 |
| URL | https://www.ine.es/jaxiT3/Tabla.htm?t=65334 |
| Licence | CC BY 4.0 (INE reuse notice, same as the IPV) |
| File | `Employment/Tasa paro por CCAA por edad por sexo por trimestres 2020_2026.csv` |
| SHA-256 | `32666a84288b46b29f12d9ffffb31dd341a7336f2d49519893ff9d9654c74856` |
| Notes | 11,340 rows (3 sexes x 7 age groups x 20 regions x 27 quarters), one value column `Total` (percentage, decimal comma), `;` separator, Windows-1252 encoding. 59 values are missing (`..`, small samples). |

Checks:
- I compared the 11,340 rows with the INE API (table 65334): 11,281 values are identical and the 59 missing values are missing in both. No value differs.
- The notes published at the time show a slightly different national rate than the table for three quarters: 2021T4 (13.33% in the note, 13.44% in the table), 2022T4 (12.87% and 12.99%) and 2023T4 (11.76% and 11.80%). The other five notes match the table exactly. The table is the current series, which INE revises, so I use the table for numbers and the notes for explanations. I did not check the cause of the revision.

#### API

| Field | Value |
|---|---|
| Title | INE API (statistics services) |
| Publisher | INE |
| Documentation | https://www.ine.es/dyngs/DAB/index.htm?cid=1099 |
| Licence | CC BY 4.0 (INE reuse notice) |
| Endpoint tested | `GET https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/65334?nult=2&tip=AM` (no key, HTTP 200, JSON, about 320 KB) |
| Tested on | 2026-11-14 (full table call repeated on 2026-11-18) |
| Fixture | `Employment/api_fixtures/ine_table_65334_last2.json` (last 2 quarters, 420 series), SHA-256 `30794adda85a266f9b672679bcdccf1acebda92fb629628bfd592b61beab120f` |

What the test call showed:
- 420 series = 3 sexes x 7 age groups x 20 territories. Each series has `COD`, `Nombre`, `MetaData` and `Data`.
- The latest quarter is 2026T3, status `Definitivo`. National total 10.18 (2026T2 = 9.87).
- Territory names have no numeric prefix in the API (`Andalucia`) but do in the CSV (`01 Andalucia`). I normalise them on ingestion.
- Missing values are returned as null where the CSV has `..`.

Function exposed to the agent (draft):

```
get_latest_unemployment_rate(
    region: str = "Total Nacional",        # one of the 20 territories (enum)
    sex: str = "Ambos sexos",              # "Ambos sexos" | "Hombres" | "Mujeres"
    age_group: str = "Total",              # "Total" | "Menores de 25 anos" | "25 y mas anos"
                                           # | "De 55 y mas anos" | "De 16 a 19 anos"
                                           # | "De 20 a 24 anos" | "De 25 a 54 anos"
    last_n_quarters: int = 1,              # 1..4
) -> {
    "series_code": "EPA452472",
    "label": "Tasa de paro de la poblacion. Ambos sexos. Canarias. Total.",
    "unit": "%",
    "values": [{"period": "2026T3", "value": 10.92, "status": "Definitivo"}],
    "source": "INE, EPA, table 65334",
    "retrieved_at": "<ISO timestamp>"
}
```

Design rules:
- The model only picks enum values. The code resolves them to a series code and builds the URL, so the model never writes URLs.
- Once the code is known I call `DATOS_SERIE/{COD}?nult=N`, a small response. The table call is only used to build the code lookup.
- Missing values return `null` with a reason, never 0.
- Timeout, one retry, a short local cache and a clear error object if the API is down.
- API for the latest values (up to 4 quarters), SQL for history, ranges, rankings and comparisons.
- Evaluation runs against the saved fixture, not the live API.

#### Documents: INE EPA press notes (8 files)

Quarterly EPA notes at key moments: the COVID quarters, the end of each year and the latest quarter. INE publishes PDFs up to 2023T3. From 2023T4 the note exists only as a web page, so I printed those pages to PDF with Chrome and their hash changes if I print them again. The columns show the national rate in the note and in the table.

| Quarter | Published | Rate in note | Rate in table | Format | URL | File | SHA-256 |
|---|---|---|---|---|---|---|---|
| 2020-T2 | 28 Jul 2020 | 15.33% | 15.33% | INE PDF | https://www.ine.es/daco/daco42/daco4211/epa0220.pdf | `Reports/INE_EPA_nota_prensa_2020-T2.pdf` | `b042d277b5dffa9c9f8e8c2b4f328f7887391e74c3d117a1e4f212570d6ac3e8` |
| 2020-T4 | 28 Jan 2021 | 16.13% | 16.13% | INE PDF | https://www.ine.es/daco/daco42/daco4211/epa0420.pdf | `Reports/INE_EPA_nota_prensa_2020-T4.pdf` | `2dd7a1c27ec4bd58cb72c8158bc657555511690e1dfc99277ac74bebc0d74493` |
| 2021-T4 | 27 Jan 2022 | 13.33% | 13.44% | INE PDF | https://www.ine.es/daco/daco42/daco4211/epa0421.pdf | `Reports/INE_EPA_nota_prensa_2021-T4.pdf` | `865aa618d74d05c3d5232b6f8032431443d043979d548bb06e73f121f342715a` |
| 2022-T4 | 26 Jan 2023 | 12.87% | 12.99% | INE PDF | https://www.ine.es/daco/daco42/daco4211/epa0422.pdf | `Reports/INE_EPA_nota_prensa_2022-T4.pdf` | `a0fb95752b036abe3e864f2c2914c0552c08d422a9946c94a93c65a3d930364b` |
| 2023-T4 | 26 Jan 2024 | 11.76% | 11.80% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/EPA4T23.htm | `Reports/INE_EPA_nota_prensa_2023-T4.pdf` | `bc4ab8f66e30c7b244d8dad4bf91ef63180e76e5e838e94573714ecca665692e` |
| 2024-T4 | 28 Jan 2025 | 10.61% | 10.61% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/EPA4T24.htm | `Reports/INE_EPA_nota_prensa_2024-T4.pdf` | `8a5f21bd4f9d142da839540cd70a593b391fd1160b028d9374ad21cbb2c2b560` |
| 2025-T4 | 27 Jan 2026 | 9.93% | 9.93% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/EPA4T25.htm | `Reports/INE_EPA_nota_prensa_2025-T4.pdf` | `7a070bf1ff33e61544aab9b75384f2c4c0045e8ea9135156505f33de3d2b56bd` |
| 2026-T3 | 27 Oct 2026 | 10.18% | 10.18% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/EPA3T26.htm | `Reports/INE_EPA_nota_prensa_2026-T3.pdf` | `6afaa6b694dc60cb1318590f92b0f53465a1141cff37beae48ad96ca1187a19f` |

The notes up to 2022 are long (27 to 35 pages with tables), the later ones are short (6 to 8 pages). Text extraction works on all of them.

#### Documents: INE labour cost notes (3 files)

Quarterly Labour Cost Survey (ETCL) notes. They give the average labour cost per worker and are the link between wages and prices. Printed to PDF from the web page.

| Quarter | Published | URL | File | SHA-256 |
|---|---|---|---|---|
| 2023-T4 | 15 Mar 2024 | https://www.ine.es/dyngs/Prensa/ETCL4T23.htm | `Reports/INE_ETCL_nota_prensa_2023-T4.pdf` | `dd9cbcf878e0ec1134fc52bff4abd15c2de9c984468fbdbc99c8b3bcae0f6b5a` |
| 2025-T4 | 17 Mar 2026 (updated 1 Jul 2026) | https://www.ine.es/dyngs/Prensa/ETCL4T25.htm | `Reports/INE_ETCL_nota_prensa_2025-T4.pdf` | `c9c04479f8ea5158858c95ccd5195c9d056fefe64dee873a23713683919c21d0` |
| 2026-T2 | 17 Sep 2026 | https://www.ine.es/dyngs/Prensa/ETCL2T26.htm | `Reports/INE_ETCL_nota_prensa_2026-T2.pdf` | `9e223fe78c3eb3469301c46b13f18edd8cd7b7a9fd19af2225a2fb86adeb9935` |

#### Documents: labour regulation (BOE, 10 files)

Labour norms that explain the period: the furlough scheme, the labour reform, the unemployment assistance reform and the yearly minimum wage (SMI) decrees. The SMI decrees have 5 pages each and give the amount of each year.

| Title | Published | In force | Version | Status | URL | File | SHA-256 |
|---|---|---|---|---|---|---|---|
| Real Decreto-ley 8/2020, urgent COVID-19 measures (includes the ERTE furlough scheme) | 2020-03-18 | 2020-03-18 | Consolidated | In force | https://www.boe.es/buscar/pdf/2020/BOE-A-2020-3824-consolidado.pdf | `Reports/BOE-A-2020-3824-consolidado.pdf` | `7de2e9a3772956fa92b67a3530b5be7df9f4ce5114a51ba637f168b86f0a457b` |
| Real Decreto 231/2020, minimum wage (SMI) 2020: 950 EUR/month, 14 payments | 2020-02-05 | 2020-02-06 | Consolidated | Applied to 2020 only (validity exhausted) | https://www.boe.es/buscar/pdf/2020/BOE-A-2020-1652-consolidado.pdf | `Reports/BOE-A-2020-1652-consolidado.pdf` | `f04921081aaddbd12785c37bb195069c584833934072a2052e7153207bde3295` |
| Real Decreto 817/2021, minimum wage (SMI) 2021: 965 EUR/month, 14 payments (from 2021-09-01) | 2021-09-29 | 2021-09-30 | Consolidated | Applied to 2021 only (validity exhausted) | https://www.boe.es/buscar/pdf/2021/BOE-A-2021-15770-consolidado.pdf | `Reports/BOE-A-2021-15770-consolidado.pdf` | `9557dbda556fce36ab777ceb87d98807d9103bb7ac1d73c969f808155cadbd1d` |
| Real Decreto-ley 32/2021, labour reform | 2021-12-30 | 2021-12-31 | Consolidated | In force | https://www.boe.es/buscar/pdf/2021/BOE-A-2021-21788-consolidado.pdf | `Reports/BOE-A-2021-21788-consolidado.pdf` | `cc3888f8115c2950dc86df41bc0074844d9e5761ad978d5310d66560d5f3ca69` |
| Real Decreto 152/2022, minimum wage (SMI) 2022: 1,000 EUR/month, 14 payments | 2022-02-23 | 2022-02-24 | Consolidated | Applied to 2022 only (validity exhausted) | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-2851-consolidado.pdf | `Reports/BOE-A-2022-2851-consolidado.pdf` | `80ea3efe3b8fceb9f2723905e452d61303a825a8792ab1bf208cde693d967ee3` |
| Real Decreto 99/2023, minimum wage (SMI) 2023: 1,080 EUR/month, 14 payments | 2023-02-15 | 2023-02-16 | Consolidated | Applied to 2023 only (validity exhausted) | https://www.boe.es/buscar/pdf/2023/BOE-A-2023-3982-consolidado.pdf | `Reports/BOE-A-2023-3982-consolidado.pdf` | `13a895f343823f4b2581910e4bec1e3765cf4271e7736a61ac4ab83e1a4d03a2` |
| Real Decreto 145/2024, minimum wage (SMI) 2024: 1,134 EUR/month, 14 payments | 2024-02-07 | 2024-02-08 | Consolidated | Applied to 2024 only (validity exhausted) | https://www.boe.es/buscar/pdf/2024/BOE-A-2024-2251-consolidado.pdf | `Reports/BOE-A-2024-2251-consolidado.pdf` | `7a872ebbb35d14983cb1ce071c599f69d4fd2b824363e1719ee53dd0c6a34d98` |
| Real Decreto-ley 2/2024, urgent measures to simplify and improve unemployment assistance | 2024-05-22 | 2024-05-23 | Consolidated | In force | https://www.boe.es/buscar/pdf/2024/BOE-A-2024-10235-consolidado.pdf | `Reports/BOE-A-2024-10235-consolidado.pdf` | `a3a3581e8f3205c6a8e04b4455a6dca9764002b0e12a121974ff0a3a66cea0e8` |
| Real Decreto 87/2025, minimum wage (SMI) 2025: 1,184 EUR/month, 14 payments | 2025-02-12 | 2025-02-13 | Consolidated | Applied to 2025 only (validity exhausted) | https://www.boe.es/buscar/pdf/2025/BOE-A-2025-2576-consolidado.pdf | `Reports/BOE-A-2025-2576-consolidado.pdf` | `1365bcd111ffc0cceca4652a6ce43701770e186a0176b6f773c785f5c5ebe6df` |
| Real Decreto 126/2026, minimum wage (SMI) 2026: 1,221 EUR/month, 14 payments | 2026-02-19 | 2026-02-20 | Consolidated | In force | https://www.boe.es/buscar/pdf/2026/BOE-A-2026-3815-consolidado.pdf | `Reports/BOE-A-2026-3815-consolidado.pdf` | `b881e1e0d27566443eac5e28d2d1add835782fc35ee0ffc3dc1cd67e4784be7a` |

#### Documents: SEPE reports (7 files)

Annual reports of the Servicio Público de Empleo Estatal and the state labour market report. All seven files are identical to the official downloads (checked 2026-11-18). The annual reports are long (224 to 289 pages) and most of the pages are about SEPE management and programmes, so I index only two chapters: the labour market indicators and the unemployment benefits. That is about 50 to 60 pages of each annual report. For the labour market report I index the summary and the four chapters. The page numbers below are PDF pages.

| Report | Covers | Pages | Pages indexed | URL | File | SHA-256 |
|---|---|---|---|---|---|---|
| Informe del mercado de trabajo estatal, data 2025 | March 2026 | 86 | 14-79 | https://sepe.es/dctm/informes:09019af480269c9c/RElTRVdFQg==/4680-704.pdf | `Reports/SEPE_informe_mercado_trabajo_estatal_datos_2025.pdf` | `39bbc6d44e3cc02a582ca115b60dd1b308e0ca1c2e501db476ed0eb5443a4db9` |
| Informe Anual SEPE 2020 | 2021 | 229 | 12-19, 115-153 | https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/publicaciones/pdf/pdf_sobre_el_sepe/2021/Informe-Anual/Informe_Anual_SEPE_2020.pdf | `Reports/SEPE_informe_anual_2020.pdf` | `2c724d89ad816ceea5d5eb3122ad87a7889e00765c626243397ea08cd734834b` |
| Informe Anual SEPE 2021 | 2022 | 241 | 17-27, 119-158 | https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/publicaciones/pdf/pdf_sobre_el_sepe/2022/Informe-Anual/Informe_Anual_SEPE_2021.pdf | `Reports/SEPE_informe_anual_2021.pdf` | `a25e455df3de691977c5bd996bcbd9e281e774c23c5c8fbb3d79df4ca7ba4bf3` |
| Informe Anual SEPE 2022 | 2023 | 224 | 17-26, 101-138 | https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/publicaciones/pdf/pdf_sobre_el_sepe/2023/Informe-Anual/Informe-Anual-SEPE_2022.pdf | `Reports/SEPE_informe_anual_2022.pdf` | `d945e41bb4402e68ccaa3921eb30a7b0338d55f06bd7144e56f3a32e89e5ed1e` |
| Informe Anual SEPE 2023 | 2024 | 281 | 15-33, 133-165 | https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/publicaciones/pdf/pdf_sobre_el_sepe/2024/informe-Anual/Informe-Anual-SEPE-2023.pdf | `Reports/SEPE_informe_anual_2023.pdf` | `9af15c69f8da5befee9bbe926fac5280ab94117c3cab3fee247239ff90377a76` |
| Informe Anual SEPE 2024 | 2025 | 289 | 16-37, 138-172 | https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/publicaciones/pdf/pdf_sobre_el_sepe/2025/Informe-Anual/SEPE_IA_2024-DEFINITIVO.pdf | `Reports/SEPE_informe_anual_2024.pdf` | `b02987d71b7679abb603666d2748ee1f3130396fc8a6ef1ac9f0fb925c89d5e2` |
| Informe Anual SEPE 2025 | 2026 | 286 | 17-38, 131-166 | https://www.sepe.es/SiteSepe/contenidos/que_es_el_sepe/publicaciones/pdf/pdf_sobre_el_sepe/2026/Informe-Anual/SEPE_IA_2025.pdf | `Reports/SEPE_informe_anual_2025.pdf` | `80e3a41272668b3e8b2c7c96ae10a1420355f486df845cced947178dd083aa42` |

The market report ("Informe del mercado de trabajo estatal") has the title "Datos 2025" and was published in 2026. One page footer says "Datos 2024", which is a typo in the source.

#### Licence notes

INE notes: CC BY 4.0, with the citation "Elaboración propia con datos extraídos del sitio web del INE: www.ine.es".

BOE: the standard BOE licence used in Housing. Reuse is allowed, citing "Basado en datos de la Agencia Estatal Boletín Oficial del Estado" and labelling the consolidated texts as informative only.

SEPE (https://www.sepe.es/HomeSepe/mas-informacion-contacto/aviso-legal.html, checked 2026-11-14): the legal notice only covers downloading and private use with the content intact. Reproduction, distribution and public communication need SEPE's authorisation. The notice also has a section on reuse of public-sector information (Ley 37/2007), but I could not confirm that these reports belong to it, so I treat them as private use. I will not publish the PDFs or their extracted text, only the manifest, download script and hashes. In the demo I show short cited excerpts with source, page and date.

### Prices

This block covers the cost of living through the consumer price index: food, housing and energy, transport and the rest of the groups. I did not add a separate fuel or commodity series. Fuel sits inside the transport group, and the documents (INE notes, Banco de España reports) explain energy and food prices.

#### Table

| Field | Value |
|---|---|
| Title | Consumer Price Index (IPC), national index, general and by ECOICOP v2 group, 2020M01-2026M10 |
| Publisher | INE |
| Retrieved | 2026-11-13 |
| URL | https://www.ine.es/jaxiT3/Tabla.htm?t=76125 (same series as table 79181) |
| Licence | CC BY 4.0 (INE reuse notice, same as the IPV) |
| File | `Prices/IPC - indice general por grupos - 2020_2026.csv` |
| SHA-256 | `100efa1c3688815c07328b47495588e5bc7385e4a55531b1c34265619b5cf7ef` |
| Notes | 1,148 rows (14 series x 82 months), `;` separator, decimal comma, Windows-1252 encoding. Index only: annual and monthly rates are computed in SQL. Latest period 2026M10. |

Classification: the table uses ECOICOP version 2 (13 groups plus the general index) with base 2025 = 100 for the whole period. The published notes use older bases: 2016 up to 2021, 2021 for 2022 and 2023, and 2025 from the 2026 notes. The older notes also use the previous groups, so names and weights differ from the table.

Checks:
- I compared all 1,148 values with the INE API (table 76125) and they all match.
- The annual rate computed from the table matches the headline annual IPC of the 18 press notes I compared (for example 9.8% in March 2022, 10.8% in July 2022, 4.9% in October 2026). The 2020 notes cannot be checked because the table has no 2019 data.

#### Documents: INE press notes (23 files)

Monthly IPC press notes from INE, chosen at key moments instead of one per year: the COVID drop (April 2020), the 2021-2022 rise and its peak (July 2022, 10.8%), the food peak (February 2023, 16.6% annual rate for food) and the later months. INE publishes a PDF for each note up to November 2023. From December 2023 the note exists only as a web page, so I printed those pages to PDF with Chrome. The first three December notes (2020, 2021, 2022) are identical to the official PDFs. I generated the others myself, so their hash changes if I print them again.

| Note | Published | Annual IPC | Format | URL | File | SHA-256 |
|---|---|---|---|---|---|---|
| 2020-04 | 14 May 2020 | -0.7% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0420.pdf | `Reports/INE_IPC_nota_prensa_2020-04.pdf` | `60a7924a57389c8fc689a53af98e3432187da3eb75582267a9c6beccde0d7fee` |
| 2020-12 | 15 Jan 2021 | -0.5% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc1220.pdf | `Reports/INE_IPC_nota_prensa_2020-12.pdf` | `947ac708e7c05f9d9ccefce0a369aaa39423f5c5cd4b4e42f8208f97760e4d7a` |
| 2021-09 | 14 Oct 2021 | 4.0% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0921.pdf | `Reports/INE_IPC_nota_prensa_2021-09.pdf` | `3da6675aeb1540dc7e8326bbbe84db23cb50f44c84f37d7fb95cac9e2c68897f` |
| 2021-12 | 14 Jan 2022 | 6.5% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc1221.pdf | `Reports/INE_IPC_nota_prensa_2021-12.pdf` | `29dafd096c17fedd513dd8c61b372d7c34b34974064f896ebd937cd86c93e226` |
| 2022-03 | 13 Apr 2022 | 9.8% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0322.pdf | `Reports/INE_IPC_nota_prensa_2022-03.pdf` | `b62e0043f438e677d32ffb769ff421e6d2073eb88872cc8508f66efd2f919724` |
| 2022-06 | 13 Jul 2022 | 10.2% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0622.pdf | `Reports/INE_IPC_nota_prensa_2022-06.pdf` | `976dba20a025bf1661105a22e9caf21e1869e1f1aa040e9b49bd08465915a5f4` |
| 2022-07 | 12 Aug 2022 | 10.8% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0722.pdf | `Reports/INE_IPC_nota_prensa_2022-07.pdf` | `548740fe331ed2af0d79dbe6707eb62ed366f4271abd6900eb79a653a845b248` |
| 2022-10 | 15 Nov 2022 | 7.3% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc1022.pdf | `Reports/INE_IPC_nota_prensa_2022-10.pdf` | `35ce8ddc1a6b994e8e59f50da2b9d1391f01b0b4fb5831ce8b607fe7eea12dca` |
| 2022-12 | 13 Jan 2023 | 5.7% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc1222.pdf | `Reports/INE_IPC_nota_prensa_2022-12.pdf` | `7a5d58ba310c49722e5be7086bb7a8f9b8ac40cdc5c61edfbbb0cdc16223ac8d` |
| 2023-01 | 15 Feb 2023 | 5.9% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0123.pdf | `Reports/INE_IPC_nota_prensa_2023-01.pdf` | `992b7fa9a5aabb560ec76395fc5eebee76afd591f027a6ff9e168d40417b61d5` |
| 2023-02 | 14 Mar 2023 | 6.0% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0223.pdf | `Reports/INE_IPC_nota_prensa_2023-02.pdf` | `fe5314120ea26fba072234e1d37ea01cecda1c8c4f9c3fe61620f2280667e723` |
| 2023-06 | 12 Jul 2023 | 1.9% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0623.pdf | `Reports/INE_IPC_nota_prensa_2023-06.pdf` | `2c9e2c9d005c62e14951726de274026f5e6c700fd7b23251caf3294661287237` |
| 2023-08 | 12 Sep 2023 | 2.6% | INE PDF | https://www.ine.es/daco/daco42/daco421/ipc0823.pdf | `Reports/INE_IPC_nota_prensa_2023-08.pdf` | `2528335d602d35af1475e8a336509581a13764ada90586f98f4ecb9cfb1e08a6` |
| 2023-12 | 12 Jan 2024 | 3.1% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC1223.htm | `Reports/INE_IPC_nota_prensa_2023-12.pdf` | `9a7fb763165af217378b056d3622d967a26846a2fc0e0013a12eddd1e70113f3` |
| 2024-01 | 15 Feb 2024 | 3.4% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC0124.htm | `Reports/INE_IPC_nota_prensa_2024-01.pdf` | `46f4af30de7a7cb31b54e8d07eb1eec33aa5303e376b463b34eb1f1559cf394f` |
| 2024-07 | 13 Aug 2024 | 2.8% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC0724.htm | `Reports/INE_IPC_nota_prensa_2024-07.pdf` | `e48743e74eff2a3f56ce5a46115d123508af644640427a952142f35463b9ef7e` |
| 2024-12 | 15 Jan 2025 | 2.8% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/es/IPC1224.htm | `Reports/INE_IPC_nota_prensa_2024-12.pdf` | `3d1a8f7c4a882dde195e4ca1ec1f24a44d7a567b851ed5d86a7d8abe370d2482` |
| 2025-05 | 13 Jun 2025 | 2.0% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC0525.htm | `Reports/INE_IPC_nota_prensa_2025-05.pdf` | `2051d580b0a14bc527e03bca6353566f8a84263d570eee7de4f07bf1b42e025c` |
| 2025-09 | 15 Oct 2025 | 3.0% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC0925.htm | `Reports/INE_IPC_nota_prensa_2025-09.pdf` | `a1d246ebf23b642f18f5f2191a2b5a70b3d7112d40188798d68e4444bae4e5bf` |
| 2025-12 | 15 Jan 2026 | 2.9% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC1225.htm | `Reports/INE_IPC_nota_prensa_2025-12.pdf` | `bc9c0e452dcd3675ad7209f0b63214ca48c2f92edf011c815b8da10ab15c617c` |
| 2026-03 | 14 Apr 2026 | 3.4% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC0326.htm | `Reports/INE_IPC_nota_prensa_2026-03.pdf` | `a2f2cb58d98f331ed648fcb33502bd07db069ff8b9536fba76a48ebf5b04d347` |
| 2026-06 | 15 Jul 2026 | 3.2% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC0626.htm | `Reports/INE_IPC_nota_prensa_2026-06.pdf` | `1c0329813830f277e13c8086317e26e92aca4a3246436c2231bb303f88782d64` |
| 2026-10 | 13 Nov 2026 | 4.9% | Web note printed to PDF | https://www.ine.es/dyngs/Prensa/IPC1026.htm | `Reports/INE_IPC_nota_prensa_2026-10.pdf` | `dd336e10742b3d9d80538b260ed84b3b565898a430f70b1f09266654c70d98ea` |

The notes up to 2023 are the long PDFs (14 to 18 pages, about 26,000 characters). The later ones are short (4 to 5 pages, 5,000 to 8,000 characters). Text extraction works on all of them.

Licence: INE, CC BY 4.0, with the citation "Elaboración propia con datos extraídos del sitio web del INE: www.ine.es".

#### Documents: Banco de España quarterly reports (5 files)

Macroeconomic projections and quarterly reports of the Banco de España. They explain inflation, energy and food prices and give forecasts. I could not find a PDF for the June 2022 report at the publisher's address, so it is not included.

| Report | Published | Pages | URL | File | SHA-256 |
|---|---|---|---|---|---|
| Informe trimestral y proyecciones macroeconómicas, June 2023 | 2023-06-19 | 42 | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/23/T2/Fich/be2302-it.pdf | `Reports/BdE_proyecciones_informe_trimestral_2023-06.pdf` | `93b133d30e91dd4bc07b1daa13123595cd440b8edf896c0b5cc6c364575a5fd0` |
| Proyecciones macroeconómicas e informe trimestral, June 2024 | 2024-06-11 | 41 | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/24/T2/Fich/be2402-it.pdf | `Reports/BdE_proyecciones_informe_trimestral_2024-06.pdf` | `82eb8942d866fa4dc0348c6db49d7eaf8308aad9ee2f3189ee799f9efc6f6e97` |
| Proyecciones macroeconómicas e informe trimestral, June 2025 | 2025-06-10 | 42 | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/25/T2/Fich/be2502-it.pdf | `Reports/BdE_proyecciones_informe_trimestral_2025-06.pdf` | `520173cbe8bf9bc9226b5b2d814c59df88406737d5ad5a477fa5b071c77644f9` |
| Proyecciones macroeconómicas e informe trimestral, June 2026 (short version) | June 2026 | 8 | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/26/T2/Fich/be2602-it.pdf | `Reports/BdE_proyecciones_informe_trimestral_2026-06.pdf` | `21d3babbf581cfe1612fbe85c6a7b2024a01fc5f08aa72100e91832b42c98de1` |
| Proyecciones macroeconómicas e informe trimestral, third quarter 2026 | October 2026 | 45 | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/26/T3/be2603-it.pdf | `Reports/BdE_proyecciones_informe_trimestral_2026-T3.pdf` | `ffb9a0c3f0398cfa1eeb059ae344280c0b8a80d0ee4f95be7f45b1959f18a0db` |

Licence (https://www.bde.es/wbe/es/pie/aviso-legal/, checked 2026-11-18): copyright Banco de España, all rights reserved. Private use is free. Other uses are allowed only if the reproduction is faithful, without altering the content, and always citing the Banco de España. Calculations made from its data are allowed with the same citation. I treat these PDFs as private use and I will not publish them.

#### Documents: MAPA food consumption (4 files)

Ministerio de Agricultura, Pesca y Alimentación, household food panel: spending, volume and average prices by product. I did not download the full 645-page report for 2025 because of its size, and I could not find the December 2024 monthly report at the usual address, so 2024 is missing.

| Document | Pages | URL | File | SHA-256 |
|---|---|---|---|---|
| La alimentación mes a mes, December 2022 (provisional data) | 16 | https://www.mapa.gob.es/dam/mapa/contenido/alimentacion/temas/consumo-y-tendencias-en-alimentacion/panel-de-consumo-alimentario/ultimos-datos/consumo-2022/mes-a-mes-alimentacion-diciembre-2022.pdf | `Reports/MAPA_alimentacion_mes_a_mes_2022-12.pdf` | `438ce8bf8f20f69ccb0a4d6f9fecdb95d7f41cb7a03f003d242724b4bc169044` |
| La alimentación mes a mes, December 2023 (provisional data) | 16 | https://www.mapa.gob.es/dam/mapa/contenido/alimentacion/temas/consumo-y-tendencias-en-alimentacion/panel-de-consumo-alimentario/ultimos-datos/consumo-2023/mes-a-mes-alimentacion-diciembre-2023.pdf | `Reports/MAPA_alimentacion_mes_a_mes_2023-12.pdf` | `bfaba835bdcc3c3f3395433a42c1bd41382d97672ec670a0003f8c926a7afaf9` |
| La alimentación mes a mes, December 2025 (provisional data) | 16 | https://www.mapa.gob.es/es/dam/jcr:381132d2-c9ab-4e68-a5dd-8ce1309e9a1c/mes-a-mes-alimentacion-diciembre-2025_V1.4735c73aea7f6d6d310947efe4eb5c4b.pdf | `Reports/MAPA_alimentacion_mes_a_mes_2025-12.pdf` | `a55690af9beb5492e517d7b530f699d2750806dbb3e250e430794656f83d4716` |
| Informe del consumo alimentario en España 2025, presentation (presented 2026-07-30) | 20 | https://www.mapa.gob.es/ca/dam/jcr:654dcbfd-fd41-49de-ae3c-a77f1c89ea47/PRESENTACI%C3%93N%20INFORME%20CONSUMO%20ALIMENTARIO%202025-final.pdf | `Reports/MAPA_informe_consumo_alimentario_2025_presentacion.pdf` | `75c894c7ad4232f8fe6475b62a2b54387a293fcf324bf04f8b74ecb7b63620c7` |

Licence: the legal notice inside each monthly report and the ministry portal (https://www.mapa.gob.es/es/atencion-al-ciudadano/aviso-legal) allow reuse citing the source and the date of the last update, except for third-party content. I cite it as "Ministerio de Agricultura, Pesca y Alimentación". I still do not publish the PDFs.

### Energy

This block covers the price of electricity. The table is the regulated price (PVPC), the API gives hourly prices, and the documents are the system reports of Red Eléctrica, the regulation that changed the price and the monthly bulletins.

#### Table

| Field | Value |
|---|---|
| Title | PVPC 2.0TD, energy term, monthly average, by territory, 2021-06 to 2026-11 |
| Publisher | Red Eléctrica (REE, Redeia) |
| Source | REData, series 1001 "PVPC" (https://www.ree.es/es/datos/mercados/precios-mercados-tiempo-real) |
| Licence | Information owned by REE: private and non-commercial informative use, citing REE and the update date (see licence notes) |
| File | `Energy/PVPC - 2020_2026.csv` |
| SHA-256 | `1ee996fb40320adb67a449c226a0eaa3b709849cc636b3a160ed74e9152c703e` |
| Notes | 660 rows, `;` separator, UTF-8. Columns: `id`, `name`, `geoid`, `geoname`, `value`, `datetime`. 5 territories x 66 months. Value in EUR/MWh. |

What the table is:
- The value is the energy term of the PVPC for the 2.0TD tariff, not the total bill. It starts in 2021-06 because the 2.0TD tariff began that month.
- Each monthly value is the average of the hourly values of the API series 1001. I checked it for October 2026: the API mean is 199.2113 and the table has 199.2113.
- The method of the PVPC changed. Since 2024 it includes a forward-price component that weighs 25% in 2024, 40% in 2025 and 55% in 2026 (Real Decreto 446/2023). Values before and after 2024 are not computed in the same way.
- The five territories have almost the same value. Península, Canarias and Baleares are identical, and Ceuta and Melilla differ by about 0.004 EUR/MWh. I do not present regional differences as real.

Cleaning I do when loading the table:
- The 660 rows are 330 unique rows repeated twice. I remove the duplicates.
- 2026-11 is a partial month (the file is from mid November). I drop it or flag it as partial.
- Names and territories have no encoding problem in the current file (UTF-8, accents correct). I still normalise them.

#### API

| Field | Value |
|---|---|
| Title | REData API, real-time markets (hourly PVPC and spot price) |
| Publisher | REE |
| Documentation | https://www.ree.es/es/datos/apidatos |
| Licence | Not stated for the API. I use REE's content conditions: cite REE and the update date, no alteration, non-commercial use |
| Endpoint tested | `GET https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=2026-11-10T00:00&end_date=2026-11-10T23:59&time_trunc=hour&geo_trunc=electric_system&geo_limit=peninsular&geo_ids=8741` (no key, HTTP 200, JSON, about 2 KB) |
| Tested on | 2026-11-18 |
| Fixture | `Energy/api_fixtures/ree_pvpc_hourly_2026-11-10.json` (24 hourly values for 2026-11-10), SHA-256 `43c89451e3b526eacb3da7eabded0f7231dce02e09e23aae8db57d1a7805dd04` |
| Link file | `Energy/API - REE - PVPC precios.url` (before: a generic page called "Consumo") |

What the test showed:
- Series 1001 is the PVPC price and the same series as the table. Series 600 is the spot market price (96 values per day without the geography filter).
- It returns hourly values only. Requests with `time_trunc=day` or `month` fail with HTTP 400, so averages are computed in my code.
- With the geography filter only the peninsular system works. Canarias and Baleares return HTTP 400.
- It accepts GET but not HEAD (HTTP 403 from the firewall). Next-day prices are already available: on 2026-11-18 the call for 2026-11-19 returned data.
- It returns errors in a JSON body with HTTP 400, for example "Los datos solicitados no están disponibles".

Function exposed to the agent (draft):

```
get_pvpc_price(
    date: str,                 # YYYY-MM-DD, a past date or tomorrow at most
) -> {
    "series_id": 1001,
    "unit": "EUR/MWh",
    "territory": "Península",
    "values": [{"hour": "2026-11-10T00:00", "value": 181.88}, ...],   # 24 values
    "summary": {"mean": ..., "min": ..., "max": ..., "cheapest_hour": ...},
    "source": "Red Eléctrica (REData), series 1001",
    "retrieved_at": "<ISO timestamp>"
}
```

Design rules:
- The model only gives the date. The code builds the URL and computes means, minimum and maximum.
- API for hourly prices of recent days (peninsular system). SQL for monthly history and for all territories.
- Timeout, one retry, a short local cache and a clear error object when the API returns HTTP 400.
- Evaluation runs against the saved fixture, not the live API.

#### Documents: REE system reports (6 files)

Annual reports on the Spanish electricity system by Red Eléctrica. They include prices, demand, generation and the regulatory framework of each year. Since 2022 REE publishes the full report only as a web site, and the PDF is a summary with the regulatory framework.

| Report | Published | Pages | URL | File | SHA-256 |
|---|---|---|---|---|---|
| Informe del sistema eléctrico español 2020 (full report) | 2021 | 100 | https://www.ree.es/sites/default/files/publication/2022/05/downloadable/inf_sis_elec_ree_2020_0.pdf | `Reports/REE_informe_sistema_electrico_2020.pdf` | `d0ce7addf472d4949366baafd56312b3c9bf8bba879795bc9662393fcd823ced` |
| Informe del sistema eléctrico español 2021 (full report) | July 2022 | 55 | https://www.sistemaelectrico-ree.es/sites/default/files/2022-08/InformeSistemaElectrico_2021.pdf | `Reports/REE_informe_sistema_electrico_2021.pdf` | `2abef6f074289b20155e252db18a279303a6b0672e5e036bd8c6744faa0a7335` |
| Informe del sistema eléctrico 2022 (summary and regulatory framework) | March 2023 | 14 | https://www.sistemaelectrico-ree.es/sites/default/files/2023-03/ISE_2022.pdf | `Reports/REE_informe_sistema_electrico_2022_resumen.pdf` | `0cab4e90d083cdc5f4899333d1d7175a45d28ec7c3428b1f469851f31203fd02` |
| Informe del sistema eléctrico 2023 (summary and regulatory framework) | March 2024 | 15 | https://www.sistemaelectrico-ree.es/sites/default/files/2024-03/ISE_2023.pdf | `Reports/REE_informe_sistema_electrico_2023_resumen.pdf` | `3f3f7311c9a59b6ee2238f5c94e8f15e10f6e205410efe278a389c426faf221b` |
| Informe del sistema eléctrico 2024 (summary and regulatory framework) | March 2025 | 16 | https://www.sistemaelectrico-ree.es/sites/default/files/2025-03/ISE_2024.pdf | `Reports/REE_informe_sistema_electrico_2024_resumen.pdf` | `ccd2eb5ef3bf243345c6e5020b8dc102c8dedf34532b0346a691dbe5c5cc3941` |
| Informe del sistema eléctrico 2025 (summary and regulatory framework) | March 2026 | 17 | https://www.sistemaelectrico-ree.es/sites/default/files/informes/2026/ise-2025.pdf | `Reports/REE_informe_sistema_electrico_2025_resumen.pdf` | `6d4ef6f018bdb03c934f1866f4f016dc6c31197516e1e66feda9270fe4713ded` |

#### Documents: regulation (BOE, 4 files)

Norms that explain the price of electricity in the period. Real Decreto-ley 6/2022 and Real Decreto-ley 8/2023, which also include energy measures, are already in Housing.

| Title | Published | In force | Version | Status | URL | File | SHA-256 |
|---|---|---|---|---|---|---|---|
| Real Decreto-ley 17/2021, urgent measures against the gas price escalation (electricity tax cuts, gas price cap) | 2021-09-15 | 2021-09-16 | Consolidated | In force | https://www.boe.es/buscar/pdf/2021/BOE-A-2021-14974-consolidado.pdf | `Reports/BOE-A-2021-14974-consolidado.pdf` | `b63a207b3de5cd42f40993abd4d4d5ec542bbe072a2259904cd839e35aa689c1` |
| Real Decreto-ley 10/2022, temporary production cost adjustment mechanism (the Iberian mechanism, gas cap) | 2022-05-14 | 2022-05-15 | Consolidated | Mechanism applied until 2023-12-31 | https://www.boe.es/buscar/pdf/2022/BOE-A-2022-7843-consolidado.pdf | `Reports/BOE-A-2022-7843-consolidado.pdf` | `0cd9d169f29265bcadf09a8fe1fa4b041091a56a666803a1d838fcf244bcae35` |
| Real Decreto-ley 3/2023, extension of the adjustment mechanism | 2023-03-29 | 2023-03-30 | Consolidated | Extends the mechanism beyond 2023-05-31 | https://www.boe.es/buscar/pdf/2023/BOE-A-2023-7937-consolidado.pdf | `Reports/BOE-A-2023-7937-consolidado.pdf` | `d88389f2411d15ee0c6d8ad6b0bcf4a17c2ebdaa2bbee4226a2a8941c471651e` |
| Real Decreto 446/2023, new PVPC calculation method (modifies RD 216/2014) | 2023-06-14 | 2023-06-15 | Original (BOE has no consolidated version) | In force. Forward-price weight in the PVPC: 25% in 2024, 40% in 2025, 55% in 2026 | https://www.boe.es/boe/dias/2023/06/14/pdfs/BOE-A-2023-14048.pdf | `Reports/BOE-A-2023-14048.pdf` | `8650620d36b069e39e8849d98d1110a8b1e3c2e58c2f25ab77ca69e1e23b197c` |

#### Documents: monthly bulletins (7 files)

"Boletín mensual de energía eléctrica" by Redeia: December bulletins from 2020 to 2025 and the September 2026 bulletin. The files are identical to the official downloads. The bulletins up to 2024 are infographics with charts and have almost no text (9,000 to 12,600 characters for 22 or 23 pages), so I do not index them and I do not use OCR. The annual reports above cover those years with real text. The 2025 and 2026 bulletins have text and I index them.

| Bulletin | Edition | Pages | Characters | Indexed | URL | File | SHA-256 |
|---|---|---|---|---|---|---|---|
| 2020-12 | 14 Jan 2021 | 22 | 10,000 | No | https://www.ree.es/sites/default/files/11_PUBLICACIONES/Documentos/Boletin_mensual_diciembre_2020.pdf | `Reports/REE_boletin_mensual_2020-12.pdf` | `e37e47605e1138afdf1dee4306def0ed4f894269458fde4eeb7f46de25f53f42` |
| 2021-12 | 17 Jan 2022 | 22 | 10,000 | No | https://www.ree.es/sites/default/files/publication/2022/01/downloadable/Boletin_mensual_Diciembre_2021_0.pdf | `Reports/REE_boletin_mensual_2021-12.pdf` | `ffc05f74ef9f107579853e127c4eb0c5e4e9c68a59082901d00e870877e19d63` |
| 2022-12 | 16 Jan 2023 | 22 | 9,400 | No | https://www.ree.es/sites/default/files/publication/2024/05/downloadable/Boletin_mensual_Diciembre_2022_0.pdf | `Reports/REE_boletin_mensual_2022-12.pdf` | `bbbd66df6e9eee1e028025ce57903463b016055334b8ba86d61d7ab73461357f` |
| 2023-12 | 16 Jan 2024 | 23 | 10,200 | No | https://www.ree.es/sites/default/files/publication/2024/05/downloadable/Boletin_mensual_diciembre_2023.pdf | `Reports/REE_boletin_mensual_2023-12.pdf` | `f7b3b1aaa436f57d89fca80548e217ef8182d7f19aacca584cdd1ac6f96d4b9c` |
| 2024-12 | 16 Jan 2025 | 23 | 12,600 | No | https://www.ree.es/sites/default/files/publication/2025/01/downloadable/Boletin_mensual_diciembre_2024.pdf | `Reports/REE_boletin_mensual_2024-12.pdf` | `00969f230329828df2018cdbce06f971bc8992361911978a5b6288674dc79bb0` |
| 2025-12 | 20 Jan 2026 | 28 | 67,000 | Yes | https://www.ree.es/sites/default/files/publication/2026/01/downloadable/boletin-mensual-diciembre-2025.pdf | `Reports/REE_boletin_mensual_2025-12.pdf` | `7bc45c9e68fb251b45ddabd229520fa861a07cca2bd30cc6c31c518c5342ddc2` |
| 2026-09 | October 2026 | 29 | 26,000 | Yes | https://www.ree.es/sites/default/files/publication/2026/10/downloadable/boletin-mensual-septiembre-2026.pdf | `Reports/REE_boletin_mensual_2026-09.pdf` | `848af537fb2bb73077023f213b8dc15bc868d770ccd735391d1e898a76fc3991` |

#### Licence notes

REE (https://www.ree.es/es/aviso-legal, checked 2026-11-18): the content belongs to REE. I may make a private copy and use the information for informative, non-commercial purposes, for example in my own web page or academic material. The conditions are: cite REE as the source, do not alter the meaning of the information or the data, and mention the date of the last update. Anything beyond that needs written authorisation. I treat the REE PDFs as private use and I will not publish them. In the demo I show short cited excerpts with source, page and date. I cite the data as "Red Eléctrica (www.ree.es)" with the date.

BOE: same standard licence as in Housing (https://www.boe.es/informacion/aviso_legal/index.php). Reuse allowed, citing "Basado en datos de la Agencia Estatal Boletín Oficial del Estado" and labelling the consolidated texts as informative only.

After this the Energy block has about 1 million characters of indexed text, compared with 150,000 before.
