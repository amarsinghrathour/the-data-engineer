from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello():
    print("Hello Airflow!")


with DAG(
    dag_id="simple_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="hello_task",
        python_callable=hello,
    )
