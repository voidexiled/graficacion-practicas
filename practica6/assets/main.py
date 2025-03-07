import matplotlib.pyplot as plt
import numpy as np

# Definir los colores según la imagen
colors = {
    "ORANGE": [255, 200, 0],
    "PINK": [255, 175, 175],
    "CYAN": [0, 255, 255],
    "MAGENTA": [255, 0, 255],
    "YELLOW": [255, 255, 0],
    "BLACK": [0, 0, 0],
    "WHITE": [255, 255, 255],
    "GRAY": [128, 128, 128],
    "LIGHT_GRAY": [192, 192, 192],
    "DARK_GRAY": [64, 64, 64],
    "RED": [255, 0, 0],
    "GREEN": [0, 255, 0],
    "BLUE": [0, 0, 255],
}

# Crear un gráfico de barras para mostrar los colores
fig, ax = plt.subplots(figsize=(10, 6))
bars = list(colors.keys())
values = list(colors.values())

# Convertir los valores RGB a escala 0-1 para matplotlib
normalized_colors = [(r / 255, g / 255, b / 255) for r, g, b in values]

# Crear las barras
for i, color in enumerate(normalized_colors):
    ax.barh(i, 1, color=color, edgecolor="black")

# Configurar el eje
ax.set_yticks(range(len(bars)))
ax.set_yticklabels(bars)
ax.set_xticks([])

# Crear las barras
for i, color in enumerate(normalized_colors):
    ax.barh(i, 1, color=color, edgecolor="black")

# Configurar el eje
ax.set_yticks(range(len(bars)))
ax.set_yticklabels(bars)
ax.set_xticks([])
ax.set_title("Colores definidos por sus valores RGB")

plt.show()
