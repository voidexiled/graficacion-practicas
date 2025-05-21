import numpy as np
import matplotlib.pyplot as plt

# Dimensiones de la imagen
width, height = 400, 400
image = np.ones((height, width, 3))

# Definición de los vértices del triángulo (coordenadas en píxeles)
v0 = np.array([100, 100])
v1 = np.array([300, 180])
v2 = np.array([200, 300])
vertices = np.array([v0, v1, v2])

# Colores asociados a cada vértice (en formato RGB, valores entre 0 y 1)
color_v0 = np.array([1.0, 0.0, 0.0])  # Rojo
color_v1 = np.array([0.0, 1.0, 0.0])  # Verde
color_v2 = np.array([0.0, 0.0, 1.0])  # Azul
colors = np.array([color_v0, color_v1, color_v2])

def barycentric_coords(p, a, b, c):
    """
    Calcula las coordenadas baricéntricas de un punto p
    con respecto al triángulo formado por los puntos a, b y c.
    """
    # Vectores del triángulo
    v0 = b - a
    v1 = c - a
    v2 = p - a

    # Producto cruzado (área * 2) para la región del triángulo
    denom = v0[0] * v1[1] - v1[0] * v0[1]

    # Evitar división por cero (triángulo degenerado)
    if np.abs(denom) < 1e-6:
        return -1, -1, -1

    # Cálculo de las coordenadas baricéntricas
    alpha = (v2[0] * v1[1] - v1[0] * v2[1]) / denom
    beta  = (v0[0] * v2[1] - v2[0] * v0[1]) / denom
    gamma = 1 - alpha - beta

    return alpha, beta, gamma

# Calcular el rectángulo contenedor (bounding box) del triángulo
min_x = int(np.clip(np.min(vertices[:, 0]), 0, width-1))
max_x = int(np.clip(np.max(vertices[:, 0]), 0, width-1))
min_y = int(np.clip(np.min(vertices[:, 1]), 0, height-1))
max_y = int(np.clip(np.max(vertices[:, 1]), 0, height-1))

# Recorrer los píxeles dentro del bounding box
for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        p = np.array([x, y])

        # Obtener coordenadas baricéntricas para el píxel
        alpha, beta, gamma = barycentric_coords(p, v0, v1, v2)

        # Verificar si el punto se encuentra dentro del triángulo
        if alpha >= 0 and beta >= 0 and gamma >= 0:
            # Interpolación de colores usando las coordenadas baricéntricas
            pixel_color = alpha * color_v0 + beta * color_v1 + gamma * color_v2
            image[y, x] = pixel_color

# Mostrar el resultado
plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.title("Sombreado con Interpolación (Baricéntrico)")
plt.axis("off")
plt.show()
