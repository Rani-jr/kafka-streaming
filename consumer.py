from kafka import KafkaConsumer
import json
import logging
from config import endpoint, username, password
from transform import transform_data

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_kafka_consumer() -> KafkaConsumer:
    """Create and return a Kafka consumer."""
    return KafkaConsumer(
        'sink',
        bootstrap_servers=endpoint,
        sasl_mechanism='SCRAM-SHA-256',
        security_protocol='SASL_SSL',
        sasl_plain_username=username,
        sasl_plain_password=password,
        group_id='your_consumer_group',  # Specify the consumer group if needed
        auto_offset_reset='earliest',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize JSON messages
    )

def save_to_file(data: dict, file_path: str):
    """Append data to a local file."""
    with open(file_path, 'a') as f:
        f.write(json.dumps(data) + '\n')

def main():
    consumer = create_kafka_consumer()
    logger.info("Kafka Consumer started!")

    try:
        for message in consumer:
            original_data = message.value
            transformed_data = transform_data(original_data)
            
            logger.info(f"Received message: {original_data}")
            logger.info(f"Transformed message: {transformed_data}")
            
            save_to_file({'original': original_data, 'transformed': transformed_data}, 'messages.log')
    except KeyboardInterrupt:
        logger.info("Consumer stopped by user.")
    except Exception as e:
        logger.error(f"Error in consumer: {e}")
    finally:
        consumer.close()
        logger.info("Consumer closed.")

if __name__ == "__main__":
    main()
