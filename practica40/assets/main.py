import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pentágono con sombreado Phong")
clock = pygame.time.Clock()

# Configuración de iluminación y materiales
light_pos = np.array([300, 300, 200])
light_color = np.array([1.0, 1.0, 1.0])
ambient = 0.1
diffuse_strength = 0.7
specular_strength = 0.6
shininess = 32

# Geometría
cx, cy = 300, 300
radius = 200
num_vertices = 5

# Coordenadas del pentágono (2D) y sus normales (simples en Z+)
angles = np.linspace(-np.pi / 2, 3 * np.pi / 2, num_vertices, endpoint=False)
vertices_2d = np.stack([
    cx + radius * np.cos(angles),
    cy + radius * np.sin(angles)
], axis=-1)
vertices_3d = np.hstack([vertices_2d, np.zeros((num_vertices, 1))])
normals = np.tile(np.array([0, 0, 1]), (num_vertices, 1))  # todos apuntan hacia fuera de la pantalla

# Centro
center = np.array([cx, cy, 0])
center_normal = np.array([0, 0, 1])

# Barycentric interpolation
def barycentric_coords(p, a, b, c):
    v0 = b[:2] - a[:2]
    v1 = c[:2] - a[:2]
    v2 = p - a[:2]
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
    u = 1 - v - w
    return u, v, w

# Phong lighting per pixel
def compute_phong(normal, position):
    normal = normal / np.linalg.norm(normal)
    light_dir = light_pos - position
    light_dir = light_dir / np.linalg.norm(light_dir)
    view_dir = np.array([0, 0, 1])

    # Ambient
    ambient_color = ambient * light_color

    # Diffuse
    diff = max(np.dot(normal, light_dir), 0)
    diffuse_color = diffuse_strength * diff * light_color

    # Specular
    reflect_dir = 2 * np.dot(normal, light_dir) * normal - light_dir
    spec = np.power(max(np.dot(view_dir, reflect_dir), 0), shininess)
    specular_color = specular_strength * spec * light_color

    result = ambient_color + diffuse_color + specular_color
    return np.clip(result * 255, 0, 255).astype(int)

# Dibuja un triángulo con sombreado Phong
def draw_phong_triangle(v1, v2, v3, n1, n2, n3):
    min_x = int(min(v1[0], v2[0], v3[0]))
    max_x = int(max(v1[0], v2[0], v3[0]))
    min_y = int(min(v1[1], v2[1], v3[1]))
    max_y = int(max(v1[1], v2[1], v3[1]))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            p = np.array([x, y])
            u, v, w = barycentric_coords(p, v1, v2, v3)
            if u >= 0 and v >= 0 and w >= 0:
                interpolated_normal = u * n1 + v * n2 + w * n3
                interpolated_pos = u * v1 + v * v2 + w * v3
                color = compute_phong(interpolated_normal, interpolated_pos)
                screen.set_at((x, y), color)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    for i in range(num_vertices):
        v1 = center
        v2 = vertices_3d[i]
        v3 = vertices_3d[(i + 1) % num_vertices]
        n1 = center_normal
        n2 = normals[i]
        n3 = normals[(i + 1) % num_vertices]

        draw_phong_triangle(v1, v2, v3, n1, n2, n3)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
