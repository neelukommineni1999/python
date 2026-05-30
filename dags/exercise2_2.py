from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ingest():
    print("Ingest")

def validate():
    print("Validate")

def report():
    print("Report")

with DAG(
    dag_id="exercise2_2",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest",
        python_callable=ingest
    )

    validate_task = PythonOperator(
        task_id="validate",
        python_callable=validate
    )

    report_task = PythonOperator(
        task_id="report",
        python_callable=report
    )

    # parallel execution
    [ingest_task, validate_task] >> report_task