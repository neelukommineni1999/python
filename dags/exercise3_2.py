from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def report():
    print("Report task running")

with DAG(
    dag_id="exercise3_2",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    report_task = PythonOperator(
        task_id="report",
        python_callable=report,
        sla=timedelta(hours=3)
    )