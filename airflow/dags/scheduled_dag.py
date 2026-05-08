"""Cron-scheduled DAG example (notebook 03)."""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def task():
    print("Running scheduled task")


with DAG(
    dag_id="scheduled_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 2 * * *",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="task1",
        python_callable=task,
    )
