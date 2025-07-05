# programa_empleados.py

# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre            # Encapsulado: atributo privado
        self.__salario = salario          # Encapsulado: atributo privado

    def mostrar_info(self):
        """Método común que será sobreescrito (polimorfismo)"""
        print(f"Empleado: {self.__nombre}, Salario: ${self.__salario}")

    def get_salario(self):
        """Acceso controlado al salario"""
        return self.__salario

    def set_salario(self, nuevo_salario):
        """Modificador controlado del salario"""
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Error: El salario debe ser mayor que 0.")

# Clase derivada: hereda de Empleado
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    # Polimorfismo: sobreescribimos mostrar_info
    def mostrar_info(self):
        print(f"Desarrollador especializado en {self.lenguaje}.")
        super().mostrar_info()

# Otra clase derivada: hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        print(f"Gerente del departamento de {self.departamento}.")
        super().mostrar_info()


# ------------------------
# Código principal (test)
# ------------------------

if __name__ == "__main__":
    # Crear instancias
    empleado1 = Empleado("Carlos", 3000)
    dev1 = Desarrollador("Ana", 4000, "Python")
    gerente1 = Gerente("Laura", 6000, "Ventas")

    # Mostrar información (Polimorfismo en acción)
    empleado1.mostrar_info()
    dev1.mostrar_info()
    gerente1.mostrar_info()

    # Encapsulación en acción
    print(f"Salario actual de Ana: ${dev1.get_salario()}")
    dev1.set_salario(4500)
    print(f"Nuevo salario de Ana: ${dev1.get_salario()}")
