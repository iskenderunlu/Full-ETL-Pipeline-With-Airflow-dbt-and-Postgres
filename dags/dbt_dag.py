from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="dbt_run_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["dbt", "etl"],
) as dag:

    init = BashOperator(
        task_id="dbt_init",
        #bash_command="cd /opt/airflow/dbt_project && dbt debug --profiles-dir . || true",
        bash_command="cd /opt/airflow/dbt && dbt debug --profiles-dir . || true",
    )

    dbt_seed = BashOperator(
    task_id="dbt_seed",
    bash_command=(
        "cd /opt/airflow/dbt && "
        "dbt seed --profiles-dir /opt/airflow/dbt"),
    )


    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=(
            "cd /opt/airflow/dbt && "
            "dbt run --profiles-dir /opt/airflow/dbt"),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=("cd /opt/airflow/dbt && dbt test --profiles-dir /opt/airflow/dbt"),
    )

    init >> dbt_seed >> dbt_run >> dbt_test
