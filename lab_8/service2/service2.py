import os

import psycopg2
from kafka import KafkaConsumer, KafkaProducer


POSTGIS_HOST = os.environ.get("POSTGRES_HOST")
POSTGIS_PORT = os.environ.get("POSTGRES_PORT")
POSTGIS_USER = os.environ.get("POSTGRES_USER")
POSTGIS_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGIS_DB = os.environ.get("POSTGRES_DB")
KAFKA_HOST = os.environ.get("KAFKA_HOST")


consumer = KafkaConsumer(
    'field-reading',
    bootstrap_servers=KAFKA_HOST,
    group_id='field-reading-group',
    auto_offset_reset='earliest'
)
producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)


def connect_to_db():
    conn = psycopg2.connect(
        host=POSTGIS_HOST,
        port=POSTGIS_PORT,
        dbname=POSTGIS_DB,
        user=POSTGIS_USER,
        password=POSTGIS_PASSWORD
    )
    return conn


def read_message():
    for message in consumer:
        payload = message.value.decode('utf-8')
        process_message(payload)
        consumer.commit()

def process_message(message):
    if message == "Data received":
        print("Message received")
        with open('data/POI.txt', 'r') as f:
            points = []
            for i in f:
                points = i.strip().split(",")
                nearest_point = get_nearest_point(points)
                print("Nearest point found: ", i.strip().split(","))
                send_to_field_processing(nearest_point[3], nearest_point[2], nearest_point[1], points)


def get_nearest_point(points):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
    Select id, name, ST_X(geometry), ST_Y(geometry), ST_Distance(geometry, 'SRID=4326;Point(%s %s)'::geometry)   
    from features
    order by ST_Distance(geometry, 'SRID=4326;Point(%s %s)'::geometry)
    limit 1;""", (float(points[0]), float(points[1]), float(points[0]), float(points[1])))
    
    nearest_point = cursor.fetchone()
    cursor.close()
    conn.close()
    return nearest_point

def send_to_field_processing(nearest_point_X, nearest_point_Y, name, poi):
    data =  {
        'point_of_interest':{
            'lat': float(poi[0]),
            'lon': float(poi[1])
        },
        'field_data': {
            "name": name, 
            'lat': nearest_point_Y,
            'lon': nearest_point_X
        }
    }
    producer.send('field-processing', str(data).encode("UTF-8"))
    print("Message sent:", str(data))
    print(".............\n")


if __name__ == "__main__":
    print("Service started!")
    print("................")
    try:
        read_message()
    except KeyboardInterrupt:
        print("...............")
        print("Service stopped")
