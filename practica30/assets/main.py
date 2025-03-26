import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def crear_cubo():
    """
    Crea un cubo centrado en el orign con lados de longitud 2.
    Devuelve:
        vertices: array con las coordenadas (x, y, z) de cada vértice.
        caras: lista de caras del cubo, donde cada cara es una lista de vértices.
    """
    # Definir los vértices del cubo
    vertices = np.array([[-1, -1, -1],
                        [1, -1, -1],
                        [1, 1, -1],
                        [-1, 1, -1],
                        [-1, -1, 1],
                        [1, -1, 1],
                        [1, 1, 1],
                        [-1, 1, 1]])

    # Definir las caras del cubo usando los índices de los vértices
    caras = [[vertices[j] for j in [0, 1, 2, 3]],  # Cara trasera
        [vertices[j] for j in [4, 5, 6, 7]],  # Cara frontal
        [vertices[j] for j in [0, 1, 5, 4]],  # Cara inferior
        [vertices[j] for j in [2, 3, 7, 6]],  # Cara superior
        [vertices[j] for j in [1, 2, 6, 5]],  # Cara derecha
        [vertices[j] for j in [4, 7, 3, 0]]]  # Cara izquierda]
    return vertices, caras

def rotacion_y(vertices, angulo):
    """
    Aplica una rotación al cubo alrededor del eje Y.

    Parámetros:
        vertices: array de vértices (n, 3).
        angulo: ángulo de rotación en radianes.
    Retorna:
        vertices_rotados: array con los vértices rotados.
    """
    # Matriz de rotación para el eje Y
    cos_a = np.cos(angulo)
    sin_a = np.sin(angulo)
    R_y = np.array([[cos_a, 0, sin_a],
                    [0, 1, 0],
                    [-sin_a, 0, cos_a]])
    # Se aplica la rotación a cada vértice
    return vertices.dot(R_y.T)

# Configuración de la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Crear el cubo inicial
vertices, caras = crear_cubo()
poly = Poly3DCollection(caras, facecolors="lightblue", edgecolors="black", alpha=0.8)
ax.add_collection3d(poly)

# Establecer límites y etiquetas del gráfico
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

def update(frame):
    """
    Actualiza la rotación del cubo y la vista del gráfico.
    - Se rota el cubo alrededor del eje Y.
    - Se actualiza el ángulo de la cámara para obtener un efecto dinámico.
    """
    # Convertir el ángulo a radianes
    angulo = np.deg2rad(-frame * 3)
    # Rotar los vértices del cubo
    vertices_rot = rotacion_y(vertices, angulo)

    # Recalcular las caras con los neuvos vertices rotados
    caras_rotadas = [[vertices_rot[j] for j in [0, 1, 2, 3]],
        [vertices_rot[j] for j in [4, 5, 6, 7]],
        [vertices_rot[j] for j in [0, 1, 5, 4]],
        [vertices_rot[j] for j in [2, 3, 7, 6]],
        [vertices_rot[j] for j in [1, 2, 6, 5]],
        [vertices_rot[j] for j in [4, 7, 3, 0]]]
    poly.set_verts(caras_rotadas)

    # Actualizar la vista: se rota la cámara para mejorar al visualización dinámica
    ax.view_init(elev=30, azim=frame)
    ax.set_title(f"Rotación: {frame}°")
    return (poly,)

# Crear la animación: el ángulo de 0 a 360 con incrementos de 2 grados
anim = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=False)

# Mostrar la animación
plt.show()