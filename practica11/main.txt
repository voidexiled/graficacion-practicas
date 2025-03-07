def escalamiento(punto, sx, sy):
    x, y = punto
    return (x * sx, y * sy)


# Punto original
punto = (3, 5)

# Escalar por 3 un X y 0.5 en Y
nuevo_punto = escalamiento(punto, 2, 0.5)

print(f"Punto original: {punto}")
print(f"Punto escalad: {nuevo_punto}")
