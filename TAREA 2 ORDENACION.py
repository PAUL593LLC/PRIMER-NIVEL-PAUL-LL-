# Lista Bidimensional con valores numéricos
# Función con algoritmo de Clasificación de burbujas:

lista = [
    [5, 2, 8],
    [3, 1, 6],
    [9, 4, 7]
]

def ordenar_fila_ascendente(lista, fila):
    lista[fila] = sorted(lista[fila])

# Imprimir la lista original
print("lista original:")
for fila in lista:
    print(fila)

# Ordenar la segunda fila de la lista en orden ascendente
ordenar_fila_ascendente(lista, 1)

# Imprimir la lista con la fila ordenada
print("\nlista con la segunda fila ordenada:")
for fila in lista:
    print(fila)

