
  
    

  create  table "airflow"."public_public"."transform_data__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    id,
    name,
    value * 2 AS doubled_value
FROM "airflow"."public"."raw_data"
  );
  