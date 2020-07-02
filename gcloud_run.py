from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta 




default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'email': ['kishorebd2500@gmail.com','kishore.lovt2500.kb@gmail.com'],
    'email_on_success':True,
    'email_on_failure':True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


dag = DAG('run_in_gcloud', default_args=default_args, schedule_interval=None) 

with dag:

    start_instance = BashOperator(
        task_id= 'instance_starting',
        bash_command='gcloud compute instances start shobdokutir-gpu-2',
        dag = dag
    )
    run_file = BashOperator(
        task_id= 'running_program',
        bash_command='bash /home/kishore/NLP/remote_run.sh ',
        dag = dag
    )
    stop_instance = BashOperator(
        task_id= 'stop_instance',
        bash_command='gcloud compute instances stop shobdokutir-gpu-2',
        dag = dag
    )


start_instance >> run_file >> stop_instance