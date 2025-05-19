from airflow import DAG
from airflow.operators.empty import EmptyOperator  # type: ignore 
from datetime import datetime

with DAG(
    'test_dag',
    start_date=datetime(2024, 1, 1),
    schedule=None
) as dag:
    EmptyOperator(task_id='dummy')