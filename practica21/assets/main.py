import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

ax.text(1, 9, "Texto Clásico", fontsize=14, color="navy", fontname="Comic Sans MS")
ax.text(
    1,
    8,
    "Texto Elegante",
    fontsize=14,
    fontweight="bold",
    color="darkred",
    fontname="Times New Roman",
)
ax.text(
    1,
    7,
    "Texto Moderno",
    fontsize=14,
    fontstyle="italic",
    color="teal",
    fontname="Arial",
)
ax.text(
    1,
    6,
    "Texto Destacado",
    fontsize=14,
    color="darkorange",
    bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightyellow"),
)
ax.text(
    1,
    5,
    "Texto con Efecto",
    fontsize=14,
    color="purple",
    path_effects=[path_effects.withStroke(linewidth=3, foreground="gray")],
)
ax.text(
    1,
    4,
    "Texto Inclinado",
    fontsize=14,
    rotation=30,
    color="indigo",
    fontname="Verdana",
)
ax.text(1, 3, "Texto Cientifico", fontsize=14, fontname="Georgia", color="maroon")
ax.text(1, 2, "Texto Digital", fontsize=14, fontname="Courier New", color="dodgerblue")
ax.text(1, 1, "Texto Especial: E=mc", fontsize=14, color="black", fontname="Calibri")

plt.show()
