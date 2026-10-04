from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test',
    bootstrap_servers='localhost:19092',
    security_protocol="PLAINTEXT", # доступ без паролей
    auto_offset_reset='earliest', # будет просматривать сообщения, которые были опубликованы до запуска сервиса
    group_id='test_consumer_group', # просмотренные сообщения не будут считываться повторно
)

print("ready")

for msg in consumer:
    print(msg.key.decode("utf-8") + ":" + msg.value.decode("utf-8"))