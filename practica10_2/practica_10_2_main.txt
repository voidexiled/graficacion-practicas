import matplotlib.pyplot as plt

# Puntos
punto_original = (3, 5)
punto_trasladado = (7, 7)
# Crear la grafica
plt.figure(figsize=(6, 6))
plt.scatter(*punto_original, color="blue", label="punto original(3,5)")

plt.scatter(*punto_trasladado, color="red", label="punto trasladado(7,7)")
# Dibujar linea de desplazamiento
plt.plot(
    [punto_original[0], punto_trasladado[0]],
    [punto_original[1], punto_trasladado[1]],
    linestyle="dashed",
    color="gray",
)
# Etiquetas y tituo
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("traslacioon de un pnto en el plano")
plt.legend()
plt.grid(True)

# Mostrar la grafica
plt.show()
