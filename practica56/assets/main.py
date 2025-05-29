import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = (
    (-1, -1, -1),
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1,  1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1,  1,  1)
)

edges = (
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
)

faces = (
    (0,1,2,3),
    (4,5,6,7),
    (0,1,5,4),
    (2,3,7,6),
    (1,2,6,5),
    (0,3,7,4)
)

colors = [
    (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (1,0,1), (0,1,1)
]

def draw_cube(intensity):
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        color = colors[i]
        r = min(max(color[0] * intensity, 0.0), 1.0)
        g = min(max(color[1] * intensity, 0.0), 1.0)
        b = min(max(color[2] * intensity, 0.0), 1.0)
        glColor3f(r, g, b)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Cubo 3D Interactivo - PyOpenGL")

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    rot_x = rot_y = rot_z = 0
    zoom = -7
    color_intensity = 1.0

    clock = pygame.time.Clock()
    running = True
    ticks_ago = 0
    while running:
        dt = clock.tick(60) / 1000
        ticks_ago += 1
        print(ticks_ago)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        random = np.random.randint(0, 1)
        if ticks_ago > 140:
            rot_x -= 90 * dt
            rot_y += 90 * dt
            zoom += 2 * dt
            if ticks_ago > 280:
                ticks_ago = 0
        else:
            rot_x += 90 * dt
            rot_y -= 90 * dt
            zoom -= 2 * dt
            

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            rot_x -= 90 * dt
        if keys[K_DOWN]:
            rot_x += 90 * dt
        if keys[K_LEFT]:
            rot_y -= 90 * dt
        if keys[K_RIGHT]:
            rot_y += 90 * dt
        if keys[K_q]:
            rot_z -= 90 * dt
        if keys[K_e]:
            rot_z += 90 * dt
        if keys[K_w]:
            zoom += 5 * dt
        if keys[K_s]:
            zoom -= 5 * dt
        if keys[K_a]:
            color_intensity = max(0.1, color_intensity - 0.5 * dt)
        if keys[K_d]:
            color_intensity = min(2.0, color_intensity + 0.5 * dt)
        if keys[K_r]:
            rot_x = rot_y = rot_z = 0
            zoom = -7
            color_intensity = 1.0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)
        glRotatef(rot_z, 0, 0, 1)

        draw_cube(color_intensity)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
