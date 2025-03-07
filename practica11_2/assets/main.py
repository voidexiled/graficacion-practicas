import matplotlib.pyplot as plt


# Definir la funcion de escalamiento
def escalamiento(punto, sx, sy):
    x, y = punto
    return (x * sx, y * sy)


# Punto original
punto = (3, 5)

# Escalar por 3 un X y 0.5 en Y
nuevo_punto = escalamiento(punto, 2, 0.5)

plt.figure(figsize=(6, 6))
plt.axhline(0, color="black", linewidth=0.5)  # Eje X
plt.axvline(0, color="black", linewidth=0.5)  # Eje Y

# Puntos y etiquetas
plt.scatter(*punto, color="blue", label="Punto Original (3,5)", s=100)
plt.scatter(*nuevo_punto, color="red", label=f"Punto Escalado{nuevo_punto}", s=100)

# Lineas de conexion
plt.plot(
    [punto[0], nuevo_punto[0]],
    [punto[0], nuevo_punto[1]],
    linestyle="dashed",
    color="gray",
)

# Etiquetas y titulo
plt.xlabel("x")
plt.ylabel("y")
plt.title("transformacion de Escalamiento")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Mostrar grafica
plt.show()
