import random

WIND_DIRS = ["N", "NO", "O", "SO", "S", "SE", "E", "NE"]

def generar_medicion():
    temp = random.gauss(25, 10)
    temp = max(0, min(110, temp))
    temp = round(temp, 2)

    hum = random.gauss(50, 20)
    hum = int(max(0, min(100, hum)))

    wind = random.choice(WIND_DIRS)

    return {
        "temperatura": temp,
        "humedad": hum,
        "direccion_viento": wind
    }

if __name__ == "__main__":
    for _ in range(10): 
        print(generar_medicion())
