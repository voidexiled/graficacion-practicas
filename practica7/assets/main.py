import numpy as np
import matplotlib.pyplot as plt
import math


# Función para generar los vértices de un hexágono regular
def generate_hexagon(center_x, center_y, radius):
    hexagon = []
    for i in range(6):  # 6 lados
        angle = 2 * math.pi * i / 6  # Ángulos en radianes
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        hexagon.append((x, y))
    return hexagon


# Definir parámetros del hexágono
center_x, center_y = 10, 10  # Centro del hexágono
radius = 6  # Radio

# Generar el hexágono
hexagon = generate_hexagon(center_x, center_y, radius)

# Extraer coordenadas x e y
x_coords, y_coords = zip(*hexagon)
x_coords = list(x_coords) + [x_coords[0]]  # Cerrar el hexágono
y_coords = list(y_coords) + [y_coords[0]]

# Dibujar el hexágono con relleno rojo y bordes azules
plt.fill(x_coords, y_coords, "red", alpha=0.5)  # Relleno rojo con transparencia
plt.plot(x_coords, y_coords, "bo-", markersize=8, linewidth=2)  # Bordes en azul

# Configuración de la visualización
plt.grid(True)
plt.xticks(range(0, 21))
plt.yticks(range(0, 21))
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.gca().set_aspect("equal")
plt.title("Hexágono Regular con Relleno")

# Mostrar el gráfico
plt.show()
