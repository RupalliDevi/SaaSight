# Data Model – SaaSight

## Tables

### 1. dim_users

* user_id (PK)
* signup_date
* country
* device_type

### 2. fact_events

* event_id (PK)
* user_id (FK)
* event_type
* event_timestamp
* feature_name

### 3. fact_subscriptions

* subscription_id (PK)
* user_id (FK)
* plan
* start_date
* end_date
* revenue
* is_active

## Relationships

* One user can have many events
* One user can have many subscriptions

## Schema Type

Star Schema
