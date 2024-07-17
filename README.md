# Kafka Streaming Pipeline

This repository contains Python scripts for a Kafka streaming pipeline, including a producer (`producer.py`) and a consumer (`consumer.py`). The pipeline generates fake data, produces it to Kafka, consumes it, and transforms the messages.

## Prerequisites

Before running the scripts, ensure you have the following installed and configured:
- Python 3.x
- Kafka, Faker
- Upstash configuration for storing sensitive information securely

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Rani-jr/kafka-streaming.git
   cd kafka-streaming
   ```

2. Install dependencies:
   ```
   pip install kafka-python faker
   ```

3. Create `cfg.config` file for Upstash configuration:
   ```
   # cfg.config
   bootstrap.servers="your-upstash-endpoint"
   sasl.mechanism=SCRAM-SHA-256
   security.protocol=SASL_SSL
   sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
    username="your-upstash-username" \
    password="your-upstash-password";
   ```

4. Update `config.py` with Kafka broker details:
   ```python
   # config.py
   endpoint = "your-upstash-endpoint"
   username = "your-upstash-username"
   password = "your-upstash-password"
   ```

## Running the Pipeline

### 1. Start the Kafka Producer

Run the `producer.py` script to start producing messages to Kafka:
```
python producer.py
```

### 2. Start the Kafka Consumer

Run the `consumer.py` script to consume messages from Kafka, transform them, and save to a local file (`messages.log`):
```
python consumer.py
```

## Notes

- Adjust Kafka topic names (`'sink'` in both scripts) as per your Kafka setup.
- Ensure Upstash configuration (`cfg.config`) and Kafka credentials (`config.py`) are kept secure and not exposed in version control.
- Customize `transform_data()` function in `transform.py` as needed for your specific data transformation requirements.