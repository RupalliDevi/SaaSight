# generate_events.py

import json
import random
from datetime import datetime, timedelta

EVENT_TYPES = [
    "login",
    "feature_use",
    "upgrade",
    "cancel",
    "renew",
    "support_ticket"
]

FEATURES = [
    "search",
    "dashboard",
    "analytics",
    "export",
    "alerts",
    "reports"
]


def generate_events(n=3000):
    events = []

    for i in range(1, n + 1):
        timestamp = datetime.now() - timedelta(
            days=random.randint(1, 500),
            minutes=random.randint(1, 1440)
        )

        event_type = random.choices(
            EVENT_TYPES,
            weights=[40, 30, 10, 5, 10, 5]
        )[0]

        event = {
            "event_id": i,
            "user_id": random.randint(1, 400),
            "event_type": event_type,
            "event_timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "feature_name": random.choice(FEATURES)
        }

        events.append(event)

    return events


if __name__ == "__main__":
    data = generate_events(3000)

    with open("data/raw/events.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Events data generated successfully!")