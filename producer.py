from kafka import KafkaProducer
from faker import Faker
from random import randrange
import json
import time
import logging
from config import endpoint, username, password

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_kafka_producer() -> KafkaProducer:
    """Create and return a Kafka producer."""
    return KafkaProducer(
        bootstrap_servers=endpoint,
        sasl_mechanism='SCRAM-SHA-256',
        security_protocol='SASL_SSL',
        sasl_plain_username=username,
        sasl_plain_password=password,
        api_version_auto_timeout_ms=100000,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON before sending
    )

def generate_fake_data(fake: Faker) -> dict:
    """Generate and return fake data."""
    return {
        'name': fake.name(),
        'address': fake.address(),
        'age': randrange(10, 100)
    }

def main():
    producer = create_kafka_producer()
    logger.info("Kafka Producer started!")
    
    fake = Faker()
    
    try:
        while True:
            data_dict = generate_fake_data(fake)
            
            try:
                result = producer.send('sink', value=data_dict).get(timeout=60)
                logger.info(f"Message produced: {data_dict}")
            except Exception as e:
                logger.error(f"Error producing message: {e}")
            
            time.sleep(randrange(5, 8))
    except KeyboardInterrupt:
        logger.info("Producer stopped by user.")
    finally:
        producer.close()
        logger.info("Producer closed.")

if __name__ == "__main__":
    main()
