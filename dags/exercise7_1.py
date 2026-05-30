from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def alert_failure(context):
    task_instance = context['task_instance']
    print(f"FAILED TASK ID: {task_instance.task_id}")
    print(f"EXECUTION DATE: {context['ds']}")

def failing_task():
    raise Exception("Intentional failure")

with DAG(
    dag_id='failure_callback_example',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='test_task',
        python_callable=failing_task,
        on_failure_callback=alert_failure
    )