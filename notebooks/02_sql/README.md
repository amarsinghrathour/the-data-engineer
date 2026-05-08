# Phase 2 — SQL & data warehousing

**Weeks 6–8**

Topics: SQL fundamentals, joins & aggregations, window functions, schema design, end-to-end SQL project.

**Project:** mini data warehouse.

---

## PostgreSQL setup (do this before notebooks)

### Option 1 — Docker (recommended)

```bash
docker run --name postgres-db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=de_course \
  -p 5432:5432 \
  -d postgres
```

Stop / remove when done:

```bash
docker stop postgres-db
docker rm postgres-db
```

### Option 2 — Local install

Install PostgreSQL locally and create database `de_course` with user/password matching what you use in the notebooks (default in this course: `admin` / `admin`).

### Python driver

Already listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Quick connection test

From repo root:

```bash
python scripts/test_postgres_connection.py
```

Or run the first cells in `01_sql_basics.ipynb`.

---

## Notebooks (in order)

| File | Topic |
|------|--------|
| `01_sql_basics.ipynb` | Connect, DDL/DML, filters, aggregates |
| `02_joins_and_aggregations.ipynb` | INNER/LEFT join, GROUP BY, HAVING |
| `03_window_functions.ipynb` | `OVER`, RANK, running totals, top-N per group |
| `04_schema_design.ipynb` | Normalization, denorm tradeoffs, indexes |
| `05_sql_project.ipynb` | E-commerce schema + analytics queries (capstone) |

Follow [`../README.md`](../README.md) — each notebook ends with **Your tasks**.
