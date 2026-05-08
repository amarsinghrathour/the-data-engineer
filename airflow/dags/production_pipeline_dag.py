"""
Portfolio DAG: API -> transform -> validate -> load -> analytics.

Implements production-style concerns:
- retries
- logging
- XCom hand-offs
- clear task boundaries
"""

from __future__ import annotations

import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.python import PythonOperator

PIPELINE_DIR = Path("/opt/airflow/projects/batch_pipeline")
if PIPELINE_DIR.exists():
    sys.path.insert(0, str(PIPELINE_DIR))
else:
    # Local fallback so DAG also parses from repo checkout.
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "projects" / "batch_pipeline"))

from etl_pipeline import extract, load, transform  # noqa: E402

logger = logging.getLogger(__name__)

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}


def extract_task(**context):
    data = extract()
    logger.info("extract_task: pulled %s rows", len(data))
    context["ti"].xcom_push(key="raw_data", value=data)


def transform_task(**context):
    raw = context["ti"].xcom_pull(key="raw_data", task_ids="extract")
    cleaned = transform(raw)
    logger.info("transform_task: transformed %s rows", len(cleaned))
    context["ti"].xcom_push(key="cleaned_data", value=cleaned)


def validate_task(**context):
    cleaned = context["ti"].xcom_pull(key="cleaned_data", task_ids="transform")
    if not cleaned:
        raise ValueError("validate_task: no rows to load")
    bad_rows = [row for row in cleaned if "@" not in row.get("email", "")]
    if bad_rows:
        raise ValueError(f"validate_task: invalid email rows: {bad_rows[:3]}")
    logger.info("validate_task: passed (%s rows)", len(cleaned))


def load_task(**context):
    data = context["ti"].xcom_pull(key="cleaned_data", task_ids="transform")
    load(data)
    logger.info("load_task: load complete")


def analytics_task():
    logger.info("analytics_task: running downstream analytics checks")
    print("Running analytics...")


with DAG(
    dag_id="production_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:
    extract_op = PythonOperator(
        task_id="extract",
        python_callable=extract_task,
    )

    transform_op = PythonOperator(
        task_id="transform",
        python_callable=transform_task,
    )

    validate_op = PythonOperator(
        task_id="validate",
        python_callable=validate_task,
    )

    load_op = PythonOperator(
        task_id="load",
        python_callable=load_task,
    )

    analytics_op = PythonOperator(
        task_id="analytics",
        python_callable=analytics_task,
    )

    extract_op >> transform_op >> validate_op >> load_op >> analytics_op
