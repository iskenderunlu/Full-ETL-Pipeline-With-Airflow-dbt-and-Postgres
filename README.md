# Full-ETL-Pipeline-With-Airflow-dbt-and-Postgres
   Big picture — what this project does is below:  
   
   Docker Compose runs three main pieces: PostgreSQL (metadata + data), Airflow (webserver + scheduler in one container for local dev), and optionally a dbt image (but we run dbt inside the Airflow image here).
   
   Airflow orchestrates the ETL DAG:
   
   Extract (create/populate a raw_data table in Postgres)
   
   Load (insert rows into raw_data)
   
   dbt seed (loads csv seeds into the DB if present)
   
   dbt run (run models -> create transformed tables)
   
   dbt test (optional)
   
   dbt contains: profiles.yml, dbt_project.yml, seeds/ (CSV), and models/ SQL models that refer to raw_data (either via source() if created externally by Airflow, or via ref() if dbt seeds it).

## Run locally
1. Build and start:
   ```bash
   docker-compose up --build
   ```
2. Access Airflow UI: [http://localhost:8080](http://localhost:8080) (user: airflow, pass: airflow)
3. Trigger DAG: `dbt_run_pipeline`
4. Inspect Postgres:
   ```bash
   psql -h localhost -U airflow -d airflow
   SELECT * FROM analytics.users_summary;

# Note: 
 You must generate your airflow fermetkey.
   ```

