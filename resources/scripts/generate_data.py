import json
import random
from pathlib import Path


def generate_users(n=100):
    users = []
    for i in range(1, n + 1):
        users.append(
            {
                "id": i,
                "name": f"user_{i}",
                "email": f"user{i}@test.com",
            }
        )
    return users


def generate_events(n=100):
    events = ["click", "purchase", "login"]
    return [
        {
            "user_id": random.randint(1, 100),
            "event": random.choice(events),
            "amount": random.randint(100, 1000),
        }
        for _ in range(n)
    ]


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "datasets"
    base_dir.mkdir(parents=True, exist_ok=True)

    with (base_dir / "generated_users.json").open("w", encoding="utf-8") as f:
        json.dump(generate_users(1000), f, indent=2)

    with (base_dir / "generated_events.json").open("w", encoding="utf-8") as f:
        json.dump(generate_events(1000), f, indent=2)

    print("Generated datasets:")
    print(base_dir / "generated_users.json")
    print(base_dir / "generated_events.json")
