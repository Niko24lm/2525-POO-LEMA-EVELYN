# --- Programación Tradicional para el Cálculo del Promedio Semanal del Clima ---

def obtener_temperatura_diaria(dia):
    """
    Solicita al usuario la temperatura para un día específico y la valida.

    Args:
        dia (str): El nombre del día de la semana.

    Returns:
        float: La temperatura ingresada por el usuario.
    """
    while True:
        try:
            temp = float(input(f"Ingrese la temperatura para el {dia} (en °C): "))
            return temp
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para la temperatura.")

def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.

    Args:
        temperaturas (list): Una lista de temperaturas diarias.

    Returns:
        float: El promedio de las temperaturas.
    """
    if not temperaturas:
        return 0.0  # Evitar división por cero si la lista está vacía
    return sum(temperaturas) / len(temperaturas)

def main_tradicional():
    """
    Función principal para la ejecución del programa tradicional.
    Recopila temperaturas diarias y calcula el promedio semanal.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas_semanales = []

    print("--- Cálculo del Promedio Semanal del Clima (Programación Tradicional) ---")

    for dia in dias_semana:
        temp_dia = obtener_temperatura_diaria(dia)
        temperaturas_semanales.append(temp_dia)

    promedio = calcular_promedio_semanal(temperaturas_semanales)
    print(f"\nLas temperaturas registradas para la semana son: {temperaturas_semanales}")
    print(f"El promedio semanal del clima es: {promedio:.2f} °C")

if __name__ == "__main__":
    main_tradicional()