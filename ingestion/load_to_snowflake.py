import pandas as pd
import snowflake.connector

# Snowflake connection
conn = snowflake.connector.connect(
    user= "RUPALLIDEVI",
    password= "HakunaMatata@12",
    account= "QNUASBW-ZF05188",
    warehouse="COMPUTE_WH",
    database="SAASIGHT_DB",
    schema="RAW",
    role="ACCOUNTADMIN"
)

cursor = conn.cursor()

# Optional: clear old data before loading
cursor.execute("TRUNCATE TABLE users")
cursor.execute("TRUNCATE TABLE events")
cursor.execute("TRUNCATE TABLE subscriptions")

# ---------------- USERS ----------------
users_df = pd.read_csv("/opt/project/data/users.csv")

for _, row in users_df.iterrows():
    cursor.execute(
        """
        INSERT INTO users (user_id, signup_date, country, device_type)
        VALUES (%s, %s, %s, %s)
        """,
        tuple(row)
    )

# ---------------- EVENTS ----------------
events_df = pd.read_csv("/opt/project/data/events.csv")

for _, row in events_df.iterrows():
    cursor.execute(
        """
        INSERT INTO events (event_id, user_id, event_type, event_timestamp)
        VALUES (%s, %s, %s, CURRENT_TIMESTAMP())
        """,
        tuple(row)
    )

# ---------------- SUBSCRIPTIONS ----------------
subs_df = pd.read_csv("/opt/project/data/subscriptions.csv")

for _, row in subs_df.iterrows():
    cursor.execute(
        """
        INSERT INTO subscriptions
        (subscription_id, user_id, plan, start_date, end_date, amount)
        VALUES (%s, %s, %s, CURRENT_DATE(), DATEADD(month, 1, CURRENT_DATE()), 99.99)
        """,
        tuple(row)
    )

conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully into Snowflake.")