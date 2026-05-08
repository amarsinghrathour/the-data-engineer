"""
Batch ETL: JSONPlaceholder users → Postgres `users` table.

Used by Airflow DAGs in `airflow/dags/etl_pipeline*.py`.

Environment (override when Postgres is not on localhost — e.g. Airflow in Docker):

- `POSTGRES_HOST` (default `localhost`; try `host.docker.internal` on Docker Desktop to reach host Postgres)
- `POSTGRES_PORT` (default `5432`)
- `POSTGRES_DB` (default `de_course`)
- `POSTGRES_USER` / `POSTGRES_PASSWORD` (defaults `admin` / `admin`)
- `ETL_INPUT_PATH` (optional; read users JSON locally instead of API)

See `schema.sql` for the expected table DDL.
"""

from __future__ import annotations

import logging
import os
from typing import Any
import json
from pathlib import Path

import psycopg2

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract() -> list[dict[str, Any]]:
    input_path = os.environ.get("ETL_INPUT_PATH")
    if input_path:
        path = Path(input_path)
        logger.info("extract: loading local file %s", path)
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    url = "https://jsonplaceholder.typicode.com/users"
    logger.info("extract: GET %s", url)
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.json()


def transform(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": d["id"],
            "name": d["name"].title(),
            "email": d["email"].lower(),
        }
        for d in data
    ]


def load(data: list[dict[str, Any]]) -> None:
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
        database=os.environ.get("POSTGRES_DB", "de_course"),
        user=os.environ.get("POSTGRES_USER", "admin"),
        password=os.environ.get("POSTGRES_PASSWORD", "admin"),
    )
    cur = conn.cursor()

    for d in data:
        cur.execute(
            """
            INSERT INTO users (id, name, email)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (d["id"], d["name"], d["email"]),
        )

    conn.commit()
    conn.close()
    logger.info("load: inserted/ignored %s rows", len(data))


def run_pipeline() -> None:
    logger.info("Pipeline started")

    raw = extract()
    cleaned = transform(raw)
    load(cleaned)

    logger.info("Pipeline completed")


# --- Airflow multi-task DAG callables (XCom between tasks) ---


def extract_task() -> list[dict[str, Any]]:
    return extract()


def transform_task(**kwargs) -> list[dict[str, Any]]:
    ti = kwargs["ti"]
    raw = ti.xcom_pull(task_ids="extract_task")
    if raw is None:
        raise ValueError("transform: missing XCom from extract_task")
    return transform(raw)


def validate_task(**kwargs) -> dict[str, Any]:
    ti = kwargs["ti"]
    rows = ti.xcom_pull(task_ids="transform_task")
    if rows is None:
        raise ValueError("validate: missing XCom from transform_task")
    if not rows:
        raise ValueError("validate: empty transform output")
    for r in rows:
        if "email" not in r or "@" not in r["email"]:
            raise ValueError(f"validate: bad row {r}")
    logger.info("validate: OK (%s rows)", len(rows))
    return {"ok": True, "count": len(rows)}


def load_task(**kwargs) -> None:
    if os.environ.get("ETL_SIMULATE_FAILURE") == "1":
        logger.error("load_task: simulated failure (unset ETL_SIMULATE_FAILURE to load)")
        raise RuntimeError("Simulated load failure for alerting practice")

    ti = kwargs["ti"]
    rows = ti.xcom_pull(task_ids="transform_task")
    if rows is None:
        raise ValueError("load_task: missing XCom from transform_task")
    load(rows)
