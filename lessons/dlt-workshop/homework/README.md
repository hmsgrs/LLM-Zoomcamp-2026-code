# dlt + Logfire homework

## Setup

Create a virtual environment and install dependencies:

```bash
uv init --no-readme
uv sync
```

Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY`:

```bash
cp .env.example .env
```

Add `OPENAI_API_KEY`, `LOGFIRE_TOKEN`, and `LOGFIRE_READ_TOKEN` to `.env`.
Set `LOGFIRE_REGION=eu` if your Logfire project is in the EU region.

## Run the agent

```bash
uv run python main.py
uv run python main.py --question "When does the course start?"
```

This sends the Question 1 run (`How do I run Ollama locally?`) to Logfire.

## Load and query traces

```bash
uv run python logfire_pipeline.py
uv run dlt pipeline logfire_pipeline show
```

The DuckDB file is `logfire_pipeline.duckdb`. Run the SQL in `queries.sql` with
DuckDB after the load to answer Questions 2 and 3. The second query lists the
actual normalized columns because the exact shape of Logfire attributes can
vary by Logfire and Pydantic AI versions.

## Files

- `ingest.py` — downloads the course FAQ and builds the search index
- `agent.py` — the FAQ agent built with Pydantic AI (system prompt + search tool)
- `main.py` — entry point that wires everything together
- `logfire_pipeline.py` — loads Logfire trace records into DuckDB with dlt
- `queries.sql` — DuckDB queries for Questions 2 and 3
