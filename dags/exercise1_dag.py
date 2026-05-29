from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello_airflow():
    print("Hello from Airflow in Docker!")

with DAG(
    dag_id="exercise1_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="print_hello",
        python_callable=hello_airflow
    )

    task1