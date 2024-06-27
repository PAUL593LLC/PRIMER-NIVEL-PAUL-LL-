def convertir_a_celsius(valor, unidad_origen):
  """
  Convierte un valor de temperatura a Celsius.

  Args:
    valor: El valor a convertir.
    unidad_origen: La unidad de origen del valor (puede ser "C", "F" o "K").

  Returns:
    El valor convertido a Celsius.
  """
  if unidad_origen == "C":
    return valor
  elif unidad_origen == "F":
    return (valor - 32) * 5 / 9
  elif unidad_origen == "K":
    return valor - 273.15
  else:
    raise ValueError("Unidad de origen no válida.")

def convertir_a_fahrenheit(valor, unidad_origen):
  """
  Convierte un valor de temperatura a Fahrenheit.

  Args:
    valor: El valor a convertir.
    unidad_origen: La unidad de origen del valor (puede ser "C", "F" o "K").

  Returns:
    El valor convertido a Fahrenheit.
  """
  if unidad_origen == "C":
    return valor * 9 / 5 + 32
  elif unidad_origen == "F":
    return valor
  elif unidad_origen == "K":
    return (valor - 273.15) * 9 / 5 + 32
  else:
    raise ValueError("Unidad de origen no válida.")

def convertir_a_kelvin(valor, unidad_origen):
  """
  Convierte un valor de temperatura a Kelvin.

  Args:
    valor: El valor a convertir.
    unidad_origen: La unidad de origen del valor (puede ser "C", "F" o "K").

  Returns:
    El valor convertido a Kelvin.
  """
  if unidad_origen == "C":
    return valor + 273.15
  elif unidad_origen == "F":
    return (valor - 32) * 5 / 9 + 273.15
  elif unidad_origen == "K":
    return valor
  else:
    raise ValueError("Unidad de origen no válida.")

# Ejemplo de uso
valor = float(input("Ingrese el valor a convertir: "))
unidad_origen = input("Ingrese la unidad de origen (C, F o K): ").upper()

unidad_destino = input("Ingrese la unidad de destino (C, F o K): ").upper()

if unidad_origen == unidad_destino:
  print("Las unidades de origen y destino son las mismas. No es necesario realizar la conversión.")
else:
  if unidad_destino == "C":
    valor_convertido = convertir_a_celsius(valor, unidad_origen)
  elif unidad_destino == "F":
    valor_convertido = convertir_a_fahrenheit(valor, unidad_origen)
  elif unidad_destino == "K":
    valor_convertido = convertir_a_kelvin(valor, unidad_origen)
  else:
    raise ValueError("Unidad de destino no válida.")

print(f"{valor} {unidad_origen} equivale a {valor_convertido:.2f} {unidad_destino}.")
