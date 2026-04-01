{{ config(materialized='table') }}

SELECT
    DATE_TRUNC('month', start_date) AS month,
    SUM(revenue) AS total_mrr
FROM SAASIGHT_DB.STAGING.STG_SUBSCRIPTIONS
WHERE is_active = TRUE
GROUP BY 1
ORDER BY 1