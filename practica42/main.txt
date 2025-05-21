import tkinter as tk
from tkinter import messagebox

def mostrar_historia():
    mensaje = (
        "* Década de 1960: Inicios con Ivan Sutherland y el programa Sketchpad.\n"
        "* 1970s: Ford de Disney introduce secuencias CGI.\n"
        "* 1995: 'Toy Story' de Pixar es el primer largometraje animado completamente por computadora."
    )
    messagebox.showinfo("Historia", mensaje)

def mostrar_evolucion():
    mensaje = (
        "* 1980/1990: Nace el CGI, mejora el modelado 3D y el renderizado.\n"
        "* 2000-2010: Realismo con captura de movimiento, sombras y simulaciones físicas.\n"
        "* 2010 en adelante: Uso de inteligencia artificial y realidad virtual."
    )
    messagebox.showinfo("Evolución", mensaje)

def mostrar_aplicaciones():
    mensaje = (
        "* Cine y TV: Efectos especiales, personajes virtuales.\n"
        "* Videojuegos: Modelado 3D, cinemáticas, mundos interactivos.\n"
        "* Medicina: Visualización de órganos, simulaciones quirúrgicas.\n"
        "* Arquitectura: Recorridos virtuales, simulaciones estructurales.\n"
        "* Educación: Videos explicativos, e-learning, animaciones didácticas."
    )
    messagebox.showinfo("Aplicaciones", mensaje)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Animación por Computadora")
ventana.geometry("400x300")
ventana.config(bg="#f0f0f0")

# Título
titulo = tk.Label(ventana, text="Animación por Computadora", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

# Botones
btn_historia = tk.Button(ventana, text="Historia", command=mostrar_historia, width=30)
btn_historia.pack(pady=5)

btn_evolucion = tk.Button(ventana, text="Evolución", command=mostrar_evolucion, width=30)
btn_evolucion.pack(pady=5)

btn_aplicaciones = tk.Button(ventana, text="Aplicaciones", command=mostrar_aplicaciones, width=30)
btn_aplicaciones.pack(pady=5)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, width=30, fg="white", bg="red")
btn_salir.pack(pady=20)

ventana.mainloop()
