import json
from kafka import KafkaProducer
import geopandas as gpd
from shapely.geometry import mapping
import psycopg2

# З'єднання з Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092')

# З'єднання з базою даних PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='postgres',
        user='postgres',
        password='postgres'
    )
    return conn

# Запис даних про поля у базу даних та відправка повідомлення у Kafka
def insert_field_to_db(field):
    conn = connect_to_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO fields (id, geom) VALUES (%s, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326))", (field['id'], json.dumps(field['geom'])))
        conn.commit()
        print(f"Field with ID {field['id']} inserted into the database.")
        producer.send('field-reading', json.dumps(field).encode('utf-8'))
        print(f"Field data sent to Kafka.")
    except Exception as e:
        print(f"Error inserting field into the database: {str(e)}")
    finally:
        cur.close()
        conn.close()

# Зчитування даних з файлу field_centroids.geojson та запис у базу даних
def read_fields_from_file():
    try:
        data = gpd.read_file('field_centroids.geojson')
        for index, row in data.iterrows():
            field = {
                'id': row['id'],
                'geom': mapping(row['geometry'])
            }
            insert_field_to_db(field)
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    read_fields_from_file()
