"""
# ABRIMOS EL ARCIVO
# Lee el contenido del archivo línea por línea utilizando el método adecuado.
# Muestra en la consola cada línea leída.
file = open("my_notes.txt", "r")
print(file)

lineas = file.readlines()
print(lineas)
file.close()  # CERRAR EL ARCHIVO
"""
"""
# Abrimos el archivo en modo lectura utilizando 'with' para asegurarnos de que se cierre correctamente después de su uso
# Leemos todas las líneas del archivo y las almacenamos en la lista 'lineas'
# Imprimimos las líneas del archivo
# Utiliza métodos como write() y readline() para manipular el archivo de texto.
# Agrega comentarios explicativos en tu código.
with open("my_notes2.txt", "w") as archivo:
    archivo.write("ALEXANDER, JHOAN, DALADIER.\n")
    archivo.write("MI FAMILIA.\n")
    archivo.write("SIEMPRE BENDECIDO.\n")
with open("my_notes2.txt", "r") as archivo:
        print(archivo.readlines())
print("Se han escrito líneas en el archivo 'my_notes2.txt'.")
"""



# Abrimos el archivo en modo lectura y lo asignamos a la variable 'file'
file = open("my_notes2.txt", "r")
print(file)

# Utilizamos 'with' para abrir el archivo en modo lectura y leer todas las líneas
with open("my_notes2.txt", "r") as archivo:
    lineas = archivo.readlines()
    # Iteramos sobre cada línea y eliminamos el salto de línea antes de imprimir
    for l in lineas:
        print(l.replace("\n", ""))







