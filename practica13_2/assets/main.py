import matplotlib.pylab as plt


# Funcion sesgado
def sesgado(punto, sx, sy):
    x, y = punto
    x_nuevo = x + sx * y
    y_nuevo = y + sy * x
    return (x_nuevo, y_nuevo)


# Punto originsl
punto = (3, 5)

# Aplica sesgado en x = 1.2 y en Y = 0.5
nuevo_punto = sesgado(punto, 1.2, 0.5)

# Graficar los puntos antes y despeus del sesgado
plt.figure(figsize=(6, 6))
plt.scatter(*punto, color="blue", label="Punto original", s=100)
plt.scatter(*nuevo_punto, color="red", label="Punto sesgado", s=100)

# Dibujar flecha entre los puntos
plt.arrow(
    punto[0],
    punto[1],
    nuevo_punto[0] - punto[0],
    nuevo_punto[1] - punto[1],
    head_width=0.3,
    head_length=0.3,
    fc="gray",
    ec="gray",
    linestyle="dashed",
)

# Configuración de la grafica
plt.xlim(0, max(punto[0], nuevo_punto[0]) + 2)
plt.ylim(0, max(punto[1], nuevo_punto[1]) + 2)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.xlabel("Eje x")
plt.ylabel("Eje Y")
plt.title("Transformacion de sesgado (shearing)")

# Mostrar grafica
plt.show()
