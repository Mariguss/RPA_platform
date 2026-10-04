from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:19092',
    security_protocol="PLAINTEXT",
)

producer.send('test', b'test message', b'key')
producer.flush()
producer.close()