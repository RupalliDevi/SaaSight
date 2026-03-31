import json
import snowflake.connector

# 🔐 Replace with your credentials
conn = snowflake.connector.connect(
    user="RUPALLIDEVI",
    password="HakunaMatata@12",
    account="QNUASBW-ZF05188",
    warehouse="COMPUTE_WH",
    database="SAASIGHT_DB",
    schema="RAW"
)

cur = conn.cursor()

# 🔹 Load Users
with open("data/raw/users.json") as f:
    users = json.load(f)

for u in users:
    cur.execute(f"""
        INSERT INTO USERS VALUES (
            {u['user_id']},
            '{u['signup_date']}',
            '{u['country']}',
            '{u['device_type']}'
        )
    """)

print("Users loaded!")

# 🔹 Load Events
with open("data/raw/events.json") as f:
    events = json.load(f)

for e in events:
    cur.execute(f"""
        INSERT INTO EVENTS VALUES (
            {e['event_id']},
            {e['user_id']},
            '{e['event_type']}',
            '{e['event_timestamp']}',
            '{e['feature_name']}'
        )
    """)

print("Events loaded!")

# 🔹 Load Subscriptions
with open("data/raw/subscriptions.json") as f:
    subs = json.load(f)

for s in subs:
    cur.execute(f"""
        INSERT INTO SUBSCRIPTIONS VALUES (
            {s['subscription_id']},
            {s['user_id']},
            '{s['plan']}',
            '{s['start_date']}',
            '{s['end_date']}',
            {s['revenue']},
            {str(s['is_active']).upper()}
        )
    """)

print("Subscriptions loaded!")

cur.close()
conn.close()