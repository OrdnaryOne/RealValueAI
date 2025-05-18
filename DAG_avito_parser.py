
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'RealValueAI',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG(
    'avito_real_estate_parser',
    default_args=default_args,
    description='DAG for daily parsing of Avito Real Estate',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['parser', 'avito'],
)

run_parser = BashOperator(
    task_id='run_avito_parser',
    bash_command='python /path/to/Web_scraper_Avito.py',
    dag=dag,
)
