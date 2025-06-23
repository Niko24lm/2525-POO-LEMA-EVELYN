# sistema_reservas.py

# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # "simple", "doble", "suite"
        self.precio = precio
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero} - {self.tipo.capitalize()} - ${self.precio} - {estado}")

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        self.disponible = True
        print(f"Habitación {self.numero} ahora está disponible.")

# Clase que representa al cliente
class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

# Clase que representa una reserva
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar(self):
        print(f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}.")
        self.habitacion.reservar()

# Clase que representa el hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print(f"Habitaciones disponibles en {self.nombre}:")
        for hab in self.habitaciones:
            if hab.disponible:
                hab.mostrar_info()

# Ejemplo de uso:
if __name__ == "__main__":
    hotel = Hotel("Hotel Paraíso")

    # Crear habitaciones
    hotel.agregar_habitacion(Habitacion(101, "simple", 50))
    hotel.agregar_habitacion(Habitacion(102, "doble", 80))
    hotel.agregar_habitacion(Habitacion(201, "suite", 150))

    hotel.mostrar_habitaciones_disponibles()

    # Crear un cliente y realizar una reserva
    cliente1 = Cliente("Juan Pérez", "12345678")
    habitacion_a_reservar = hotel.habitaciones[1]  # Habitación 102
    reserva1 = Reserva(cliente1, habitacion_a_reservar)
    reserva1.confirmar()

    hotel.mostrar_habitaciones_disponibles()
