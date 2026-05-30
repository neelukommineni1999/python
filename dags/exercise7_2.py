from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def failing_task():
    raise Exception("Intentional failure")

default_args = {
    "email": ["data-support@company.com"],
    "email_on_failure": True,
    "email_on_retry": False
}

with DAG(
    dag_id="email_alert_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    task1 = PythonOperator(
        task_id="fail_task",
        python_callable=failing_task
    )