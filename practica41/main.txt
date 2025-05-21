def mostrar_historia():
    print("\n--- Historia de la Animación por Computadora ---")
    print("* Década de 1960: Inicios con Ivan Sutherland y el programa Sketchpad.")
    print("* 1982: 'Tron' de Disney usa secuencias generadas por computadora.")
    print("* 1995: Pixar lanza 'Toy Story', el primer largometraje 100% animado digitalmente.\n")

def mostrar_evolucion():
    print("\n--- Evolución Tecnológica ---")
    print("* 1980-1990: Nace el CGI, mejora el modelado 3D y el renderizado.")
    print("* 2000-2010: Realismo con captura de movimiento, sombras y simulaciones físicas.")
    print("* 2010 en adelante: Se integran IA, realidad aumentada y motores como Unity o Unreal Engine.\n")

def mostrar_aplicaciones():
    print("\n--- Aplicaciones de la Animación por Computadora ---")
    print("* Cine y TV: Personajes virtuales, efectos visuales.")
    print("* Videojuegos: Modelado, cinemáticas, interacción.")
    print("* Medicina: Simulación quirúrgica, visualización de órganos.")
    print("* Arquitectura: Recorridos virtuales, modelos 3D.")
    print("* Educación: Recursos animados y e-learning.\n")

def menu():
    while True:
        print("=== Animación por Computadora ===")
        print("1. Historia")
        print("2. Evolución")
        print("3. Aplicaciones")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_historia()
        elif opcion == '2':
            mostrar_evolucion()
        elif opcion == '3':
            mostrar_aplicaciones()
        elif opcion == '4':
            print("Gracias por explorar la animación por computadora.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__== "__main__":
    menu()
