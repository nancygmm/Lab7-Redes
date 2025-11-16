from kafka import KafkaProducer
from sensor import generar_medicion
import json
import time
import random
from datetime import datetime

BROKER = "iot.redesuvg.cloud:9092"
TOPIC = "22513"   

def main():
    producer = KafkaProducer(
        bootstrap_servers=[BROKER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    print(f"[{datetime.now()}] Producer JSON iniciado. Enviando a topic '{TOPIC}'...")
    print("Presiona Ctrl+C para detener.\n")

    try:
        while True:
            data = generar_medicion()
            producer.send(TOPIC, data)

            print(f"[{datetime.now()}] Enviado a {TOPIC}: {data}")

            time.sleep(random.randint(15, 30))

    except KeyboardInterrupt:
        print("\nProducer detenido por el usuario.")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()
