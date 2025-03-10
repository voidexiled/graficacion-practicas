# importando la biblioteca
import matplotlib.pyplot as plt

activities = ["alimentos", "dormir", "trabajo", "jugar"]

slices = [3, 7, 8, 6]
colors = ["r", "y", "g", "b"]
plt.pie(
    slices,
    labels=activities,
    colors=colors,
    startangle=90,
    shadow=True,
    explode=(0, 0, 0.1, 0),
    radius=1.2,
    autopct="%1.1f%%",
)
plt.legend()
plt.title("Sector Circular")
plt.show()
