from kafka import KafkaConsumer
from payload import decode_medicion
import matplotlib.pyplot as plt
from datetime import datetime

BROKER = "iot.redesuvg.cloud:9092"
TOPIC = "22513" 
GROUP_ID = "grupo-lab7-compacto"

def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=[BROKER],
        auto_offset_reset="latest",
        group_id=GROUP_ID
    )

    print(f"[{datetime.now()}] Consumer COMPACTO escuchando en topic '{TOPIC}'...")
    print("Abre también producer_compacto.py para empezar a recibir datos.\n")

    temps = []
    humes = []
    idx = []

    plt.ion()
    fig, ax = plt.subplots()

    for i, msg in enumerate(consumer, start=1):
        data = decode_medicion(msg.value)

        temp = data["temperatura"]
        hum = data["humedad"]
        wind = data["direccion_viento"]

        temps.append(temp)
        humes.append(hum)
        idx.append(i)

        print(f"[{datetime.now()}] Recibido #{i}: bytes={msg.value}  -> {data}")

        ax.clear()
        ax.plot(idx, temps, label="Temperatura (°C)")
        ax.plot(idx, humes, label="Humedad (%)")
        ax.set_xlabel("Muestra")
        ax.set_ylabel("Valor")
        ax.set_title("Telemetría Estación (Payload compacto 3 bytes)")
        ax.legend()
        ax.grid(True)

        plt.tight_layout()
        plt.pause(0.01)

if __name__ == "__main__":
    main()
