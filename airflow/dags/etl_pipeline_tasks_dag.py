"""
Multi-task version of the batch ETL (assignment reference for notebook 04).

extract_task → transform_task → validate_task → load_task

Set environment variable ETL_SIMULATE_FAILURE=1 on the Airflow worker to simulate load failure (bonus).
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.python import PythonOperator

_BATCH = Path(__file__).resolve().parent.parent / "projects" / "batch_pipeline"
sys.path.insert(0, str(_BATCH))

from etl_pipeline import (  # noqa: E402
    extract_task,
    load_task,
    transform_task,
    validate_task,
)

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    dag_id="etl_pipeline_tasks_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    t_extract = PythonOperator(
        task_id="extract_task",
        python_callable=extract_task,
    )

    t_transform = PythonOperator(
        task_id="transform_task",
        python_callable=transform_task,
    )

    t_validate = PythonOperator(
        task_id="validate_task",
        python_callable=validate_task,
    )

    t_load = PythonOperator(
        task_id="load_task",
        python_callable=load_task,
    )

    t_extract >> t_transform >> t_validate >> t_load
