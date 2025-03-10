# importando la biblioteca
import matplotlib.pyplot as plt

# valores del eje x.
x = [1, 2, 3]
# valores correspondientes al eje
y = [2, 4, 1]
# Graficando los puntos.
plt.plot(x, y)

# etiqueta del eje x
plt.xlabel("eje x")
# etiqueta del eje y
plt.ylabel("eje y")

# escribiendo el titulo de la grafica
plt.title("rectas")
# muestra la grafica de la funcion
plt.show()
