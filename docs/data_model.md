# Data Model – SaaSight Analytics Platform

## Overview
The project follows a **Star Schema** design to support scalable analytics and reporting in Power BI.

---

## Tables

### Dimension Table: `dim_users`
Stores user-level attributes.

- `user_id` *(Primary Key)*
- `signup_date`
- `country`
- `device_type`

---

### Fact Table: `fact_events`
Captures user activity and feature interactions.

- `event_id` *(Primary Key)*
- `user_id` *(Foreign Key → dim_users)*
- `event_type`
- `event_timestamp`
- `feature_name`

---

### Fact Table: `fact_subscriptions`
Tracks subscription lifecycle and revenue metrics.

- `subscription_id` *(Primary Key)*
- `user_id` *(Foreign Key → dim_users)*
- `plan`
- `start_date`
- `end_date`
- `revenue`
- `is_active`

---

## Relationships

- One user can generate multiple events
- One user can hold multiple subscriptions

---

## Modeling Approach

**Star Schema**

Chosen to optimize reporting performance, simplify joins, and support business intelligence analysis.
