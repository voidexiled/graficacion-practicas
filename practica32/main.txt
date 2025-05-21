import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import math


def flood_fill(image, x, y, new_color):
    """
    Realiza flood fill en 'image' a partir del píxel (x, y).
    image: numpy array de la imagen en formato RGB.
    new_color: np.array con el nuevo color [R, G, B].
    """
    height, width, _ = image.shape
    old_color = image[y, x].copy()
    if np.array_equal(old_color, new_color):
        return
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if (
            0 <= cx < width
            and 0 <= cy < height
            and np.array_equal(image[cy, cx], old_color)
        ):
            image[cy, cx] = new_color
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))


# Dimensiones de la imagen
width, height = 300, 300

# Crear una imagen en blanco (fondo blanco)
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Parámetros del hexágono regular
center = (150, 150)
radius = 100
num_lados = 6

# Calcular las coordenadas de los vértices del hexágono
polygon_points = []
for i in range(num_lados):
    angle = 2 * math.pi * i / num_lados
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    polygon_points.append((x, y))

# Dibujar el contorno del hexágono (en negro)
draw.line(polygon_points + [polygon_points[0]], fill="black", width=2)

# Convertir la imagen a un array numpy para manipulación
img_array = np.array(img)

# Seleccionar un punto semilla dentro del hexágono
seed_x, seed_y = center  # Se utiliza el centro del hexágono

# Definir el color de relleno (rojo)
new_color = np.array([255, 255, 0], dtype=np.uint8)

# Aplicar flood fill al área interna del hexágono
flood_fill(img_array, seed_x, seed_y, new_color)

# Visualizar el resultado
plt.figure(figsize=(6, 6))
plt.imshow(img_array)
plt.title("Relleno de Hexágono Regular con Flood Fill")
plt.axis("off")
plt.show()
