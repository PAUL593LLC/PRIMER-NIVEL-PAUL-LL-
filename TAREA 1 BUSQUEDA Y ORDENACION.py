def buscar_valor(lista, valor):
    """ Función que busca un valor específico en una lista bidimensional. """
    filas = len(lista)
    columnas = len(lista[0])

    for p in range(filas):
        for q in range(columnas):
            if lista[p][q] == valor:
                return True, (p, q)

    return False, None

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valor_a_buscar = 5

encontrado, posicion = buscar_valor(lista, valor_a_buscar)

if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la lista")
