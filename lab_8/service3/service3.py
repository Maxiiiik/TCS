# import os
# import json
# import rasterio
# import ast
# from kafka import KafkaConsumer


# KAFKA_HOST = os.environ.get("KAFKA_HOST")


# consumer = KafkaConsumer(
#     'field-processing',
#     bootstrap_servers=KAFKA_HOST,
#     group_id='field-processing-group',
#     auto_offset_reset='earliest'
# )

# def read_message():
#     for message in consumer:
#         payload = message.value.decode('utf-8')
#         print(f"Message received: \n{payload}")
#         process_message(payload)
#         consumer.commit()

# def process_message(message):
#     data = ast.literal_eval(message)
#     result = process_field_data(data)
#     save_to_json(result, f"output/result_{data['point_of_interest']['lat']}_{data['point_of_interest']['lon']}.geojson")
#     print(f"File generated: output/result_{data['point_of_interest']['lat']}_{data['point_of_interest']['lon']}.geojson")
#     print("Message processed!")
#     print("..................")

# def process_field_data(field_data):
#     moisture = get_soil_moisture(field_data['field_data']['lat'], field_data['field_data']['lon'])
#     json_data = json.dumps({
#         'point_of_interest': {
#             'lat': field_data['point_of_interest']['lat'],
#             'lon': field_data['point_of_interest']['lon']
#         },
#         'field_data': field_data['field_data'],
#         'moisture': int(moisture)
#     }, indent=4)
#     return json_data

# def get_soil_moisture(lat, lon):
#     file_path = 'soil_moisture.tif'
    
#     with rasterio.open(file_path) as dataset:
#         col, row = dataset.index(lat, lon)
#         moisture = dataset.read(1, window=((row, row+1), (col, col+1)))
#     return moisture[0][0]

# def save_to_json(data, filename):
#     with open(filename, 'w') as file:
#         file.write(data)


# def main():
#     print("Service started!")
#     print("................")
#     read_message()
    

# if __name__ == '__main__':
#     main()





import os
import json
import rasterio
import ast
from kafka import KafkaConsumer


KAFKA_HOST = os.environ.get("KAFKA_HOST")


consumer = KafkaConsumer(
    'field-processing',
    bootstrap_servers=KAFKA_HOST,
    group_id='field-processing-group',
    auto_offset_reset='earliest'
)

def read_message():
    for message in consumer:
        payload = message.value.decode('utf-8')
        print(f"Message received: \n{payload}")
        process_message(payload)
        consumer.commit()

def process_message(message):
    data = json.loads(message.replace("'", '"'))
    result = process_field_data(data)
    filename = f"output/result_{data['point_of_interest']['lat']}_{data['point_of_interest']['lon']}.geojson"
    save_to_geojson(result, filename)
    print(f"File generated: {filename}")
    print("Message processed!")
    print("..................")

def process_field_data(field_data):
    moisture = field_data.get('moisture', 0)

    lat = field_data['point_of_interest']['lat']
    lon = field_data['point_of_interest']['lon']
    
    feature = {
        'type': 'Feature',
        'properties': {
            'moisture': moisture
        },
        'geometry': {
            'type': 'Point',
            'coordinates': [lat, lon]
        }
    }

    result = {
        'type': 'FeatureCollection',
        'name': 'field_data',
        'crs': {
            'type': 'name',
            'properties': {
                'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'
            }
        },
        'features': [feature]
    }
    return result

def save_to_geojson(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    print("Service started!")
    print("................")
    read_message()
    

if __name__ == '__main__':
    main()
