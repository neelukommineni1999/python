from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime

def show_date(**context):
    print(context['ds'])

def show_var(**context):
    print(Variable.get("WAREHOUSE_URL", default_var="NOT_SET"))

with DAG(
    "context_variable_demo",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="date",
        python_callable=show_date
    )

    t2 = PythonOperator(
        task_id="var",
        python_callable=show_var
    )

    t3 = BashOperator(
        task_id="bash",
        bash_command="echo {{ ds }}"
    )

    t1 >> t2 >> t3