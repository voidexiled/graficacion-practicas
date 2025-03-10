import math


def rotacion(punto, angulo):
    x, y = punto
    rad = math.radians(angulo)  # Convertir grados a radianes
    x_nuevo = x * math.cos(rad) - y * math.sin(rad)
    y_nuevo = x * math.sin(rad) + y * math.cos(rad)
    return (round(x_nuevo, 2), round(y_nuevo, 2))


# Punto original
punto = (3, 5)

# Rotar 45 grados
nuevo_punto = rotacion(punto, 45)
print(f"Punto original: {punto}")
print(f"Punto rotado: {nuevo_punto}")
