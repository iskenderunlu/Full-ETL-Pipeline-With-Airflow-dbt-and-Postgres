{{ config(materialized='table') }}

with raw as (
    select
      id::int as id,
      first_name,
      last_name,
      email,
      signup_date::date as signup_date
    from {{ ref('users') }}
)

select * from raw
