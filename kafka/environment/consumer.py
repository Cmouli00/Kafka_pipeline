import logging
from kafka import KafkaConsumer
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("consumer")

consumer = KafkaConsumer(
    "users",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode())
)

output = []

for message in consumer:
    logger.info(f"Consumed message: {message.value}")

    output.append(message.value)

    logger.info(f"Current output size: {len(output)}")

    if len(output) >= 10:
        break

logger.info("Writing output to file")

with open("/app/output.json", "w") as f:
    json.dump(output, f)

logger.info("Consumer finished successfully")