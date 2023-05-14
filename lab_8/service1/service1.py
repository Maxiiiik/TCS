import json
import os
from time import sleep

import psycopg2
from kafka import KafkaProducer


POSTGIS_HOST = os.environ.get("POSTGRES_HOST")
POSTGIS_PORT = os.environ.get("POSTGRES_PORT")
POSTGIS_USER = os.environ.get("POSTGRES_USER")
POSTGIS_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGIS_DB = os.environ.get("POSTGRES_DB")
KAFKA_HOST = os.environ.get("KAFKA_HOST")

producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)
filename = 'data/field_centroids.geojson'


def connect_to_db():
    conn = psycopg2.connect(
        host=POSTGIS_HOST,
        port=POSTGIS_PORT,
        dbname=POSTGIS_DB,
        user=POSTGIS_USER,
        password=POSTGIS_PASSWORD
    )
    return conn

def insert_field_to_db(field):
    conn = connect_to_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO features (id, name, geometry) VALUES (%s, %s, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326))", (field['id'], field['name'], json.dumps(field['geom'])))
        conn.commit()
        print(f"Field with ID {field['id']} inserted into the database.")
    except Exception as e:
        print(f"Error inserting field into the database: {str(e)}")
    finally:
        cur.close()
        conn.close()

def read_fields_from_file():
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        for feature in data['features']:
            field = {
                'id': feature['properties']['id'],
                'name': feature['properties']['Name'],
                'geom': feature['geometry']}
            insert_field_to_db(field)
        os.remove(filename)
        producer.send('field-reading', "Data received".encode("UTF-8"))
        print(f"Field data sent to Kafka.\n")
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        

# Check and run read_fiealds_from_file() if file exists
def check_new_file():
    while True:
        if os.path.exists(filename):
            read_fields_from_file()
            print("Data saved into db.")
            print("................\n")
        sleep(5)


if __name__ == "__main__":
    print("Service started!")
    print("................")
    try:
        check_new_file()
    except KeyboardInterrupt:
        print("Service stopped")
