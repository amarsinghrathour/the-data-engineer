"""
Airflow wrapper around `projects/batch_pipeline/etl_pipeline.py` (single-task DAG).

Requires Compose volume mount `../projects/batch_pipeline` → `/opt/airflow/projects/batch_pipeline`.
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.python import PythonOperator

_BATCH = Path(__file__).resolve().parent.parent / "projects" / "batch_pipeline"
sys.path.insert(0, str(_BATCH))

from etl_pipeline import run_pipeline  # noqa: E402

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    dag_id="etl_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline,
    )
