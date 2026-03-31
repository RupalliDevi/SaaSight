import json
import random
from datetime import datetime, timedelta

plans = ["free", "pro", "enterprise"]

def generate_subscriptions(n=100):
    subs = []
    for i in range(1, n+1):
        start = datetime.now() - timedelta(days=random.randint(1, 365))
        end = start + timedelta(days=random.randint(30, 180))

        sub = {
            "subscription_id": i,
            "user_id": random.randint(1, 100),
            "plan": random.choice(plans),
            "start_date": start.strftime("%Y-%m-%d"),
            "end_date": end.strftime("%Y-%m-%d"),
            "revenue": random.randint(0, 500),
            "is_active": random.choice([True, False])
        }
        subs.append(sub)
    return subs

if __name__ == "__main__":
    data = generate_subscriptions(100)
    with open("data/raw/subscriptions.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Subscriptions data generated!")