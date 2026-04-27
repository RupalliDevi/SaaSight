# generate_users.py

import json
import random
from datetime import datetime, timedelta

COUNTRIES = [
    "USA", "Canada", "UK", "Germany",
    "India", "Australia", "Singapore", "Netherlands"
]

DEVICES = ["mobile", "web", "tablet"]


def generate_users(n=400):
    users = []

    for i in range(1, n + 1):
        signup_date = datetime.now() - timedelta(days=random.randint(30, 500))

        user = {
            "user_id": i,
            "signup_date": signup_date.strftime("%Y-%m-%d"),
            "country": random.choice(COUNTRIES),
            "device_type": random.choice(DEVICES)
        }

        users.append(user)

    return users


if __name__ == "__main__":
    data = generate_users(400)

    with open("data/raw/users.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Users data generated successfully!")