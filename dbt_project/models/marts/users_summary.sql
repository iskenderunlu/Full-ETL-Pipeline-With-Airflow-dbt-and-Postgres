{{ config(materialized='table') }}

select
  count(*) as total_users,
  min(signup_date) as first_signup,
  max(signup_date) as last_signup
from {{ ref('stg_users') }}
