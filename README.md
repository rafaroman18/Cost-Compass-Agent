# Cost Compass

**Spain cost-of-living agent: RAG + SQL + live APIs.**

Cost Compass answers questions about the cost of living in Spain from 2020 to 2026. It crosses four areas (housing, employment, prices and energy), reads official reports and laws, queries statistical tables and calls live public APIs, and it answers with its sources.

> Status: work in progress. Steps 1 and 2 are done, step 3 is in progress. See the roadmap below.

## What it can answer

- **Facts in documents:** "What cap did Real Decreto-ley 6/2022 put on rent updates, and until when?"
- **Numbers in tables:** "Which region had the highest unemployment rate in 2026Q3?"
- **Both together:** "Did the minimum wage grow more than prices between 2020 and 2026?"
- **Live data:** "What was the cheapest hour for the electricity price on 10 November 2026?"
- **What it does not know:** when the data is not in the corpus, it says so instead of inventing an answer.

## How it works

```
Question ─► Router ─► Tools ─────────► Synthesizer ─► Answer + sources
                      · rag_search
                      · sql_query
                      · API tools
```

- **Router:** decides which tool to use.
- **Tools:** `rag_search` retrieves passages from the documents, `sql_query` queries the tables in read-only mode, and the API tools call the INE (unemployment) and Red Eléctrica (electricity price) APIs.
- **Synthesizer:** writes the answer from the evidence and cites it.

The agent is built with [Pydantic AI](https://ai.pydantic.dev/) on top of a model-agnostic LLM layer (local models with Ollama, GPT and Gemini).

## Data

| Block | Table (SQL) | Documents (RAG) | API |
|---|---|---|---|
| Housing | Housing price index (INE) | Laws (BOE), housing reports | none |
| Employment | Unemployment rate, EPA (INE) | Labour laws, INE and SEPE reports | INE statistics |
| Prices | Consumer price index (INE) | INE press notes, Banco de España, food consumption | none |
| Energy | Regulated electricity price, PVPC (REE) | Regulation, REE reports | REE electricity prices |

Every source, with its URL, licence and SHA-256 hash, is listed in [`Step 1 - Data and domain.md`](Steps/Step%201%20-%20Data%20and%20domain/Step%201%20-%20Data%20and%20domain.md).

**The data files are not in this repository.** Several licences do not allow redistributing the PDFs, so the repository only contains the manifest. The files are ignored by git.

## Evaluation

The agent is evaluated with 92 questions in Spanish (`Steps/Step 2 - Validation set/eval_set.jsonl`): 33 SQL, 24 document, 15 mixed, 10 API and 10 unanswerable. Each question has a reference answer and its sources. Some questions are traps on purpose, for example a rule that changed in its consolidated version, a repealed law or an index with a different base.

## Roadmap

| Step | Content | Status |
|---|---|---|
| 1 | Domain and data | Done |
| 2 | Validation set | Done |
| 3 | LLM layer with cache, Ollama on GPU | In progress |
| 4 | RAG benchmark: which retrieval strategy is best | Planned |
| 5 | SQL tool, evaluated separately | Planned |
| 6 | Agent: router, tools and synthesizer | Planned |
| 7 | Model comparison: local, GPT, Gemini | Planned |
| 8 | Demo, API and error analysis | Planned |

The two experiments are: which RAG strategy works best (naive, BM25, hybrid, reranking, query rewriting), measured with recall@k, MRR and faithfulness, and which model answers best and at what latency and cost.

## Results

In progress. The tables for the RAG strategies and the models will be added here.

## Setup

```bash
python3 -m venv venv_rag_agent
source venv_rag_agent/bin/activate
pip install -r requirements.txt
cp .env_example .env      # then fill in your keys
```

The data files have to be downloaded from the sources listed in the manifest.

## Repository

```
Steps/
  Step 1 - Data and domain/   manifest of sources, licences and hashes
  Step 2 - Validation set/    questions, reference answers and sources
  Step 3 - LLM layer/         agent, tools, prompts and LLM layer
General Structure.md          working plan
```

## Limitations

- The corpus is closed: documents and data until November 2026.
- The validation set has 92 questions written by me, so small differences between two models are not reliable.
- The PDFs cannot be shared, so the results can only be reproduced by downloading the sources again.
