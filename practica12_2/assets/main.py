import matplotlib.pyplot as plt
import math


# Funcion Rotacion
def rotacion(punto, angulo):
    x, y = punto
    rad = math.radians(angulo)  # Convertir grados a raidanes
    x_nuevo = x * math.cos(rad) - y * math.sin(rad)
    y_nuevo = x * math.sin(rad) + y * math.cos(rad)
    return round(x_nuevo, 2), round(y_nuevo, 2)


# Punto original
punto = (3, 5)

# Rotar 45 grados
nuevo_punto = rotacion(punto, 45)

# Graficar los puntos
plt.figure(figsize=(6, 6))
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", linewidth=0.5)

# Dibujar puntos
plt.scatter(*punto, color="blue", label="Punto original (3,5)")
plt.scatter(*nuevo_punto, color="red", label=f"Punto rotado {nuevo_punto}")

# Dibujar lineas de referencia
plt.plot([0, punto[0]], [0, punto[1]], "b--", alpha=0.5)
plt.plot([0, nuevo_punto[0]], [0, nuevo_punto[1]], "r--", alpha=0.5)

# Etiquetas
plt.legend()
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Rotacion de un punto en 45 grados")

# Mostrar gráfrica
plt.show()
