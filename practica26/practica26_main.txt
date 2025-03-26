import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crear una malla par alos ejes X e Y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Definir tres superficies planas (planos)
# Plano 1: z = 0 (plano horizontal)
Z1 = np.zeros_like(X)

# Plano 2: z = 0.5*x + 0.2*y + 1
Z2 = 0.5 * X + 0.2 * Y + 1

# Plano 3: z = -0.3*x + 0.4*y - 1
Z3 = 0.3 * X + 0.4 * Y - 1

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Graficar cada superficie con transparencia para ver las intersecciones
ax.plot_surface(
    X, Y, Z1, alpha=0.5, color="blue", rstride=1, cstride=1, edgecolor="none"
)
ax.plot_surface(
    X, Y, Z2, alpha=0.5, color="red", rstride=1, cstride=1, edgecolor="none"
)
ax.plot_surface(
    X, Y, Z3, alpha=0.5, color="green", rstride=1, cstride=1, edgecolor="none"
)

# Configurar etiquetas y título
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Superficies Planas en 3D con Animación")


def update(angle):
    ax.view_init(elev=30, azim=angle)
    return (ax,)


# Crear la animación: se rotará la vista de 0 a 360 grados
anim = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# Mostrar la gráfica animada
plt.show()
