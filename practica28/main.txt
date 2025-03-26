import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation  # Para la animación


def traslacion_3d(punto, tx, ty, tz):
    """
    Aplica una transformación de traslación 3D a un punto.

    Args:
        punto: un Array NumPy de 3 elementos que presenta el punto (x, y, z).
        tx: La cantidad de traslación en el eje X,
        ty: La cantidad de traslación en el eje Y,
        tz: La cantidad de traslación en el eje Z

    Returns:
        Un array NumPy de 3 elementos que representa el punto trasladado.
    """

    matriz_traslacion = np.array(
        [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]]
    )

    punto_homogeneo = np.append(punto, 1)
    punto_trasladado_homogeneo = np.dot(matriz_traslacion, punto_homogeneo)
    punto_trasladado = punto_trasladado_homogeneo[:3]

    return punto_trasladado


# Ejemplo de uso
punto_original = np.array([1, 2, 3])
tx = 5
ty = -2
tz = 1

punto_trasladado = traslacion_3d(punto_original, tx, ty, tz)

print("Punto original:", punto_original)
print("Punto trasladado:", punto_trasladado)

# Gráfica 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Puntos
ax.scatter(
    punto_original[0],
    punto_original[1],
    punto_original[2],
    c="r",
    marker="o",
    label="Punto Original",
)
ax.scatter(
    punto_trasladado[0],
    punto_trasladado[1],
    punto_trasladado[2],
    c="b",
    marker="^",
    label="Punto Trasladado",
)

# Ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.plot(
    [punto_original[0], punto_trasladado[0]],
    [punto_original[1], punto_trasladado[1]],
    [punto_original[2], punto_trasladado[2]],
    "g--",
)

plt.legend()
plt.title("Traslación 3D")


# Definir la función de actualizacion para la animación
def update(angle):
    ax.view_init(elev=30, azim=angle)
    return (ax,)


# Crear la animación: rotará la vista de 0 a 360 grados
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
plt.show()
