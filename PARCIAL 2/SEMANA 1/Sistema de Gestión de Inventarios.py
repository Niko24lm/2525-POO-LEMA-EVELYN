# Clase Producto
# Esta clase representa cada producto que tenemos en el inventario.
# Decidí ponerle atributos básicos: ID, nombre, cantidad y precio
# porque son los datos esenciales para poder administrarlos en la tienda.

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto
        Aquí inicializamos los atributos de cada producto.
        :param id_producto: Identificador único del producto (no puede repetirse)
        :param nombre: Nombre del producto (ejemplo: "Coca-Cola")
        :param cantidad: Número de unidades disponibles en el inventario
        :param precio: Precio unitario del producto
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # === Getters (para obtener valores de los atributos) ===
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # === Setters (para modificar los atributos después de crearlos) ===
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        """
        Este método lo usé para que cuando imprimamos un objeto Producto
        se muestre en un formato entendible en lugar de la dirección de memoria.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# ===========================
# Bloque de prueba (solo para verificar que funciona)
# ===========================
if __name__ == "__main__":
    # Creamos un producto de prueba
    producto1 = Producto(1, "Coca-Cola", 50, 1.50)
    print(producto1)

    # Modificamos atributos usando setters
    producto1.set_precio(15.00)
    producto1.set_cantidad(50)

    # Imprimimos otra vez para ver los cambios
    print("Después de actualizar:")
    print(producto1)
