# Local Apache Airflow (Docker)

Minimal **Apache Airflow 2.7** setup with the **`standalone`** command — good for learning DAGs without wiring Postgres + Redis manually.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose

## Run

From this directory (`airflow/`):

```bash
docker compose up
```

The Compose file mounts **`../projects/batch_pipeline`** into the container and installs **`requests`** / **`psycopg2-binary`** on startup (`_PIP_ADDITIONAL_REQUIREMENTS`). The first boot may take longer while packages install.

When the container is ready, open:

👉 **http://localhost:8080**

### Login

Airflow **standalone** creates an admin user on first boot. Check the container logs for the generated username/password — many releases still default to **`airflow` / `airflow`** if nothing else is printed.

```bash
docker compose logs airflow 2>&1 | head -80
```

If login fails, recreate the volume/container after checking [Airflow Docker docs](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

## DAGs

Place DAG files in **`dags/`** — they are mounted into the container at `/opt/airflow/dags`.

Example DAGs in **`dags/`**:

| File | DAG ID | Notes |
|------|--------|--------|
| `simple_dag.py` | `simple_dag` | Notebook `01_airflow_basics.ipynb` |
| `etl_dag.py` | `etl_simple_chain_dag` | Linear print-chain demo (notebook `02_creating_dags.ipynb`) |
| `users_pipeline_dag.py` | `users_pipeline_dag` | Parallel branches + XCom (notebook `02_creating_dags.ipynb`) |
| `scheduled_dag.py` | `scheduled_dag` | Cron schedule (`0 2 * * *`) — notebook `03_scheduling_and_retries.ipynb` |
| `retry_dag.py` | `retry_dag` | Random failures + retries |
| `timeout_dag.py` | `timeout_dag` | `execution_timeout` demo |
| `etl_resilient_dag.py` | `etl_resilient_dag` | ETL + retries + timeout + simulated failure |
| `etl_pipeline_dag.py` | `etl_pipeline_dag` | Runs **`projects/batch_pipeline/etl_pipeline.py`** (`run_pipeline`) — notebook `04_pipeline_integration.ipynb` |
| `etl_pipeline_tasks_dag.py` | `etl_pipeline_tasks_dag` | Same ETL split into tasks + validation (assignment pattern) |
| `production_pipeline_dag.py` | `production_pipeline` | Portfolio capstone DAG: API -> transform -> validate -> load -> analytics (notebook `05_airflow_project.ipynb`) |

## Stop

`Ctrl+C` in the terminal, or:

```bash
docker compose down
```
