from kafka import KafkaProducer
from sensor import generar_medicion
from payload import encode_medicion
from datetime import datetime
import time
import random

BROKER = "iot.redesuvg.cloud:9092"
TOPIC = "22513"  

def main():
    producer = KafkaProducer(
        bootstrap_servers=[BROKER]
    )

    print(f"[{datetime.now()}] Producer COMPACTO iniciado. Enviando a topic '{TOPIC}'...")
    print("Presiona Ctrl+C para detener.\n")

    try:
        while True:
            medicion = generar_medicion()
            payload = encode_medicion(medicion)

            producer.send(TOPIC, payload)
            print(f"[{datetime.now()}] Enviado a {TOPIC}: {medicion}  -> bytes {payload}")

            time.sleep(random.randint(15, 30))

    except KeyboardInterrupt:
        print("\nProducer compacto detenido por el usuario.")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()
