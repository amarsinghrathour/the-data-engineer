"""Retries + random failures for UI observation (notebook 03)."""

import random
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def unstable_task():
    if random.random() < 0.7:
        raise RuntimeError("Random failure")
    print("Success")


with DAG(
    dag_id="retry_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(seconds=10),
    },
) as dag:

    t1 = PythonOperator(
        task_id="unstable_task",
        python_callable=unstable_task,
    )
