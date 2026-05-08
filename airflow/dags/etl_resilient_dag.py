"""
Resilient ETL pattern: schedule + retries + timeout + optional simulated failure.

Assignment reference for notebook `03_scheduling_and_retries.ipynb`.

Set SIMULATE_TRANSFORM_FAILURE = True to force failures and watch retries in the UI.
"""

import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

logger = logging.getLogger(__name__)

# Set True to force failures and watch retries in the UI (notebook 03 assignment).
SIMULATE_TRANSFORM_FAILURE = False


def extract():
    logger.info("extract: starting")
    print("Extracting data...")


def transform():
    logger.info("transform: starting")
    if SIMULATE_TRANSFORM_FAILURE:
        logger.warning("transform: simulated failure (disable SIMULATE_TRANSFORM_FAILURE for success)")
        raise RuntimeError("Simulated transform failure — retries should kick in")
    print("Transforming data...")


def load():
    logger.info("load: starting")
    print("Loading data...")


with DAG(
    dag_id="etl_resilient_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
        "execution_timeout": timedelta(minutes=5),
    },
) as dag:

    task_extract = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    task_transform = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    task_load = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    task_extract >> task_transform >> task_load
