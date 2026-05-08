from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract():
    print("Extracting data...")


def transform():
    print("Transforming data...")


def load():
    print("Loading data...")


with DAG(
    dag_id="etl_simple_chain_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
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
