import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y setters
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        # Diccionario con clave = id_producto, valor = objeto Producto
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            raise KeyError(f"El producto con ID {producto.id} ya existe.")
        self.productos[producto.id] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            raise KeyError(f"No existe producto con ID {id_producto}.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
        else:
            raise KeyError(f"No existe producto con ID {id_producto}.")

    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].precio = nuevo_precio
        else:
            raise KeyError(f"No existe producto con ID {id_producto}.")

    def buscar_por_nombre(self, nombre):
        # Búsqueda insensible a mayúsculas
        nombre = nombre.lower()
        resultados = [p for p in self.productos.values() if nombre in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            # Serializamos la lista de productos como diccionarios
            lista_productos = [p.to_dict() for p in self.productos.values()]
            json.dump(lista_productos, f, indent=4, ensure_ascii=False)

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                lista_productos = json.load(f)
                self.productos = {}
                for p_data in lista_productos:
                    producto = Producto.from_dict(p_data)
                    self.productos[producto.id] = producto
        except FileNotFoundError:
            # Si no existe el archivo, iniciamos con inventario vacío
            self.productos = {}

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- Sistema Avanzado de Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad de producto")
        print("4. Actualizar precio de producto")
        print("5. Buscar productos por nombre")
        print("6. Mostrar todos los productos")
        print("7. Guardar inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("Ingrese ID único del producto: ").strip()
                if id_producto == "":
                    print("El ID no puede estar vacío.")
                    continue
                nombre = input("Ingrese nombre del producto: ").strip()
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)
                print("Producto añadido exitosamente.")

            elif opcion == "2":
                id_producto = input("Ingrese ID del producto a eliminar: ").strip()
                inventario.eliminar_producto(id_producto)
                print("Producto eliminado exitosamente.")

            elif opcion == "3":
                id_producto = input("Ingrese ID del producto a actualizar cantidad: ").strip()
                nueva_cantidad = int(input("Ingrese nueva cantidad: "))
                inventario.actualizar_cantidad(id_producto, nueva_cantidad)
                print("Cantidad actualizada exitosamente.")

            elif opcion == "4":
                id_producto = input("Ingrese ID del producto a actualizar precio: ").strip()
                nuevo_precio = float(input("Ingrese nuevo precio: "))
                inventario.actualizar_precio(id_producto, nuevo_precio)
                print("Precio actualizado exitosamente.")

            elif opcion == "5":
                nombre = input("Ingrese nombre o parte del nombre para buscar: ").strip()
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    print(f"Se encontraron {len(resultados)} producto(s):")
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron productos con ese nombre.")

            elif opcion == "6":
                inventario.mostrar_todos()

            elif opcion == "7":
                inventario.guardar_en_archivo("inventario.json")
                print("Inventario guardado en 'inventario.json'.")

            elif opcion == "8":
                inventario.guardar_en_archivo("inventario.json")
                print("Inventario guardado. Saliendo...")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except KeyError as ke:
            print(f"Error: {ke}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    menu()