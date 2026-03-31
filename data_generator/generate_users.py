import json
import random
from datetime import datetime, timedelta

countries = ["India", "USA", "UK", "Germany", "Canada"]
devices = ["mobile", "web"]

def generate_users(n=100):
    users = []
    for i in range(1, n+1):
        user = {
            "user_id": i,
            "signup_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
            "country": random.choice(countries),
            "device_type": random.choice(devices)
        }
        users.append(user)
    return users

if __name__ == "__main__":
    data = generate_users(100)
    with open("data/raw/users.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Users data generated!")