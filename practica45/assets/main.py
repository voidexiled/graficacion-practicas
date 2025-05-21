import pygame
import sys

#Inicializacion
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Tweening Acelerado")

#Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Posiciones clave
start_x = 100
end_x = 700
y = HEIGHT // 2
radius = 30

#Parametros de animacion
duration = 1.0 #segundos
clock = pygame.time.Clock()
fps = 60
total_frames = int(duration * fps)
frame = 0

#Loop principal
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Tween acelerado (cuafratico)
    t= frame/ total_frames
    if t> 1:
        t=1
    t_squared = t*t
    x= int(start_x + (end_x - start_x)* t_squared)

    #Dibujar
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x,y), radius)
    pygame.display.flip()

    frame += 1
    if frame > total_frames:
        pygame.time.wait(1000)
        frame = 0 #Reiniciar animacion

pygame.quit()
sys.exit()
