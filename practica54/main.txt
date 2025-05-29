import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random
import math

# ------ CONFIGURACIÓN DEL MUNDO Y MULTITUD ------

NUM_AGENTS = 100
WORLD_SIZE = 20

class Agent:
    def __init__(self): # ¡CORRECCIÓN AQUÍ: DOBLE GUION BAJO!
        self.position = np.array([
            random.uniform(-WORLD_SIZE, WORLD_SIZE),
            0,
            random.uniform(-WORLD_SIZE, WORLD_SIZE)
        ])
        angle = random.uniform(0, 2 * math.pi)
        self.direction = np.array([math.cos(angle), 0, math.sin(angle)])
        self.speed = random.uniform(0.03, 0.07)

    def update(self):
        self.position += self.direction * self.speed

        # Rebote si toca el límite del mundo
        for i in [0, 2]: # Solo revisa X y Z, asumiendo Y es fijo o no limitado
            if abs(self.position[i]) > WORLD_SIZE:
                self.direction[i] *= -1
                self.position[i] = np.clip(self.position[i], -WORLD_SIZE, WORLD_SIZE)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glScalef(0.5, 1.0, 0.5) # Hace los agentes un poco más altos que anchos/profundos
        draw_cube()
        glPopMatrix()

# ------ DIBUJO DE ESCENA ------
def draw_ground():
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_LINES)
    for i in range(-WORLD_SIZE, WORLD_SIZE + 1):
        glVertex3f(i, 0, -WORLD_SIZE)
        glVertex3f(i, 0, WORLD_SIZE)
        glVertex3f(-WORLD_SIZE, 0, i)
        glVertex3f(WORLD_SIZE, 0, i)
    glEnd()

def draw_cube():
    glColor3f(0.6, 0.8, 1.0) # Color azulado para los cubos
    vertices = [
        [ 1, 0, -1], [ 1, 2, -1], [-1, 2, -1], [-1, 0, -1], # Cara frontal (y=0 a y=2)
        [ 1, 0,  1], [ 1, 2,  1], [-1, 2,  1], [-1, 0,  1]  # Cara trasera
    ]
    edges = [
        (0,1),(1,2),(2,3),(3,0), # Bordes cara frontal
        (4,5),(5,6),(6,7),(7,4), # Bordes cara trasera
        (0,4),(1,5),(2,6),(3,7)  # Bordes conectando caras
    ]
    glBegin(GL_LINES)
    for edge in edges:
        for v_index in edge:
            glVertex3fv(vertices[v_index])
    glEnd()

# ------ OPENGL Y SIMULACIÓN ------
def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.05, 0.05, 0.05, 1) # Fondo gris oscuro

def main():
    pygame.init()
    display = (1000, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Crowds 3D Simulation - 100 Agents")

    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    glTranslatef(0, -3, -40) # Mover la cámara hacia atrás y un poco hacia abajo
    glRotatef(30, 1, 0, 0) # Rotar un poco la vista hacia abajo

    init_opengl()

    agents = [Agent() for _ in range(NUM_AGENTS)]

    clock = pygame.time.Clock()
    running = True
    angle = 0 # Para rotar la escena

    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glPushMatrix()
        glRotatef(angle, 0, 1, 0) # Rotar toda la escena alrededor del eje Y
        draw_ground()

        for agent in agents:
            agent.update()
            agent.draw()
        glPopMatrix() # Fin de la rotación de la escena

        pygame.display.flip()
        clock.tick(60)
        angle += 0.2 # Incrementar el ángulo de rotación

    pygame.quit()

if __name__ == "__main__":
    main()
