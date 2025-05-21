import pygame
import numpy as np

# Inicialización
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pentágono con sombreado Gouraud (NumPy)")
clock = pygame.time.Clock()

# Centro y radio
cx, cy = 300, 300
radius = 200
num_vertices = 5

# Generar coordenadas del pentágono
angles = np.linspace(-np.pi / 2, 3 * np.pi / 2, num_vertices, endpoint=False)
vertices = np.stack([
    cx + radius * np.cos(angles),
    cy + radius * np.sin(angles)
], axis=-1)

# Colores RGB por vértice
vertex_colors = np.array([
    [255, 0, 0],    # Rojo
    [0, 255, 0],    # Verde
    [0, 0, 255],    # Azul
    [255, 255, 0],  # Amarillo
    [255, 0, 255]   # Magenta
])

# Centro del pentágono
center = np.array([cx, cy])
center_color = vertex_colors.mean(axis=0)

# Función de coordenadas baricéntricas
def barycentric_coords(p, a, b, c):
    v0 = b - a
    v1 = c - a
    v2 = p - a
    d00 = np.dot(v0, v0)
    d01 = np.dot(v0, v1)
    d11 = np.dot(v1, v1)
    d20 = np.dot(v2, v0)
    d21 = np.dot(v2, v1)
    denom = d00 * d11 - d01 * d01
    if denom == 0:
        return -1, -1, -1
    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1.0 - v - w
    return u, v, w

# Dibujar triángulo con interpolación Gouraud
def draw_gouraud_triangle(a, b, c, ca, cb, cc):
    min_x = int(min(a[0], b[0], c[0]))
    max_x = int(max(a[0], b[0], c[0]))
    min_y = int(min(a[1], b[1], c[1]))
    max_y = int(max(a[1], b[1], c[1]))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            p = np.array([x, y])
            u, v, w = barycentric_coords(p, a, b, c)
            if u >= 0 and v >= 0 and w >= 0:
                color = u * ca + v * cb + w * cc
                color = np.clip(color, 0, 255).astype(int)
                screen.set_at((x, y), color)

# Loop principal
running = True
while running:
    screen.fill((0, 0, 0))

    for i in range(num_vertices):
        a = center
        b = vertices[i]
        c = vertices[(i + 1) % num_vertices]
        ca = center_color
        cb = vertex_colors[i]
        cc = vertex_colors[(i + 1) % num_vertices]
        draw_gouraud_triangle(a, b, c, ca, cb, cc)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
