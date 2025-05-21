import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Si usas Jupyter, puedes omitir esta línea y utilizar %matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def crear_cubo():
    """
    Crea un cubo centrado en el origen con lados de longitud 2.
    Devuelve:
        vertices: array con las coordenadas (x, y, z) de cada vértice.
        caras: lista de caras del cubo, donde cada cara es una lista de vértices.
    """
    vertices = np.array([[-1, -1, -1],
                       [ 1, -1, -1],
                       [ 1,  1, -1],
                       [-1,  1, -1],
                       [-1, -1,  1],
                       [ 1, -1,  1],
                       [ 1,  1,  1],
                       [-1,  1,  1]])

    caras = [ [vertices[j] for j in [0, 1, 2, 3]],  # Cara trasera
              [vertices[j] for j in [4, 5, 6, 7]],  # Cara frontal
              [vertices[j] for j in [0, 1, 5, 4]],  # Cara inferior
              [vertices[j] for j in [2, 3, 7, 6]],  # Cara superior
              [vertices[j] for j in [1, 2, 6, 5]],  # Cara derecha
              [vertices[j] for j in [4, 7, 3, 0]] ] # Cara izquierda
    return vertices, caras

def sesgar_x_z(vertices, shear_factor):
    """
    Aplica una transformación de sesgado al cubo.

    Se sesga el eje X en función de la coordenada Z:
        x' = x + shear_factor * z
        y' = y
        z' = z

    Parámetros:
        vertices: array de vértices (n, 3).
        shear_factor: factor de sesgado.
    Retorna:
        vertices_sesgados: array con los vértices transformados.
    """
    # Matriz de sesgado para transformar X en función de Z.
    shear_matrix = np.array([[1, 0, shear_factor],
                             [0, 1, 0],
                             [0, 0, 1]])
    return vertices.dot(shear_matrix.T)

# Configuración de la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear el cubo inicial
vertices, caras = crear_cubo()
poly = Poly3DCollection(caras, facecolors='lightcoral', edgecolors='black', alpha=0.8)
ax.add_collection3d(poly)

# Establecer límites y etiquetas de los ejes
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def update(frame):
    """
    Actualiza el sesgado del cubo y la vista del gráfico.
    - Se aplica un factor de sesgado que oscila de forma sinusoidal.
    - Se aplica la transformación de sesgado a los vértices del cubo.
    - Se actualizan las caras del cubo y se rota la vista (ángulo azimutal).
    """
    # Oscilación del factor de sesgado
    shear_factor = 0.5 * np.sin(np.deg2rad(frame))
    vertices_sesgados = sesgar_x_z(vertices, shear_factor)

    # Recalcular las caras con los nuevos vértices transformados
    caras_sesgadas = [[vertices_sesgados[j] for j in [0, 1, 2, 3]],
                     [vertices_sesgados[j] for j in [4, 5, 6, 7]],
                     [vertices_sesgados[j] for j in [0, 1, 5, 4]],
                     [vertices_sesgados[j] for j in [2, 3, 7, 6]],
                     [vertices_sesgados[j] for j in [1, 2, 6, 5]],
                     [vertices_sesgados[j] for j in [4, 7, 3, 0]]]
    poly.set_verts(caras_sesgadas)

    # Actualizar la vista: rotación de la cámara para un efecto dinámico
    ax.view_init(elev=30, azim=frame)
    ax.set_title(f"Sesgado: factor {shear_factor:.2f}")
    return poly,

# Crear la animación: el parámetro 'frame' varía de 0 a 360º en pasos de 2º
anim = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=False)

# Mostrar la animación
plt.show()
