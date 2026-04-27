# generate_subscriptions.py

import json
import random
from datetime import datetime, timedelta

PLANS = {
    "Basic": 49.99,
    "Premium": 99.99,
    "Enterprise": 199.99
}


def generate_subscriptions(n=800):
    subscriptions = []

    for i in range(1, n + 1):
        start_date = datetime.now() - timedelta(days=random.randint(30, 500))
        duration_days = random.randint(30, 180)
        end_date = start_date + timedelta(days=duration_days)

        plan = random.choices(
            ["Basic", "Premium", "Enterprise"],
            weights=[50, 35, 15]
        )[0]

        is_active = random.choices(
            [True, False],
            weights=[80, 20]
        )[0]

        sub = {
            "subscription_id": i,
            "user_id": random.randint(1, 400),
            "plan": plan,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "revenue": PLANS[plan],
            "is_active": is_active
        }

        subscriptions.append(sub)

    return subscriptions


if __name__ == "__main__":
    data = generate_subscriptions(800)

    with open("data/raw/subscriptions.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Subscriptions data generated successfully!")