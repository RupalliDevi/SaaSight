{{ config(materialized='table') }}

SELECT
    DATE_TRUNC('month', event_timestamp) AS month,
    COUNT(DISTINCT user_id) AS active_users
FROM {{ ref('stg_events') }}
GROUP BY 1
ORDER BY 1