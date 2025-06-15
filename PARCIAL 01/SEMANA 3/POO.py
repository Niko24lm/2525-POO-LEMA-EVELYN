# --- Programación Orientada a Objetos (POO) para el Cálculo del Promedio Semanal del Clima ---

class DiaClima:
    """
    Representa la información del clima para un día específico.
    Encapsula el día de la semana y su temperatura.
    """
    def __init__(self, nombre_dia):
        """
        Inicializa un objeto DiaClima.

        Args:
            nombre_dia (str): El nombre del día de la semana (ej. "Lunes").
        """
        self._nombre_dia = nombre_dia  # Atributo protegido para el nombre del día
        self._temperatura = None      # Atributo protegido para la temperatura

    def get_nombre_dia(self):
        """
        Obtiene el nombre del día.
        """
        return self._nombre_dia

    def set_temperatura(self, temperatura):
        """
        Establece la temperatura para el día.

        Args:
            temperatura (float): La temperatura a establecer.
        """
        self._temperatura = temperatura

    def get_temperatura(self):
        """
        Obtiene la temperatura del día.
        """
        return self._temperatura

class ClimaSemanal:
    """
    Gestiona la información del clima para toda la semana.
    Utiliza objetos DiaClima para almacenar las temperaturas diarias.
    """
    def __init__(self):
        """
        Inicializa un objeto ClimaSemanal creando los objetos DiaClima para cada día.
        """
        self._dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self._informacion_clima_diaria = [DiaClima(dia) for dia in self._dias]

    def ingresar_temperaturas_diarias(self):
        """
        Solicita al usuario las temperaturas para cada día de la semana.
        """
        print("--- Cálculo del Promedio Semanal del Clima (Programación Orientada a Objetos) ---")
        for dia_obj in self._informacion_clima_diaria:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el {dia_obj.get_nombre_dia()} (en °C): "))
                    dia_obj.set_temperatura(temp)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para la temperatura.")

    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de las temperaturas semanales.

        Returns:
            float: El promedio de las temperaturas semanales.
        """
        temperaturas = [dia_obj.get_temperatura() for dia_obj in self._informacion_clima_diaria]
        if not temperaturas:
            return 0.0
        return sum(temperaturas) / len(temperaturas)

    def mostrar_temperaturas(self):
        """
        Muestra las temperaturas registradas para cada día.
        """
        print("\nTemperaturas registradas para la semana:")
        for dia_obj in self._informacion_clima_diaria:
            print(f"- {dia_obj.get_nombre_dia()}: {dia_obj.get_temperatura():.2f} °C")

def main_poo():
    """
    Función principal para la ejecución del programa POO.
    Crea una instancia de ClimaSemanal, ingresa datos y calcula el promedio.
    """
    clima_semanal = ClimaSemanal()
    clima_semanal.ingresar_temperaturas_diarias()
    promedio = clima_semanal.calcular_promedio_semanal()
    clima_semanal.mostrar_temperaturas()
    print(f"El promedio semanal del clima es: {promedio:.2f} °C")

if __name__ == "__main__":
    main_poo()