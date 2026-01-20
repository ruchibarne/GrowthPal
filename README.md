Overview
This project builds an end-to-end data engineering pipeline that crawls company websites,
extracts structured content, standardizes it, and computes basic analytics.

Architecture
- Raw HTML stored in S3-like folders
- Section-based content extraction
- Standardized JSON records
- Aggregated metrics
- Orchestrated using Apache Airflow

Failure Handling
- HTTP timeouts handled
- Empty sections allowed
- DAG retries enabled

Scaling Considerations
- Website list can be expanded to n-sites
- Easy migration to S3, Spark, or distributed crawlers
- Modular task-based DAG

How to Run
1. Install dependencies
2. Start Airflow
3. Trigger `web_content_data_pipeline`
