# TAREA-SEMANA-11
ARREGLOS MULTIDIMENSIONALES
def buscar_valor(lista, valor):
  """
  Función que busca un valor específico en una lista bidimensional.
  """

  filas = len(lista)
  columnas = len(lista[0])

  for p in range(filas):
    for q in range(columnas):
      if lista[p][q] == valor:
        return True, (p, q)

  return False, None


lista= [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

valor_a_buscar = 3

encontrado, posicion = buscar_valor(lista, valor_a_buscar)

if encontrado:
  print(f"El valor {3} se encontró en la posición {2}")
else:
  print(f"El valor {3} no se encontró en la lista")
