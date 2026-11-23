# RAG Agent

## Validation set

92 questions in Spanish about the cost of living in Spain from 2020 to 2026. Each one has a reference answer and its sources, so I can score retrieval and the final answer separately.

Files:
- `eval_set.jsonl`: the questions, one per line.
- `scripts/build_reference_db.py`: builds the SQLite database used to compute the SQL answers.

### Categories

| Category | Questions | The agent needs | Answer comes from |
|---|---|---|---|
| `sql` | 33 | `sql_query` | The reference SQL on the reference database |
| `doc` | 24 | `rag_search` | A document, with file and page |
| `both` | 15 | Documents and tables | A document plus a reference SQL |
| `api` | 10 | `get_latest_unemployment_rate` or `get_pvpc_price` | The saved API fixtures |
| `no_answer` | 10 | Say that the information is not available | Nothing in the corpus |

Difficulty: 22 easy, 50 medium, 20 hard. 10 questions cross two blocks, for example the minimum wage against inflation.

### Fields

| Field | Content |
|---|---|
| `id`, `category`, `difficulty` | `SQL-01`, `doc`, `easy`... |
| `question`, `answer` | The question and the reference answer |
| `numeric` | Value, unit and tolerance of each figure, only on questions with figures |
| `sources` | Table, document with page, or API fixture |
| `sql` | The SQL that gives the number, when there is one |
| `note` | Why the question is tricky, only on a few |

### How I built the answers

- **SQL:** I wrote the query first and took the answer from its result.
- **Documents:** I read each fact and kept the file and page. All 39 cited quotes are on their page.
- **API:** the answers come from the saved fixtures (EPA 2026T3 and the hourly PVPC of 2026-11-10), not from the live API. The four EPA questions can also be answered with SQL, and I score the result, not the tool.
- **No answer:** future dates (2), dates before the data (2), topics outside the corpus (3), a missing document (2) and a granularity that does not exist (1).

### Traps

- **Consolidated text:** `DOC-03` and `DOC-21` have dates that differ between the original and the consolidated version.
- **Repealed rule:** `DOC-10` (Real Decreto-ley 2/2026).
- **Index base:** `BOTH-05` (base 2015 against base 2025).
- **Revised series:** `BOTH-03` (13.33% in the INE note, 13.44% in the table).
- **Two similar series:** `BOTH-07` (Ministry appraisals against the INE index).
- **Small difference:** `BOTH-02` (minimum wage +28.5%, prices +28.8%).
- **Annual forecast against one month:** `BOTH-15`.
- **Tool choice:** `API-05` to `API-09` need the API, and `API-10` needs the API and SQL.

### Limits

- I wrote all the questions, so they follow the wording of the documents that I know.
- With 92 questions, small differences between two models are not reliable.
- The scoring metrics belong to the next steps.
