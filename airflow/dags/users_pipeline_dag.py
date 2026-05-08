"""
Assignment DAG (notebook 02): parallel branches + XCom + logging.

Flow: extract_users → [transform_users, validate_data] → load_users
"""

import logging

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

logger = logging.getLogger(__name__)


def extract_users():
    logger.info("extract_users: starting")
    return {"users": [{"id": 1, "name": "Ada"}, {"id": 2, "name": "Grace"}]}


def transform_users(ti):
    payload = ti.xcom_pull(task_ids="extract_users")
    logger.info("transform_users: received XCom from extract_users: %s", payload)
    users = payload.get("users", []) if isinstance(payload, dict) else []
    out = [{"id": u["id"], "name": u["name"].upper()} for u in users]
    logger.info("transform_users: normalized %d rows", len(out))
    return {"users_normalized": out}


def validate_data(ti):
    payload = ti.xcom_pull(task_ids="extract_users")
    logger.info("validate_data: received XCom from extract_users: %s", payload)
    if not payload or not payload.get("users"):
        raise ValueError("validate_data: empty extract payload")
    logger.info("validate_data: OK")
    return {"valid": True, "count": len(payload["users"])}


def load_users(ti):
    transformed = ti.xcom_pull(task_ids="transform_users")
    validation = ti.xcom_pull(task_ids="validate_data")
    logger.info(
        "load_users: transform=%s validation=%s",
        transformed,
        validation,
    )
    logger.info("load_users: load complete")


with DAG(
    dag_id="users_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    task_extract = PythonOperator(
        task_id="extract_users",
        python_callable=extract_users,
    )

    task_transform = PythonOperator(
        task_id="transform_users",
        python_callable=transform_users,
    )

    task_validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    task_load = PythonOperator(
        task_id="load_users",
        python_callable=load_users,
    )

    task_extract >> [task_transform, task_validate] >> task_load
