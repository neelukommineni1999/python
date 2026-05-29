from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def ingest():
    print("Ingest")

def transform():
    print("Transform")

with DAG(
    dag_id="exercise3_1",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest",
        python_callable=ingest,
        retries=5,
        retry_delay=timedelta(minutes=20)
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
        retries=2,
        retry_delay=timedelta(minutes=5)
    )

    ingest_task >> transform_task