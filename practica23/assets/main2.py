import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

Z = np.sin(X**2 + Y**2) / (X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="k", alpha=0.7)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Modelado de superficies, Paraboloide")


# Función de animación
def update(frame):
    ax.view_init(
        elev=30, azim=frame
    )  # Cambia azim para girar en Z, usa elev para girar en X


ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

plt.show()
