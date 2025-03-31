from confluent_kafka import Consumer

# Kafka Consumer Configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker
    'group.id': 'market-data-group',        # Consumer group
    'auto.offset.reset': 'earliest'         # Start from the beginning if no previous offset
}

# Create Kafka Consumer
consumer = Consumer(conf)
consumer.subscribe(['market-data'])  # Subscribe to the topic

print("Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"Received: {msg.value().decode('utf-8')}")  # Decode and print message

except KeyboardInterrupt:
    print("Closing consumer...")

finally:
    consumer.close()
