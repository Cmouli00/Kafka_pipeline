FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Install Java (required for Kafka)
RUN apt-get update && apt-get install -y default-jre wget

# Download Kafka
RUN wget -q https://archive.apache.org/dist/kafka/3.7.0/kafka_2.13-3.7.0.tgz \
    && tar -xzf kafka_2.13-3.7.0.tgz \
    && mv kafka_2.13-3.7.0 /kafka \
    && rm kafka_2.13-3.7.0.tgz

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]