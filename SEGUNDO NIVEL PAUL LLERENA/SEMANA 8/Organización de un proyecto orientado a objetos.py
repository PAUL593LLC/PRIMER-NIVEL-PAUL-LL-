import os


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo de script.

    Args:
        ruta_script (str): Ruta al archivo de script.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def agregar_script(opciones):
    """
    Agrega un nuevo script al menú de opciones.

    Args:
        opciones (dict): Diccionario de opciones del menú.
    """
    nombre_script = input("Introduce el nombre descriptivo del script: ")
    ruta_script = input("Introduce la ruta relativa al script: ")
    key = str(len(opciones) + 1)
    opciones[key] = ruta_script
    print(f"Script '{nombre_script}' agregado con la opción {key}.")


def mostrar_menu():
    """
    Muestra el menú principal del Dashboard y maneja la interacción del usuario.
    """
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Puedes agregar más scripts aquí
    }

    while True:
        print("\nMenu Principal - Dashboard")
        print("1 - Unidad 1/1.2. Técnicas de Programación/1.2-1. Ejemplo Técnicas de Programación.py")
        print("A - Agregar un nuevo script al menú")
        print("0 - Salir")

        eleccion = input("Elige una opción para ver su código, agregar un script o '0' para salir: ").strip()
        if eleccion == '0':
            break
        elif eleccion == 'A':
            agregar_script(opciones)
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
