from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from etl_twitter import run_etl_twitter
import pendulum

# initalize args
default_args = {
    'owner': 'airflow',
    'depends_on_post': False,
    'start_date': datetime(2015, 12, 1),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'start_interval': '0 0 * * *'
}

# initialize DAG
dag = DAG(
    'dag_twitter',
    default_args=default_args,
    description='ETL code'
)

# initialize operators
run_etl = PythonOperator(
    task_id='execute_twitter_etl',
    python_callable=run_etl_twitter,
    dag=dag
)
