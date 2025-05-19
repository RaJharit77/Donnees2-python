from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 5, 7),
}

with DAG(
    dag_id='hello_etl',
    schedule='@daily',
    default_args=default_args,
    catchup=False
) as dag:

    def extract():
        print("Étape 1 : Extraction de données")

    def transform():
        print("Étape 2 : Transformation de données")

    def load():
        print("Étape 3 : Chargement des données")

    t1 = PythonOperator(
        task_id='extract_task',
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id='transform_task',
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id='load_task',
        python_callable=load
    )

    # Dépendances : t1 >> t2 >> t3
    t1 >> t2 >> t3