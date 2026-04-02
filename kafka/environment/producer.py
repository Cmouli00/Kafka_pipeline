import logging
from kafka import KafkaProducer
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("producer")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode()
)

with open("data.json") as f:
    data = json.load(f)

for record in data:
    logger.info(f"Sending record: {record}")
    producer.send("users", record)

    logger.info(f"Retrying send for record: {record}")
    producer.send("users", record)

producer.flush()

logger.info("Producer finished sending messages")