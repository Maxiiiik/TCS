import os
import json
from kafka import KafkaConsumer, KafkaProducer
from psycopg2 import connect
from shapely.geometry import Point
from shapely.ops import nearest_points


def connect_to_db():
    connection_string = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
                        f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    conn = connect(connection_string)
    return conn


def get_nearest_field(point, fields):
    nearest_field = None
    min_distance = float('inf')

    for field in fields:
        field_point = field['geom']
        distance = point.distance(field_point)

        if distance < min_distance:
            min_distance = distance
            nearest_field = field

    return nearest_field


def process_fields(consumer, producer):
    for message in consumer:
        message_data = json.loads(message.value)
        poi_coordinates = message_data['coordinates']

        poi_point = Point(poi_coordinates['lon'], poi_coordinates['lat'])

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM fields")
        fields = cursor.fetchall()

        nearest_field = get_nearest_field(poi_point, fields)

        if nearest_field is not None:
            payload = {
                "point_of_interest": {
                    "lat": poi_coordinates['lat'],
                    "lon": poi_coordinates['lon']
                },
                "field_data": {
                    "name": nearest_field[1],
                    "lat": nearest_field[2].y,
                    "lon": nearest_field[2].x
                }
            }

            producer.send('field-processing', json.dumps(payload).encode('utf-8'))

        conn.close()


if __name__ == '__main__':
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
    consumer_topic = 'field-reading'
    producer_topic = 'field-processing'

    consumer = KafkaConsumer(consumer_topic, bootstrap_servers=bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    process_fields(consumer, producer)
