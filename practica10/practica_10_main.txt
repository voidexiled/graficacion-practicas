def traslacion(punto, tx, ty):
    x, y = punto
    return (x + tx, y + ty)


# punto original
punto = (3, 5)

# Desplazar 4 unidades en X y 2 en Y
nuevo_punto = traslacion(punto, 4, 2)

print(f"Punto original:{punto}")
print(f"Punto trasladado:{nuevo_punto}")
