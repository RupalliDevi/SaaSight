{{ config(materialized='table') }}

select
    sum(amount) as total_mrr
from {{ ref('stg_subscriptions') }}