import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# ______ DEFINICIÓN DEL ESQUELETO ______
# Cada par (i, j) representa un hueso que conecta el punto i al punto j
bones = [
    (0, 1), # pelvis -> torso
    (1, 2), # torso -> cuello
    (2, 3), # cuello -> cabeza
    (1, 4), # torso -> brazo izq
    (4, 5), # brazo izq -> antebrazo izq
    (1, 6), # torso -> brazo der
    (6, 7), # brazo der -> antebrazo der
    (0, 8), # pelvis -> pierna izq
    (8, 9), # pierna izq -> pie izq
    (0, 10), # pelvis -> pierna der
    (10, 11) # pierna der -> pie der
]

# FRAMES DE MOCAP SIMULADOS (12 puntos por frame)
def generate_mock_mocap_frames(num_frames=120):
    frames = []
    for t in range(num_frames):
        angle = np.radians(t * 3)
        points = np.array([
            [0, 0, 0],    # 0 pelvis
            [0, 1, 0],    # 1 torso
            [0, 2, 0],    # 2 cuello
            [0, 2.5, 0.2*np.sin(angle)], # 3 cabeza
            [-0.5, 1.8, 0.2*np.sin(angle)],    # 4 brazo izq
            [-1, 1.6, 0.4*np.sin(angle)],    # 5 antebrazo izq
            [0.5, 1.8, -0.2*np.sin(angle)],    # 6 brazo der
            [1, 1.6, -0.4*np.sin(angle)],    # 7 antebrazo der
            [-0.3, -1, 0.1*np.cos(angle)],    # 8 pierna izq
            [-0.3, -2, 0.2*np.cos(angle)],    # 9 pie izq
            [0.3, -1, -0.1*np.cos(angle)],    # 10 pierna der
            [0.3, -2, -0.2*np.cos(angle)],    # 11 pie der
        ])
        frames.append(points)
    return frames

# FUNCIONES DE DIBUJO
def draw_skeleton(points):
    glColor3f(0.6, 0.9, 1.0)
    glBegin(GL_LINES)
    for i, j in bones:
        glVertex3fv(points[i])
        glVertex3fv(points[j])
    glEnd()

    glPointSize(6)
    glColor3f(1, 0.5, 0.2)
    glBegin(GL_POINTS)
    for p in points:
        glVertex3fv(p)
    glEnd()

# ______ OPENGL Y LOOP PRINCIPAL ______
def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.05, 0.05, 0.05, 1)

def main():
    pygame.init()
    display = (1000, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Motion Capture 3D - Demo Skeleton")

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0, -1.0, -8)

    init_opengl()
    mocap_frames = generate_mock_mocap_frames()
    frame_count = len(mocap_frames)
    clock = pygame.time.Clock()
    angle = 0
    frame_index = 0

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glPushMatrix()
        glRotatef(angle, 0, 1, 0)
        draw_skeleton(mocap_frames[frame_index])
        glPopMatrix()

        frame_index = (frame_index + 1) % frame_count
        angle += 0.5

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
