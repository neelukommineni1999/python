from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def file_check():
    print("Checking file")

def row_validation():
    print("Validating rows")

def schema_validation():
    print("Validating schema")

def load_warehouse():
    print("Loading data into warehouse")

with DAG(
    dag_id="validation_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    file_check_task = PythonOperator(task_id="file_check", python_callable=file_check)

    row_task = PythonOperator(task_id="row_validation", python_callable=row_validation)

    schema_task = PythonOperator(task_id="schema_validation", python_callable=schema_validation)

    load_task = PythonOperator(task_id="load_warehouse", python_callable=load_warehouse)

    file_check_task >> [row_task, schema_task] >> load_task