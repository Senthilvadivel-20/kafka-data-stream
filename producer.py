from confluent_kafka import Producer
import time
import random

# Kafka Producer Configuration
conf = {"bootstrap.servers": "localhost:9092"}
producer = Producer(conf)

# Stock symbols
stocks = ["AAPL", "GOOGL", "AMZN", "TSLA"]

def generate_market_data():
    stock = random.choice(stocks)
    price = round(random.uniform(100, 2000), 2)
    timestamp = int(time.time())
    return f"{stock},{price},{timestamp}"

# Send messages
while True:
    message = generate_market_data()
    producer.produce("market-data", key="stock", value=message)
    print(f"Sent: {message}")
    producer.flush()
    time.sleep(1)  # Simulate real-time data feed
