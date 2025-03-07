import numpy as np
import matplotlib.pyplot as plt

from scipy.special import comb


def bezier_cube(control_points, num_points=100):
    n = len(control_points) - 1
    t = np.linspace(0, 1, num_points)
    curve = np.zeros((num_points, 2))
    for i in range(n + 1):
        binomial_coef = comb(n, i)
        term = (binomial_coef * (t**i) * ((i - t) ** (n - i)))[:, np.newaxis]
        curve += term * np.array(control_points[i])
    return curve[:, 0], curve[:, 1]


control_points = [(0, 0), (1, 2), (3, 3), (4, 0)]
x, y = bezier_cube(control_points)  # type: ignore
plt.plot(x, y, label="Curva")
plt.scatter(*zip(*control_points), color="red", label="Puntos de control")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Curve de Beizer en Python")
plt.grid()
plt.show()
