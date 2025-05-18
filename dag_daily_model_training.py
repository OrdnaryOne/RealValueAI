from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'RealValueAI',
    'depends_on_past': False,
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

with DAG(
    dag_id='daily_model_training',
    default_args=default_args,
    description='Daily training of real estate ML models',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['training'],
) as dag:

    run_training = BashOperator(
        task_id='run_model_training',
        bash_command='python3 /opt/airflow/dags/scripts/fit_model.py',
    )

    run_training
