class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """Constructor para inicializar un producto con ID, nombre, cantidad y precio."""
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f} €"


class Inventario:
    def __init__(self):
        """Inicializa una lista vacía para almacenar productos."""
        self.productos = []

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario asegurando que el ID sea único."""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe. No se puede añadir el producto.")
        else:
            self.productos.append(producto)
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id):
        """Elimina un producto del inventario por su ID."""
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto por su ID."""
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre (puede haber nombres similares)."""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
