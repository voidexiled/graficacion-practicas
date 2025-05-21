import pygame
import sys

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Onion Skinning")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
SHADOW_COLOR = (255, 0, 0, 40) # Color traslucido para sombra

clock = pygame.time.Clock()
fps = 60

# Posiciones de cuadros anteriores para onion skinning
history = []
max_trail = 10 # cantidad de cuadrso pasados que se muestra

# Objeto animado
x,y = 100, HEIGHT // 2
speed = 3
radius = 30

# Loop principal
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar posición
    x += speed
    if x > WIDTH + radius:
        x = -radius
        history.clear()
    
    # Guardar la posición actual en el historial
    history.append((x, y))
    if len(history) > max_trail:
        history.pop(0)
        
    # Dibujar
    screen.fill(WHITE)
    
    # Dibujar sombras anteriores (onion skinning)
    for i, (hx, hy) in enumerate(history):
        alpha = int(255 * ((i + 1) / max_trail)) // 6 # gradiente de opacidad
        shadow_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(shadow_surface, (255, 0, 0, alpha), (radius, radius), radius)
        screen.blit(shadow_surface, (hx - radius, hy - radius))    
        
    # Dibujar objeto actual
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()

pygame.quit()
sys.exit()