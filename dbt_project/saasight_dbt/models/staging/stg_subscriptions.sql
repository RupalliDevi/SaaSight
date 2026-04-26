select
    subscription_id,
    user_id,
    plan,
    start_date,
    end_date,
    amount
from {{ source('raw', 'subscriptions') }}