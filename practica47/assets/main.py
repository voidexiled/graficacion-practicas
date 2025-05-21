import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Morfing - Cuadrado a Estrella")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255) # Asumo este color, puede ser otro azul

clock = pygame.time.Clock()
fps = 60
duration = 3  # segundos
total_frames = duration * fps

# Definir dos formas con el mismo número de puntos
def get_square(center, size):
    cx, cy = center
    half = size // 2 # Use integer division for pixel coordinates
    return [
        (cx - half, cy - half),
        (cx + half, cy - half),
        (cx + half, cy + half),
        (cx - half, cy + half)
    ]

def get_star(center, size):
    cx, cy = center
    points = []
    for i in range(4): # The screenshot seems to imply range(4) based on points[:4]
        angle = i * (math.pi / 2)
        outer_x = cx + math.cos(angle) * size
        outer_y = cy + math.sin(angle) * size

        inner_angle = angle + math.pi / 4
        inner_x = cx + math.cos(inner_angle) * (size * 0.5)
        inner_y = cy + math.sin(inner_angle) * (size * 0.5)

        points.extend([(outer_x, outer_y), (inner_x, inner_y)])

    return points[:4]

def interpolate_points(p1_list, p2_list, t):
    interpolated_points = []
    for (x1, y1), (x2, y2) in zip(p1_list, p2_list):
        ix = int(x1 + (x2 - x1) * t)
        iy = int(y1 + (y2 - y1) * t)
        interpolated_points.append((ix, iy))
    return interpolated_points

center = (WIDTH // 2, HEIGHT // 2)
size = 150

shape_a = get_square(center, size)
shape_b = get_star(center, size) # This will be the 4-point "star"

frame = 0
running = True

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    t = (frame % total_frames) / total_frames

    if (frame // total_frames) % 2 == 1:
        # Reverse morph (shape_b to shape_a)
        current_shape = interpolate_points(shape_b, shape_a, t)
    else:
        # Forward morph (shape_a to shape_b)
        current_shape = interpolate_points(shape_a, shape_b, t)

    screen.fill(WHITE)
    if current_shape and len(current_shape) >= 3: # Need at least 3 points for a polygon
        pygame.draw.polygon(screen, BLUE, current_shape)
    pygame.display.flip()

    frame += 1

pygame.quit()
sys.exit()
