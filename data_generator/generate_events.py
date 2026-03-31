import json
import random
from datetime import datetime, timedelta

event_types = ["login", "feature_use"]
features = ["search", "dashboard", "analytics", "export"]

def generate_events(n=500):
    events = []
    for i in range(1, n+1):
        event = {
            "event_id": i,
            "user_id": random.randint(1, 100),
            "event_type": random.choice(event_types),
            "event_timestamp": (datetime.now() - timedelta(minutes=random.randint(1, 10000))).strftime("%Y-%m-%d %H:%M:%S"),
            "feature_name": random.choice(features)
        }
        events.append(event)
    return events

if __name__ == "__main__":
    data = generate_events(500)
    with open("data/raw/events.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Events data generated!")