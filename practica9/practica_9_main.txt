import cairo

# Dimensiones de la imagen SVG
width, height = 400, 300

# Crear un archivo SVG
with cairo.SVGSurface("imagen_vectorial.svg", width, height) as surface:
    ctx = cairo.Context(surface)

    # Fondo blanco
    ctx.set_source_rgb(1, 1, 1)  # RGB (Blanco)
    ctx.paint()

    # Dibujar un rectangulo (rojo)
    ctx.set_source_rgb(1, 0, 0)  # RGB (rojo)
    ctx.rectangle(50, 50, 100, 80)  # (x, y, ancho, alto)
    ctx.fill()

    # Dibujar una linea (Azul)
    ctx.set_source_rgb(0, 1, 0)  # RGB (azul)
    ctx.arc(200, 100, 40, 0, 2 * 3.1416)  # (x,y, radio, inicio, fin)
    ctx.fill()

    # Dibujar una linea (verde)
    ctx.set_source_rgb(0, 1, 0)  # RGB (verde)
    ctx.set_line_width(5)
    ctx.move_to(50, 200)  # Punto de inicio (x, y)
    ctx.line_to(350, 200)  # Punto Final (x,y)
    ctx.stroke()

    print("imagen vectorial guardada como 'imagen_vectorial.svg'")
