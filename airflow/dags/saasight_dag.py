from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="saasight_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="End-to-end SaaS data pipeline",
) as dag:

    # Step 1: Generate Data
    generate_data = BashOperator(
    task_id="generate_data",
    bash_command="""
    cd /opt/project &&
    python data_generator/generate_users.py &&
    python data_generator/generate_events.py &&
    python data_generator/generate_subscriptions.py
    """
)

    # Step 2: Load Data to Snowflake
    load_data = BashOperator(
        task_id="load_to_snowflake",
        bash_command="""
        python /opt/project/ingestion/load_to_snowflake.py
        """
    )

    # Step 3: Run dbt models
    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="""
        cd /opt/project/dbt_project/saasight_dbt &&
        python -m dbt.cli.main run
        """
    )

    # Task sequence
    generate_data >> load_data >> run_dbt