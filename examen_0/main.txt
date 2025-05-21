import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def draw_hexagon_gradient():
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    # Definir los vértices del hexágono (inscrito en un círculo de radio 1)
    theta = np.linspace(0, 2 * np.pi, 7)
    vertices = np.column_stack([np.cos(theta), np.sin(theta)])

    # Crear una malla de puntos que cubre el área del hexágono
    nx, ny = 500, 500
    x = np.linspace(-1, 1, nx)
    y = np.linspace(-1, 1, ny)
    X, Y = np.meshgrid(x, y)

    # Crear el degradado: se varía el color según la coordenada x
    # Normalizar x para que varíe de 0 (izquierda) a 1 (derecha)
    norm_x = (X + 1) / 2
    grad = np.empty((ny, nx, 3))
    grad[:, :, 0] = norm_x  # Canal rojo aumenta de izquierda a derecha
    grad[:, :, 1] = 0  # Canal verde en 0
    grad[:, :, 2] = 1 - norm_x  # Canal azul disminuye de izquierda a derecha

    # Crear una máscara para que el degradado se aplique solo dentro del hexágono
    hex_path = Path(vertices)
    points = np.column_stack((X.ravel(), Y.ravel()))
    mask = hex_path.contains_points(points).reshape((ny, nx))

    # Establecer el degradado fuera del hexágono (por ejemplo, en blanco)
    grad[~mask] = [1, 1, 1]

    # Mostrar el degradado usando imshow
    ax.imshow(grad, extent=[-1, 1, -1, 1], origin="lower")

    # Dibujar el contorno del hexágono
    hexagon = patches.Polygon(
        vertices, closed=True, fill=False, edgecolor="black", linewidth=2
    )
    ax.add_patch(hexagon)

    plt.show()


draw_hexagon_gradient()
