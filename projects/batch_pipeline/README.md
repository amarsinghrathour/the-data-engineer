# Batch pipeline (ETL script)

Python module **`etl_pipeline.py`** — fetch users from [JSONPlaceholder](https://jsonplaceholder.typicode.com/), normalize fields, load into Postgres.

## Database

1. Create a database (example name: **`de_course`**).
2. Apply **`schema.sql`**:

   ```bash
   psql -h localhost -U admin -d de_course -f schema.sql
   ```

Adjust user/password to match **`POSTGRES_*`** environment variables.

## Run without Airflow

From this directory (with network access and Postgres running):

```bash
python3 -c "from etl_pipeline import run_pipeline; run_pipeline()"
```

Use local reusable fixture data instead of API calls:

```bash
ETL_INPUT_PATH=../../resources/datasets/users.json python3 -c "from etl_pipeline import run_pipeline; run_pipeline()"
```

## Run with Airflow (Docker)

The Compose file mounts this folder to **`/opt/airflow/projects/batch_pipeline`**. From **inside** the Airflow container, **`localhost`** is the container itself — not your laptop’s Postgres.

If Postgres runs on the host (Docker Desktop macOS/Windows), set for the Airflow service (see **`airflow/docker-compose.yml`**):

```yaml
environment:
  POSTGRES_HOST: host.docker.internal
```

Linux hosts may need **`extra_hosts`** or the host gateway IP — see Docker docs for your OS.

## Dependencies

`requests` and **`psycopg2-binary`** are installed at container startup via **`_PIP_ADDITIONAL_REQUIREMENTS`** in Compose.
