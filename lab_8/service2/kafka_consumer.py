from kafka import KafkaConsumer

# Налаштування Kafka-споживача
consumer = KafkaConsumer(
    'field-processing',
    bootstrap_servers='localhost:9092',
    group_id='field-processing-group'
)

# Читання повідомлень з каналу field-processing
for message in consumer:
    # Отримання повідомлення
    payload = message.value.decode('utf-8')
    
    # Обробка повідомлення
    process_message(payload)
    
    # Підтвердження успішного оброблення повідомлення
    consumer.commit()
    
def process_message(payload):
    # Розбір та обробка повідомлення
    # Тут виконується обробка даних про поля та вологості грунту
    
    # Збереження результату
    save_result_to_file(payload)
    
def save_result_to_file(payload):
    # Збереження результату у файл json
    # Тут виконується збереження оброблених даних у вказаній структурі у файл json
    pass
