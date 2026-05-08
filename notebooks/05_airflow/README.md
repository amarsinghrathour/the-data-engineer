# Phase 5 — Orchestration (Airflow)

**Weeks 15–17**

Learn **scheduling**, **dependencies**, **retries**, and how production teams run batch work on a clock.

**Project:** automated pipeline with retries (`05_airflow_project.ipynb`).

---

## Airflow (Docker)

**Before** these notebooks, start local Airflow:

👉 **[`airflow/README.md`](../../airflow/README.md)** — `docker compose up` in `airflow/`, then open **http://localhost:8080**.

---

## Notebooks (in order)

| File | Topic |
|------|--------|
| `01_airflow_basics.ipynb` | Why orchestration, DAGs, first DAG |
| `02_creating_dags.ipynb` | Dependencies, parallelism, XCom |
| `03_scheduling_and_retries.ipynb` | Schedules, retries, timeouts, failures |
| `04_pipeline_integration.ipynb` | ETL script + Airflow + Postgres |
| `05_airflow_project.ipynb` | Portfolio project: production-style DAG system |

Follow [`../README.md`](../README.md) — each notebook ends with **Your tasks**.
