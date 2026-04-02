from kafka import KafkaConsumer
import json
import os

consumer = KafkaConsumer(
    "users",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    value_deserializer=lambda x: json.loads(x.decode())
)

records = {}

for message in consumer:
    data = message.value

    # deduplicate using id
    records[data["id"]] = data

    if len(records) == 5:
        break

# deterministic output
output = sorted(records.values(), key=lambda x: x["id"])

if os.path.exists("/app/output.json"):
    os.remove("/app/output.json")

with open("/app/output.json", "w") as f:
    json.dump(output, f)