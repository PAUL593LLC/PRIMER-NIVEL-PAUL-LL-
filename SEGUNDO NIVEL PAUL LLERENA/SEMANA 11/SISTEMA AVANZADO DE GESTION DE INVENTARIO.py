import pickle

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto {producto.get_nombre()} agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id_producto} actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

# Funciones para guardar y cargar el inventario
def guardar_inventario(inventario, archivo):
    with open(archivo, "wb") as f:
        pickle.dump(inventario.productos, f)
    print(f"Inventario guardado en {archivo}.")

def cargar_inventario(archivo):
    try:
        with open(archivo, "rb") as f:
            productos = pickle.load(f)
            inventario = Inventario()
            for id_producto, info in productos.items():
                producto = Producto(info['id_producto'], info['nombre'], info['cantidad'], info['precio'])
                inventario.agregar_producto(producto)
            print(f"Inventario cargado desde {archivo}.")
            return inventario
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}, creando un nuevo inventario.")
        return Inventario()

# Función para mostrar el menú
def menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar productos")
    print("6. Guardar y salir")

# Función principal
def main():
    inventario = cargar_inventario("inventario.dat")
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad del producto (deje en blanco si no desea cambiar): ")
            precio = input("Ingrese nuevo precio del producto (deje en blanco si no desea cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )
        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            guardar_inventario(inventario, "inventario.dat")
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
