import matplotlib.pyplot as plt
import numpy as np


def sierpinski_triangle(ax, points, depth):
    """Genera recursivamente el Triangulo de Sierpinski"""
    if depth == 0:
        triangle = plt.Polygon(points, edgecolor="black", facecolor="white")
        ax.add_patch(triangle)
    else:
        middle = (points[0] + points[1]) / 2
        mid2 = (points[1] + points[2]) / 2
        mid3 = (points[2] + points[0]) / 2

        sierpinski_triangle(ax, [points[0], middle, mid3], depth - 1)
        sierpinski_triangle(ax, [middle, points[1], mid2], depth - 1)
        sierpinski_triangle(ax, [mid3, mid2, points[2]], depth - 1)


def generate_sierpinski(depth=5):
    """Configura la figura y genera el Triangulo de Sierpinski"""
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, np.sqrt(3) / 2)

    points = np.array([[0.5, np.sqrt(3) / 2], [0, 0], [1, 0]])
    sierpinski_triangle(ax, points, depth)

    plt.show()


# Genera el Triangulo de Sierpinski
generate_sierpinski(5)
