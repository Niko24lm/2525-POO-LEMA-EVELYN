# Este programa calcula el área de un círculo o un rectángulo.
# Permite al usuario elegir la figura y proporciona el resultado.

import math

def calcular_area_circulo(radio_circulo: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio_circulo (float): El radio del círculo.

    Returns:
        float: El área calculada del círculo.
    """
    # Se utiliza math.pi para obtener el valor de PI.
    area_circulo = math.pi * (radio_circulo ** 2)
    return area_circulo

def calcular_area_rectangulo(largo_rectangulo: float, ancho_rectangulo: float) -> float:
    """
    Calcula el área de un rectángulo dadas sus dimensiones de largo y ancho.

    Args:
        largo_rectangulo (float): El largo del rectángulo.
        ancho_rectangulo (float): El ancho del rectángulo.

    Returns:
        float: El área calculada del rectángulo.
    """
    # El área del rectángulo se calcula multiplicando el largo por el ancho.
    area_rectangulo = largo_rectangulo * ancho_rectangulo
    return area_rectangulo

def main():
    """
    Función principal del programa que gestiona la interacción con el usuario
    y llama a las funciones de cálculo de área.
    """
    # Variable booleana para controlar el bucle principal del programa
    continuar_programa = True

    while continuar_programa:
        print("\n--- Calculadora de Área de Figuras ---")
        print("1. Calcular área de un Círculo")
        print("2. Calcular área de un Rectángulo")
        print("3. Salir")

        # Se solicita al usuario que elija una opción (tipo string inicialmente)
        opcion_elegida_str = input("Ingrese el número de la opción deseada: ")

        # Se intenta convertir la opción a un entero
        try:
            opcion_elegida_int = int(opcion_elegida_str)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue # Vuelve al inicio del bucle

        if opcion_elegida_int == 1:
            print("\n--- Cálculo de Área de Círculo ---")
            # Se solicita el radio como string y se convierte a float
            radio_str = input("Ingrese el radio del círculo (ej. 5.5): ")
            try:
                radio_float = float(radio_str)
                # Se verifica que el radio sea un valor positivo (tipo boolean)
                es_radio_valido = radio_float > 0
                if es_radio_valido:
                    resultado_area = calcular_area_circulo(radio_float)
                    # Se muestra el resultado (tipo float)
                    print(f"El área del círculo con radio {radio_float} es: {resultado_area:.2f}")
                else:
                    print("El radio debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida para el radio. Por favor, ingrese un número.")

        elif opcion_elegida_int == 2:
            print("\n--- Cálculo de Área de Rectángulo ---")
            # Se solicitan el largo y el ancho como strings y se convierten a float
            largo_str = input("Ingrese el largo del rectángulo (ej. 10.0): ")
            ancho_str = input("Ingrese el ancho del rectángulo (ej. 4.5): ")
            try:
                largo_float = float(largo_str)
                ancho_float = float(ancho_str)
                # Se verifica que las dimensiones sean positivas
                son_dimensiones_validas = (largo_float > 0) and (ancho_float > 0)
                if son_dimensiones_validas:
                    resultado_area = calcular_area_rectangulo(largo_float, ancho_float)
                    # Se muestra el resultado (tipo float)
                    print(f"El área del rectángulo con largo {largo_float} y ancho {ancho_float} es: {resultado_area:.2f}")
                else:
                    print("El largo y el ancho deben ser números positivos.")
            except ValueError:
                print("Entrada inválida para las dimensiones. Por favor, ingrese números.")

        elif opcion_elegida_int == 3:
            # Se cambia la variable booleana para salir del bucle
            continuar_programa = False
            print("¡Gracias por usar la calculadora de áreas!")

        else:
            # Opción inválida si el número no está en el rango
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()