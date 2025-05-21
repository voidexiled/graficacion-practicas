import numpy as np
from PIL import Image, ImageDraw  # ImageDraw será utilizado ahora
import math
import matplotlib.pyplot as plt


def triangle_gouraud_fill(img_array, verts, colors):
    """
    Rellena un triángulo definido por 'verts' (lista de 3 tuplas (x, y))
    usando los colores en 'colors' (lista de 3 tuplas (R, G, B)) con interpolación
    Gouraud (basada en coordenadas baricéntricas).

    Parámetros:
    - img_array: arreglo NumPy de la imagen (modificable in situ).
    - verts: lista de 3 vértices del triángulo.
    - colors: lista de 3 colores correspondientes a cada vértice.
    """
    # Extraer coordenadas x e y de los vértices
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]
    # Calcular la caja envolvente del triángulo
    min_x = max(min(xs), 0)
    max_x = min(max(xs), img_array.shape[1] - 1)
    min_y = max(min(ys), 0)
    max_y = min(max(ys), img_array.shape[0] - 1)

    # Extraer vértices
    x0, y0 = verts[0]
    x1, y1 = verts[1]
    x2, y2 = verts[2]

    # Precalcular el denominador para las coordenadas baricéntricas
    denom = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
    if denom == 0:
        return  # El triángulo es degenerado

    # Recorrer cada píxel dentro de la caja envolvente
    for y in range(int(min_y), int(max_y) + 1):
        for x in range(int(min_x), int(max_x) + 1):
            # Calcular coordenadas baricéntricas
            w0 = ((y1 - y2) * (x - x2) + (x2 - x1) * (y - y2)) / denom
            w1 = ((y2 - y0) * (x - x2) + (x0 - x2) * (y - y2)) / denom
            w2 = 1 - w0 - w1

            # Si el píxel se encuentra dentro del triángulo
            if w0 >= 0 and w1 >= 0 and w2 >= 0:
                # Interpolar el color según las coordenadas baricéntricas
                r = int(w0 * colors[0][0] + w1 * colors[1][0] + w2 * colors[2][0])
                g = int(w0 * colors[0][1] + w1 * colors[1][1] + w2 * colors[2][1])
                b = int(w0 * colors[0][2] + w1 * colors[1][2] + w2 * colors[2][2])
                img_array[y, x] = (r, g, b)


# Dimensiones de la imagen
width, height = 400, 400

# Crear una imagen en blanco y obtener su arreglo NumPy
img = Image.new("RGB", (width, height), "white")
img_array = np.array(img)

# Parámetros del octágono (8 lados)
num_sides = 8
radius = 150
center = (width // 2, height // 2)
octagon = []

# Generar los vértices del octágono distribuidos uniformemente
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    octagon.append((int(x), int(y)))

# Definir un color para cada vértice (por ejemplo, usando una gama de colores)
vertex_colors = [
    (255, 0, 0),  # Rojo
    (255, 127, 0),  # Naranja
    (255, 255, 0),  # Amarillo
    (0, 255, 0),  # Verde
    (0, 0, 255),  # Azul
    (75, 0, 130),  # Índigo
    (148, 0, 211),  # Violeta
    (255, 192, 203),  # Rosa
]

# Calcular el centroide del octágono (usado para triangulación en forma de abanico)
# En un polígono regular, el centroide coincide con el baricentro
cx = sum(x for x, y in octagon) / len(octagon)
cy = sum(y for x, y in octagon) / len(octagon)
centroid = (int(cx), int(cy))  # Este es el baricentro

# Calcular el color del centroide como el promedio de los colores de los vértices
centroid_color = tuple(
    sum(color[i] for color in vertex_colors) // len(vertex_colors) for i in range(3)
)

# Triangular el octágono usando el centroide y rellenar cada triángulo con sombreado Gouraud
for i in range(num_sides):
    v1 = octagon[i]
    v2 = octagon[(i + 1) % num_sides]
    c1 = vertex_colors[i]
    c2 = vertex_colors[(i + 1) % num_sides]

    # Definir el triángulo: dos vértices del octágono y el centroide
    triangle = [v1, v2, centroid]
    triangle_colors = [c1, c2, centroid_color]
    triangle_gouraud_fill(img_array, triangle, triangle_colors)

# Convertir el arreglo NumPy modificado de vuelta a una imagen PIL
img_out = Image.fromarray(img_array)

# --- NUEVO: Dibujar las medianas y resaltar el baricentro ---
# Crear un objeto Draw para dibujar sobre la imagen resultante del sombreado
draw = ImageDraw.Draw(img_out)

# Definir color para las medianas y el baricentro
median_color = (0, 0, 0)  # Negro para las medianas
barycenter_color = (255, 255, 255)  # Blanco para el baricentro
barycenter_marker_radius = 4  # Radio del círculo para marcar el baricentro

# Dibujar las 8 medianas (líneas desde cada vértice al baricentro)
for vertex in octagon:
    draw.line([vertex, centroid], fill=median_color, width=1)

# Resaltar el baricentro (dibujar un pequeño círculo)
bx, by = centroid
draw.ellipse(
    [
        (bx - barycenter_marker_radius, by - barycenter_marker_radius),
        (bx + barycenter_marker_radius, by + barycenter_marker_radius),
    ],
    fill=barycenter_color,
    outline=median_color,  # Contorno negro para mejor visibilidad
)

# Definir el texto con las coordenadas (x, y)
centroid_text = f"({centroid[0]}, {centroid[1]})"
# Dibujar el texto cerca del varicentro; ajusta la posición según necesites
draw.text(
    (bx + barycenter_marker_radius + 5, by - barycenter_marker_radius - 5),
    centroid_text,
    fill=(0, 0, 0),
)

# --- FIN NUEVO ---

# Visualizar el resultado con Matplotlib
plt.figure(figsize=(6, 6))
plt.imshow(img_out)
plt.axis("off")
plt.title("Octágono con Sombreado Gouraud, Medianas y Baricentro")  # Título actualizado
plt.show()
