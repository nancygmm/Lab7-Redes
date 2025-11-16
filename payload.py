from sensor import WIND_DIRS

def encode_medicion(msg):
    temp = msg["temperatura"]
    hum = msg["humedad"]
    wind = msg["direccion_viento"]

    temp_int = int(round(temp * 100))  
    hum_int = int(hum)                 

    wind_int = WIND_DIRS.index(wind)

    temp_int = max(0, min(11000, temp_int))
    hum_int = max(0, min(100, hum_int))
    wind_int = max(0, min(7, wind_int))

    payload = ((temp_int & 0x3FFF) << 10) | ((hum_int & 0x7F) << 3) | (wind_int & 0x07)

    b0 = (payload >> 16) & 0xFF
    b1 = (payload >> 8) & 0xFF
    b2 = payload & 0xFF

    return bytes([b0, b1, b2])

def decode_medicion(b):
    if len(b) != 3:
        raise ValueError("Se esperaban exactamente 3 bytes")

    payload = (b[0] << 16) | (b[1] << 8) | b[2]

    temp_int = (payload >> 10) & 0x3FFF  
    hum_int  = (payload >> 3) & 0x7F    
    wind_int = payload & 0x07          

    temp = temp_int / 100.0
    hum = hum_int
    wind = WIND_DIRS[wind_int]

    return {
        "temperatura": temp,
        "humedad": hum,
        "direccion_viento": wind
    }

if __name__ == "__main__":
    from sensor import generar_medicion

    original = generar_medicion()
    print("Original:", original)

    encoded = encode_medicion(original)
    print("Bytes:", encoded)

    decoded = decode_medicion(encoded)
    print("Decodificado:", decoded)
