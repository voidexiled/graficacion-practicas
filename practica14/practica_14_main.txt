import numpy as np
import matplotlib.pyplot as plt


def aplicar_transformacion(puntos, matriz):

    puntos_homogeneos = np.c_[puntos, np.ones(len(puntos))].T
    puntos_transformados = matriz @ puntos_homogeneos
    return puntos_transformados[:2].T


puntos_originales = np.array([[1, 1], [3, 1], [3, 3], [1, 3], [1, 1]])

theta = np.radians(30)

tx, ty = 2, 1

matriz_transformacion = np.array(
    [[np.cos(theta), -np.sin(theta), tx], [np.sin(theta), np.cos(theta), ty], [0, 0, 1]]
)

puntos_transformados = aplicar_transformacion(puntos_originales, matriz_transformacion)

plt.figure(figsize=(6, 6))
plt.plot(puntos_originales[:, 0], puntos_originales[:, 1], "bo-", label="Original")
plt.plot(
    puntos_transformados[:, 0], puntos_transformados[:, 1], "ro-", label="Transformados"
)

plt.xlim(-2, 6)
plt.ylim(-2, 6)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Transformacion Matrcial (Mostrar+ transicion)")
plt.show()
