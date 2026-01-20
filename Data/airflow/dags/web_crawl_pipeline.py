from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.crawler import crawl_websites
from src.extractor import extract_sections
from src.transformer import transform_data
from src.aggregator import aggregate_metrics

default_args = {
    "owner": "airflow",
    "retries": 2
}

with DAG(
    dag_id="web_content_data_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    crawl = PythonOperator(
        task_id="crawl_websites",
        python_callable=crawl_websites
    )

    extract = PythonOperator(
        task_id="extract_content",
        python_callable=extract_sections
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    aggregate = PythonOperator(
        task_id="aggregate_metrics",
        python_callable=aggregate_metrics
    )

    crawl >> extract >> transform >> aggregate
