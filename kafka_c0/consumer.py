import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime

TOPIC = "iot_sensor_data"

KAFKA_BOOTSTRAP = "localhost:9092"

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "iot_db"
COLLECTION = "sensor_data"

mongo_client = MongoClient(MONGO_URI)
col = mongo_client[DB_NAME][COLLECTION]

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_BOOTSTRAP],
    auto_offset_reset="latest",     
    enable_auto_commit=True,
    group_id="iot-mongo-consumer",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)





# print("Kafka → MongoDB consumer started. Waiting for messages...")

try:
    for message in consumer:
        data = message.value
        print(message)
       
        data["ingested_at"] = datetime.utcnow().isoformat()

        result = col.insert_one(data)
        print(f"Inserted {result.inserted_id} | Offset {message.offset} | Data: {data}")

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    consumer.close()
    mongo_client.close()
