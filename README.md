# ETL pipeline: Airflow + dbt + Postgres (Docker Compose starter)

## Run locally
1. Build and start:
   ```bash
   docker-compose up --build
   ```
2. Access Airflow UI: [http://localhost:8080](http://localhost:8080) (user: admin, pass: admin)
3. Trigger DAG: `dbt_run_pipeline`
4. Inspect Postgres:
   ```bash
   psql -h localhost -U airflow -d airflow
   SELECT * FROM analytics.users_summary;
   ```
# Full-ETL-Pipeline-With-Airflow-dbt-and-Postgres
