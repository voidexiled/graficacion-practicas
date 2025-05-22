import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

# ------- Utilidades OPENGL ------- 

def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.1, 0.1, 0.1, 1)
    glLineWidth(5)
    
def draw_bone(length=1.0):
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, length, 0)
    glEnd()
    # Dibuja una pequeña esfera en el extremo
    draw_sphere(0.1, 0, length, 0)
    
def draw_sphere(radius, x, y, z):
    """ Esfera en una posición"""
    glPushMatrix()
    glTranslatef(x, y, z)
    quad = gluNewQuadric()
    gluSphere(quad, radius, 8, 8)
    glPopMatrix()
    
# ------- ANIMACIÓN ESQUELÉTICA -------

def draw_skeleton(shoulder_angle, elbow_angle, wrist_angle):
    glColor3f(0.5, 0.8, 1.0)
    
    # Articulación 1: hombre
    glPushMatrix()
    glRotatef(shoulder_angle, 0, 0, 1)
    draw_bone(2.0)
    
    # Articulación 2: codo (relativa al hombro)
    glTranslatef(0, 2.0, 0)
    glRotatef(elbow_angle, 0, 0, 1)
    draw_bone(1.5)
    
    # Articulación 3: muñeca (relativa al codo)
    glTranslatef(0, 1.5, 0)
    glRotatef(wrist_angle, 0, 0, 1)
    draw_bone(1.0)
    
    glPopMatrix()
    
# ------- LOOP PRINCIPAL -------

def main():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Skeletal Animation 3D - Esqueleto Jerárquico')
    
    gluPerspective(45, display[0] / display[1], 0.1, 100)
    glTranslatef(0.0, -2.0, -10)
    
    init_opengl()
    
    angle = 0
    clock = pygame.time.Clock()
    running = True
    
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        for event in pygame.event.get():
            if event.type == QUIT:        
                running = False
                
        # Animación de cada hueso
        shoulder = 30 * math.sin(math.radians(angle))
        elbow = 45 * math.sin(math.radians(angle * 2))
        wrist =  60 * math.sin(math.radians(angle * 3))
        
        # Rotación global del modelo
        glPushMatrix()
        glRotatef(angle * 0.3, 0, 1, 0)
        draw_skeleton(shoulder, elbow, wrist)
        glPopMatrix()
        
        pygame.display.flip()
        clock.tick(60)
        angle += 2
        
    pygame.quit()
    
if __name__ == '__main__':
    main()