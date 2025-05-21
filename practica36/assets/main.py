# 4.1.2D_Graficación_sombreado_Phong_2025 > ...
import numpy as np
from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plt

def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm if norm != 0 else v

def triangle_phong_fill_color(img_array, verts, normals, base_colors, light_dir, view_dir,
                             ambient=0.1, diffuse_coef=1.0, specular_coef=1.0, shininess=20):
    """
    Rellena un triángulo definido por `verts` (lista de 3 tuplas (x, y)) usando el modelo de iluminación Phong.
    Se interpolan los vectores normales (parámetro `normals`) y los colores base (parámetro `base_colors`) mediante
    coordenadas baricéntricas para cada píxel, y se calcula el color final (en RGB) combinando las componentes ambiente,
    difusa y especular.
    Parámetros:
      - img_array: arreglo NumPy de la imagen (se modifica in situ).
      - verts: lista de 3 vértices (x, y) del triángulo.
      - normals: lista de 3 vectores normales (cada uno de 3 componentes) asociados a cada vértice.
      - base_colors: lista de 3 colores base (tuplas RGB, valores 0-255) para cada vértice.
      - light_dir: vector dirección de la luz (normalizado).
      - view_dir: vector dirección de la cámara (normalizado).
      - ambient: componente ambiente.
      - diffuse_coef: coeficiente difuso.
      - specular_coef: coeficiente especular.
      - shininess: exponente de brillo para la componente especular.
    """
    # Extraer coordenadas de los vértices
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]

    # Calcular la caja envolvente del triángulo (limitada a los bordes de la imagen)
    min_x = max(int(min(xs)), 0)
    max_x = min(int(max(xs)), img_array.shape[1] - 1)
    min_y = max(int(min(ys)), 0)
    max_y = min(int(max(ys)), img_array.shape[0] - 1)

    # Extraer vértices individuales
    x0, y0 = verts[0]
    x1, y1 = verts[1]
    x2, y2 = verts[2]

    # Precalcular el denominador para coordenadas baricéntricas
    denom = ((y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2))
    if denom == 0:
        return # Triángulo degenerado

    # Recorrer cada píxel dentro de la caja envolvente
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            # Calcular coordenadas baricéntricas
            w0 = ((y1 - y2) * (x - x2) + (x2 - x1) * (y - y2)) / denom
            w1 = ((y2 - y0) * (x - x0) + (x0 - x2) * (y - y0)) / denom
            w2 = 1 - w0 - w1

            # Verificar si el píxel (x, y) se encuentra dentro del triángulo
            if w0 >= 0 and w1 >= 0 and w2 >= 0:
                # Interpolar el vector normal y normalizarlo
                n_interp = w0 * np.array(normals[0]) + w1 * np.array(normals[1]) + w2 * np.array(normals[2])
                n_interp = normalize(n_interp)

                # Interpolar el color base (convertido a [0,1])
                color_interp = (w0 * np.array(base_colors[0]) +
                                w1 * np.array(base_colors[1]) +
                                w2 * np.array(base_colors[2])) / 255.0

                # Modelo Phong: I = Ia + Id + Is
                Ia = ambient
                NdotL = max(np.dot(n_interp, light_dir), 0)
                Id = diffuse_coef * NdotL
                # Calcular el vector reflejado: R = 2*(N·L)*N - L
                R = 2 * NdotL * n_interp - light_dir
                R = normalize(R)
                RdotV = max(np.dot(R, view_dir), 0)
                Is = specular_coef * (RdotV ** shininess)

                # Calcular el color final por canal:
                # Se aplica la base de color a la componente ambiente + difusa y se suma la componente especular (usamos blanco para el especular).
                final_color = color_interp * (Ia + Id) + Is * np.array([1, 1, 1])
                final_color = np.clip(final_color, 0, 1) * 255
                img_array[y, x] = tuple(final_color.astype(np.uint8))

# Dimensiones de la imagen
width, height = 500, 500

# Crear una imagen en blanco y convertirla a arreglo NumPy
img = Image.new("RGB", (width, height), "white")
img_array = np.array(img)

# Parámetros del eneágono (9 lados)
num_sides = 9
radius = 200
center = (width // 2, height // 2)
polygon = []

# Generar los vértices del eneágono
for i in range(num_sides):
   angle = 2 * math.pi * i / num_sides
   x = center[0] + radius * math.cos(angle)
   y = center[1] + radius * math.sin(angle)
   polygon.append((int(x), int(y)))

# Asignar un vector normal a cada vértice.
# Se utiliza una componente z no nula para simular una variación en la iluminación.
vertex_normals = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    n = np.array([math.cos(angle), math.sin(angle), 0.5])
    n = normalize(n)
    vertex_normals.append(n)

# Asignar un color base a cada vértice (valores RGB en [0,255])
vertex_colors = [
    (255, 0, 0),     # Rojo
    (255, 127, 0),   # Naranja
    (255, 255, 0),   # Amarillo
    (0, 255, 0),     # Verde
    (0, 255, 255),   # Cian
    (0, 0, 255),     # Azul
    (127, 0, 255),   # Indigo
    (255, 0, 255),   # Magenta
    (255, 0, 127)    # Rosa
]

# Calcular el centroide del eneágono
cx = sum(x for x, y in polygon) / len(polygon)
cy = sum(y for x, y in polygon) / len(polygon)
centroid = (int(cx), int(cy))

# Calcular el vector normal del centroide como promedio de los vértices
centroid_normal = np.mean(vertex_normals, axis=0)
centroid_normal = normalize(centroid_normal)

# Calcular el color base del centroide como el promedio de los colores de los vértices
centroid_color = tuple(np.mean(vertex_colors, axis=0).astype(np.uint8))

# Parámetros para el modelo Phong
light_dir = normalize(np.array([1, 1, 1]))  # Dirección de la luz
view_dir = normalize(np.array([0, 0, 1]))   # Dirección de la cámara (vista frontal)

# Triangular el eneágono usando el centroide (triangulación en abanico)
for i in range(num_sides):
    v1 = polygon[i]
    v2 = polygon[(i + 1) % num_sides]
    n1 = vertex_normals[i]
    n2 = vertex_normals[(i + 1) % num_sides]
    c1 = vertex_colors[i]
    c2 = vertex_colors[(i + 1) % num_sides]
    
    # Definir el triángulo: dos vértices del eneágono y el centroide
    triangle = [v1, v2, centroid]
    triangle_normals = [n1, n2, centroid_normal]
    triangle_colors = [c1, c2, centroid_color]
    triangle_phong_fill_color(img_array, triangle, triangle_normals, triangle_colors,
                               light_dir, view_dir,
                               ambient=0.1, diffuse_coef=0.8, specular_coef=0.5, shininess=20)

# Convertir el arreglo modificado de vuelta a una imagen PIL
img_out = Image.fromarray(img_array)

# Visualizar el resultado
plt.figure(figsize=(6, 6))
plt.imshow(img_out)
plt.axis('off')
plt.title("Eneágono con Sombreado Phong en Color")
plt.show()