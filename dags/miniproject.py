from airflow import DAG
from airflow.operators.python import PythonOperator, get_current_context
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import pandas as pd
import os
import logging


# CONFIG PATHS
BASE_PATH = "/opt/airflow/data"
WAREHOUSE_PATH = f"{BASE_PATH}/warehouse.csv"
LOOKUP_PATH = f"{BASE_PATH}/region_lookup.csv"


# FAILURE CALLBACK
def on_failure_callback(context):
    task_id = context["task_instance"].task_id
    ds = context["ds"]
    logging.error(f"FAILED TASK: {task_id} | DATE: {ds}")


# TASK 2: VALIDATION
def validate_records():
    context = get_current_context()
    ds = context["ds"]

    file_path = f"{BASE_PATH}/shipment_{ds}.csv"
    df = pd.read_csv(file_path)

    required_columns = ["shipment_id", "region", "weight"]

    logging.info(f"Row count: {len(df)} for date {ds}")

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    null_rates = df[required_columns].isnull().mean()
    logging.info(f"NULL rates: {null_rates.to_dict()}")

    for col, rate in null_rates.items():
        if rate > 0.05:
            raise ValueError(f"NULL rate > 5% in {col}: {rate}")


# TASK 3: TRANSFORM
def transform_records():
    context = get_current_context()
    ds = context["ds"]

    input_file = f"{BASE_PATH}/shipment_{ds}.csv"
    output_file = f"{BASE_PATH}/transformed_{ds}.csv"

    df = pd.read_csv(input_file)

    df.columns = [c.lower().strip() for c in df.columns]
    df = df.drop_duplicates()

    lookup = pd.read_csv(LOOKUP_PATH)
    df = df.merge(lookup, on="region", how="left")

    df.to_csv(output_file, index=False)
    logging.info(f"Transform completed for {ds}")


# TASK 4: LOAD
def load_to_warehouse():
    context = get_current_context()
    ds = context["ds"]

    file_path = f"{BASE_PATH}/transformed_{ds}.csv"
    new_df = pd.read_csv(file_path)

    new_df["ds"] = ds

    if os.path.exists(WAREHOUSE_PATH):
        warehouse_df = pd.read_csv(WAREHOUSE_PATH)
        warehouse_df = warehouse_df[warehouse_df["ds"] != ds]
        final_df = pd.concat([warehouse_df, new_df], ignore_index=True)
    else:
        final_df = new_df

    final_df.to_csv(WAREHOUSE_PATH, index=False)
    logging.info(f"Loaded data for {ds}")


# DAG DEFAULTS
default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": on_failure_callback
}


# DAG
with DAG(
    dag_id="logistics_daily_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 2 * * *",
    catchup=False,
    tags=["logistics", "pipeline"]
) as dag:

    # TASK 1: FILE ARRIVAL CHECK
    check_file_arrival = FileSensor(
        task_id="check_file_arrival",
        filepath=f"{BASE_PATH}/shipment_{{{{ ds }}}}.csv",
        poke_interval=20 * 60,
        timeout=60 * 60 * 5,
        mode="reschedule",
        retries=5,
        on_failure_callback=on_failure_callback
    )

    validate = PythonOperator(
        task_id="validate_records",
        python_callable=validate_records
    )

    transform = PythonOperator(
        task_id="transform_records",
        python_callable=transform_records
    )

    load = PythonOperator(
        task_id="load_to_warehouse",
        python_callable=load_to_warehouse
    )

    # FLOW
    check_file_arrival >> validate >> transform >> load