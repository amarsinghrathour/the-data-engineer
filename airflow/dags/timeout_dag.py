"""Execution timeout on tasks (notebook 03)."""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def bounded_task():
    print("Finishes quickly — within execution_timeout")


with DAG(
    dag_id="timeout_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "execution_timeout": timedelta(seconds=30),
    },
) as dag:

    PythonOperator(
        task_id="bounded_task",
        python_callable=bounded_task,
    )
