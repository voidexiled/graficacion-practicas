def sesgado(punto, sx, sy):
    x, y = punto
    x_nuevo = x + sx * y
    y_nuevo = y + sy * x
    return (x_nuevo, y_nuevo)


# Punto originsl
punto = (3, 5)

# Aplica sesgado en x = 1.2 y en Y = 0.5
nuevo_punto = sesgado(punto, 1.2, 0.5)

print(f"Punto original: {punto}")
print(f"Punto sesgado: {nuevo_punto}")
