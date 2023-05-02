import json
from kafka import KafkaConsumer
from rasterio.io import MemoryFile

def read_soil_moisture(file_path):
    # Читання файла з вологістю грунту
    with MemoryFile(file_path) as memfile:
        with memfile.open() as dataset:
            # Виконуємо потрібні дії з даними, наприклад, отримання значення вологості для певної координати
            # В цьому прикладі просто використовуємо заглушку
            moisture = 0.75
            return moisture

def process_field_data():
    consumer = KafkaConsumer(
        'field-processing',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        field_data = message.value
        poi = field_data['point_of_interest']
        field = field_data['field_data']

        # Отримання вологості грунту для поля
        moisture = read_soil_moisture('soil_moisture.tif')

        # Підготовка даних для збереження у файл json
        data = {
            'point_of_interest': poi,
            'field_data': field,
            'moisture': moisture
        }

        # Збереження даних у файл json
        with open('output.json', 'w') as file:
            json.dump(data, file)

        # Виведення повідомлення про обробку поля
        print(f'Processed field: {field["name"]}')

if __name__ == '__main__':
    process_field_data()
