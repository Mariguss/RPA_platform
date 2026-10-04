from kafka import KafkaConsumer

BASE_URL = "http://localhost:8888"

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


# def load_test_data():
#     json_path = Path(__file__).parent / "test_data_customer.json"
#     json_text= json_path.read_text(encoding="utf-8")
#     data_dict = json.loads(json_text)["test_customer"]
#     return Customer.model_validate(data_dict)
#
#
# test_data = load_test_data()
#
#
# LoginPage(driver, BASE_URL).login("admin", "admin")
#
# register_customer(driver, BASE_URL, schema=test_data)
