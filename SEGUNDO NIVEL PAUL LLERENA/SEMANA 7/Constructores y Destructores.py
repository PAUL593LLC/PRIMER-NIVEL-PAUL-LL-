class Libro:
    def __init__(self, titulo, autor, isbn):
        """
        Constructor: inicializa un objeto Libro con título, autor e ISBN.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __del__(self):
        """
        Destructor: elimina un objeto Libro.
        """
        print(f"Eliminado libro: {self.titulo} de {self.autor}")

    def __str__(self):
        """
        Representación de cadena de un objeto Libro.
        """
        return f"{self.titulo} de {self.autor} (ISBN: {self.isbn})"


class Biblioteca:
    def __init__(self, nombre):
        """
        Constructor: inicializa un objeto Biblioteca con un nombre.
        """
        self.nombre = nombre
        self.libros = []

    def __del__(self):
        """
        Destructor: elimina un objeto Biblioteca y todos sus libros.
        """
        print(f"Eliminada biblioteca: {self.nombre}")
        for libro in self.libros:
            del libro

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.
        """
        self.libros.append(libro)

    def mostrar_libros(self):
        """
        Muestra todos los libros en la biblioteca.
        """
        print(f"Libros en la biblioteca {self.nombre}:")
        for libro in self.libros:
            print(libro)


# Crear algunos libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "978-84-9105-947-6")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-9759-220-3")
libro3 = Libro("1984", "George Orwell", "978-84-9989-094-4")

# Crear una biblioteca y agregar los libros
biblioteca = Biblioteca("Biblioteca Municipal")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Mostrar los libros en la biblioteca
biblioteca.mostrar_libros()

# Eliminar la biblioteca (se llamará al destructor de Biblioteca)
del biblioteca