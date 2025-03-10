from PIL import Image

# Dimensiones de la imagen
width, height = 256, 256

# Crear una nueva imagen en modo RGB
image = Image.new("RGB", (width, height))

# Generar un degradado de colores
for x in range(width):
    for y in range(height):
        r = x  # Rojo varía en el eje x
        g = y  # Verde varía en el eje Y
        b = (x + y) // 2  # Azul es un promedio de X e Y
        image.putpixel((x, y), (r, g, b))
# guardar l aimagen de formato png
image.save("degradado.png")
# mostrar imagen
image.show()
