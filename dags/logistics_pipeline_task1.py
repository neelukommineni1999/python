from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# ---------------- FAILURE CALLBACK ----------------
def on_failure(context):
    print(f"FAILED TASK: {context['task_instance'].task_id} | DATE: {context['ds']}")

# ---------------- TASK FUNCTIONS ----------------
def file_check(**context):
    date = context['ds']
    path = f'/data/shipments/{date}.csv'  # we will break this later

    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")

    print(f"File found: {path}")

def validate(**context):
    print(f"Validating data for {context['ds']}")

def transform(**context):
    print(f"Transforming data for {context['ds']}")

def load(**context):
    print(f"Loading data for {context['ds']}")

def send_report(**context):
    print(f"Sending report for {context['ds']}")

# ---------------- DAG ----------------
with DAG(
    dag_id='logistics_pipeline_task1',
    start_date=datetime(2024, 1, 1),
    schedule='0 2 * * *',
    catchup=False,
    default_args={
        'retries': 3,
        'retry_delay': timedelta(minutes=10),
        'on_failure_callback': on_failure
    }
) as dag:

    t1 = PythonOperator(
        task_id='file_check',
        python_callable=file_check,
        retries=5,
        retry_delay=timedelta(minutes=15)
    )

    t2 = PythonOperator(task_id='validate', python_callable=validate)
    t3 = PythonOperator(task_id='transform', python_callable=transform)
    t4 = PythonOperator(task_id='load', python_callable=load)
    t5 = PythonOperator(task_id='send_report', python_callable=send_report)

    t1 >> t2 >> t3 >> [t4, t5]