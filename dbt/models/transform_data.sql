{{ config(materialized='table') }}

SELECT
    id,
    name,
    value * 2 AS doubled_value
FROM {{ ref('raw_data') }}
