import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'PARCIAL 01/SEMANA 2/2.1 Tarea.py',
        '2': 'PARCIAL 01/SEMANA 3/POO.py/Programación Tradicional.py',
        '3': 'PARCIAL 01/SEMANA 4/EjemplosMundoReal_POO.py',
        '4': 'PARCIAL 01/SEMANA 5/Tipos de datos e Identificadores.py',
        '5': 'PARCIAL 01/SEMANA 6/Aplicación de Conceptos de POO en Python.py',
        '6': 'PARCIAL 01/SEMANA 7/Implementación de Constructores y Destructores en Python.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()

    import threading
    import time


    # Función que simula una tarea para un hilo
    def tarea_hilo(identificador, delay):
        for i in range(5):
            print(f'Hilo {identificador}: Realizando tarea {i}')
            time.sleep(delay)


    # Crear instancias de hilos
    hilo1 = threading.Thread(target=tarea_hilo, args=(1, 1))
    hilo2 = threading.Thread(target=tarea_hilo, args=(2, 0.8))
    hilo3 = threading.Thread(target=tarea_hilo, args=(3, 1.2))

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()
    hilo3.start()

    # Esperar a que todos los hilos terminen
    hilo1.join()
    hilo2.join()
    hilo3.join()

    print('Programa principal: Todas las tareas han sido completadas.')



