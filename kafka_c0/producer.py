import time
import json
import random
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'iot_sensor_data'

print(f"Producer started. Sending data to topic: {topic}")

try:
    while True:
        payload = {
            'timestamp': time.time(),
            'sensor_id': 'DHT11_01',
            'temperature': round(random.uniform(20.0, 30.0), 2),
            'status': 'OK'
        }
        
        producer.send(topic, value=payload)
        print(f"Sent to Kafka: {payload}")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Producer shutting down...")
finally:
    producer.close()