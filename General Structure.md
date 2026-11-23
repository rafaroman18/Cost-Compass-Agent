# Simplified Overview

```
Question ─► ROUTER ─► TOOLS ─────────► SYNTHESIZER ─► Answer + sources
           (classifies) · rag_search    (writes with
                        · sql_query      the evidence)
                        · both / none
```

- **Router**: decides which tool to use and returns JSON.
- **Tools**: executed by code. `rag_search` uses the best strategy from the benchmark; `sql_query` generates, validates and runs SQL in read-only mode.
- **Synthesizer**: receives the question + evidence and writes the answer with citations.

## Three Project Blocks

| Block | What is compared | What stays fixed |
|---|---|---|
| **A. RAG Benchmark** | Retrieval strategies (naive, BM25, hybrid, reranking, rewriting) | Model, corpus, prompts |
| **B. Models** | Local, GPT, Gemini | Everything else |

## Steps

1. **Domain and data**: pick a topic with documents and tables that complement each other.
2. **Evaluation set**: ~75 labeled questions (document, SQL, both, unanswerable).
3. **Base infrastructure**: model-agnostic LLM layer with caching, Ollama running on GPU.
4. **RAG benchmark** (block A): baseline, variants, results table.
5. **SQL tool**: schema, generation, validation, retries; evaluated separately.
6. **Agent**: router, tools and synthesizer; evaluation of each stage.
7. **Model comparison** (block B): same experiments with the three models.
8. **Presentation**: demo, API, README in English with error analysis and limitations.

## What You Measure at Each Step

- Step 4: recall@k, MRR, faithfulness.
- Step 5: *execution accuracy*.
- Step 6: router accuracy and final answer quality.
- Step 7: quality, latency and cost per model.

The natural next step is **step 1**: choosing the domain. Tell me when you want to start and we'll go through it.

## Blocks

```
Block       Table (SQL)        Documents (RAG)        API (optional)
Housing     Price index        10-30 reports          —
Employment  EPA (Labour Force) 10-30 press releases   Statistics API
Prices      CPI                10-30 press releases   —
Energy      Historical prices  Regulations & reports  Electricity price API
```
