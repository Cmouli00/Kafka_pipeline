import subprocess
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pipeline")

logger.info("Starting Zookeeper...")
subprocess.Popen([
    "/kafka/bin/zookeeper-server-start.sh",
    "/kafka/config/zookeeper.properties"
])

time.sleep(3)

logger.info("Starting Kafka broker...")
subprocess.Popen([
    "/kafka/bin/kafka-server-start.sh",
    "/kafka/config/server.properties"
])

time.sleep(5)

logger.info("Creating topic 'users'...")
subprocess.run([
    "/kafka/bin/kafka-topics.sh",
    "--create",
    "--topic", "users",
    "--bootstrap-server", "localhost:9092",
    "--partitions", "1",
    "--replication-factor", "1"
])

time.sleep(2)

logger.info("Running producer...")
subprocess.run(["python", "producer.py"])

logger.info("Running consumer...")
subprocess.run(["python", "consumer.py"])

logger.info("Pipeline execution completed")