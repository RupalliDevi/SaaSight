{{ config(materialized='table') }}

select
    count(*) as total_customers,
    count(case when end_date < current_date then 1 end) as churned_customers
from {{ ref('stg_subscriptions') }}