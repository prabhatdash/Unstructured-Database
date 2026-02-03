import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'iot_sensor_data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # Read from the start if no offset is saved
    enable_auto_commit=True,       # Automatically mark messages as 'read'
    group_id='my-sensor-group',    # Consumer group ID
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started. Waiting for messages...")

try:
    for message in consumer:
        data = message.value
        print(f"Consumed: {data} | Partition: {message.partition} | Offset: {message.offset}")
except KeyboardInterrupt:
    print("Consumer shutting down...")
finally:
    consumer.close()