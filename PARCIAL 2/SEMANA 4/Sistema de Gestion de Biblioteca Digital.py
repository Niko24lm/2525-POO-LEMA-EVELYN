from typing import Tuple, List, Dict, Set

class Libro:
    """
    Representa un libro con título, autor, categoría e ISBN.
    El título y autor se almacenan en una tupla inmutable.
    """
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._info: Tuple[str, str] = (titulo, autor)  # Tupla inmutable (titulo, autor)
        self.categoria: str = categoria
        self.isbn: str = isbn

    @property
    def titulo(self) -> str:
        return self._info[0]

    @property
    def autor(self) -> str:
        return self._info[1]

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    """
    Representa un usuario con nombre, ID único y lista de libros prestados.
    """
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[Libro] = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

class Biblioteca:
    """
    Gestiona libros, usuarios y préstamos.
    """
    def __init__(self):
        self.libros: Dict[str, Libro] = {}  # ISBN -> Libro
        self.usuarios: Dict[str, Usuario] = {}  # ID usuario -> Usuario
        self.ids_usuarios: Set[str] = set()  # Conjunto para IDs únicos

    # Añadir un libro a la biblioteca
    def añadir_libro(self, libro: Libro) -> bool:
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
            return False
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro}")
        return True

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn: str) -> bool:
        if isbn not in self.libros:
            print(f"No existe un libro con ISBN {isbn} en la biblioteca.")
            return False
        # Verificar que el libro no esté prestado a ningún usuario
        for usuario in self.usuarios.values():
            if any(libro.isbn == isbn for libro in usuario.libros_prestados):
                print(f"No se puede eliminar el libro con ISBN {isbn} porque está prestado.")
                return False
        libro = self.libros.pop(isbn)
        print(f"Libro eliminado: {libro}")
        return True

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")
            return False
        self.usuarios[usuario.id_usuario] = usuario
        self.ids_usuarios.add(usuario.id_usuario)
        print(f"Usuario registrado: {usuario}")
        return True

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario: str) -> bool:
        if id_usuario not in self.ids_usuarios:
            print(f"No existe un usuario con ID {id_usuario}.")
            return False
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"No se puede dar de baja al usuario {id_usuario} porque tiene libros prestados.")
            return False
        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario dado de baja: {usuario}")
        return True

    # Prestar un libro a un usuario
    def prestar_libro(self, isbn: str, id_usuario: str) -> bool:
        if isbn not in self.libros:
            print(f"No existe un libro con ISBN {isbn}.")
            return False
        if id_usuario not in self.ids_usuarios:
            print(f"No existe un usuario con ID {id_usuario}.")
            return False
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        # Verificar que el libro no esté ya prestado a alguien
        for u in self.usuarios.values():
            if any(lib.isbn == isbn for lib in u.libros_prestados):
                print(f"El libro '{libro.titulo}' ya está prestado a otro usuario.")
                return False
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        return True

    # Devolver un libro de un usuario
    def devolver_libro(self, isbn: str, id_usuario: str) -> bool:
        if id_usuario not in self.ids_usuarios:
            print(f"No existe un usuario con ID {id_usuario}.")
            return False
        usuario = self.usuarios[id_usuario]
        for i, libro in enumerate(usuario.libros_prestados):
            if libro.isbn == isbn:
                usuario.libros_prestados.pop(i)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return True
        print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")
        return False

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, titulo: str = None, autor: str = None, categoria: str = None) -> List[Libro]:
        resultados = []
        for libro in self.libros.values():
            if titulo and titulo.lower() not in libro.titulo.lower():
                continue
            if autor and autor.lower() not in libro.autor.lower():
                continue
            if categoria and categoria.lower() != libro.categoria.lower():
                continue
            resultados.append(libro)
        return resultados

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario: str) -> List[Libro]:
        if id_usuario not in self.ids_usuarios:
            print(f"No existe un usuario con ID {id_usuario}.")
            return []
        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados

# --- Pruebas del sistema ---

if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "978-0-14-312970-6")
    libro3 = Libro("1984", "George Orwell", "Distopía", "978-0-452-28423-4")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Eliana Ramirez", "U001")
    usuario2 = Usuario("Hugo lopez", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("978-3-16-148410-0", "U001")  # Cien Años de Soledad a Ana
    biblioteca.prestar_libro("978-0-14-312970-6", "U002")  # El Principito a Luis

    # Intentar prestar un libro ya prestado
    biblioteca.prestar_libro("978-3-16-148410-0", "U002")  # Debe fallar

    # Listar libros prestados a Ana
    print("\nLibros prestados a Ana:")
    for libro in biblioteca.listar_libros_prestados("U001"):
        print(libro)

    # Devolver libro
    biblioteca.devolver_libro("978-3-16-148410-0", "U001")

    # Buscar libros por autor
    print("\nBuscar libros por autor 'George Orwell':")
    resultados = biblioteca.buscar_libros(autor="George Orwell")
    for libro in resultados:
        print(libro)

    # Quitar libro (que no está prestado)
    biblioteca.quitar_libro("978-3-16-148410-0")

    # Dar de baja usuario sin libros prestados
    biblioteca.dar_baja_usuario("U001")

    # Intentar dar de baja usuario con libro prestado
    biblioteca.dar_baja_usuario("U002")  # Luis tiene un libro prestado, debe fallar
