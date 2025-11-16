from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
from datetime import datetime

BROKER = "iot.redesuvg.cloud:9092"
TOPIC = "22513"   

def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=[BROKER],
        auto_offset_reset="latest",  
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        group_id="grupo-lab7-json"
    )

    print(f"[{datetime.now()}] Consumer JSON escuchando en topic '{TOPIC}'...")
    print("Abre también producer_json.py para empezar a recibir datos.\n")

    temps = []
    humes = []
    idx = []

    plt.ion()
    fig, ax = plt.subplots()

    for i, msg in enumerate(consumer, start=1):
        data = msg.value
        temp = data["temperatura"]
        hum = data["humedad"]
        wind = data["direccion_viento"]

        temps.append(temp)
        humes.append(hum)
        idx.append(i)

        print(f"[{datetime.now()}] Recibido #{i}: {data}")

        ax.clear()
        ax.plot(idx, temps, label="Temperatura (°C)")
        ax.plot(idx, humes, label="Humedad (%)")
        ax.set_xlabel("Muestra")
        ax.set_ylabel("Valor")
        ax.set_title("Telemetría Estación (JSON)")
        ax.legend()
        ax.grid(True)

        plt.tight_layout()
        plt.pause(0.01)

if __name__ == "__main__":
    main()
