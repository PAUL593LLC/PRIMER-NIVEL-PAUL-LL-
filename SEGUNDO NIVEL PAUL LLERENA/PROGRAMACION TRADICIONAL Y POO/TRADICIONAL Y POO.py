# PROGRAMACION TRADICIONAL
def ingresar_temperaturas():
  temperaturas = []
  for i in range(7):
    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temperaturas.append(temperatura)
  return temperaturas

def calcular_promedio(temperaturas):
  promedio = sum(temperaturas) / len(temperaturas)
  return promedio

# Entrada de datos y cálculo del promedio
temperaturas_semanales = ingresar_temperaturas()
promedio_semanal = calcular_promedio(temperaturas_semanales)

# Mostrar el resultado
print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f}")




# PROGRAMACION ORIENTADA A OBJETOS POO
class Dia:
  def __init__(self, fecha, temperatura):
    self.fecha = fecha
    self.temperatura = temperatura

  def mostrar_datos(self):
    print(f"Fecha: {self.fecha}, Temperatura: {self.temperatura:.2f}")

class Semana:
  def __init__(self):
    self.dias = []

  def agregar_dia(self, dia):
    self.dias.append(dia)

  def calcular_promedio(self):
    promedio = sum(dia.temperatura for dia in self.dias) / len(self.dias)
    return promedio

  def mostrar_semana(self):
    print("## Resumen Semanal del Clima ##")
    for dia in self.dias:
      dia.mostrar_datos()
    promedio_semanal = self.calcular_promedio()
    print(f"Promedio semanal: {promedio_semanal:.2f}")

# Crear objetos Dia y Semana
semana = Semana()
for i in range(7):
  fecha = input("Ingrese la fecha del día (YYYY-MM-DD): ")
  temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
  dia = Dia(fecha, temperatura)
  semana.agregar_dia(dia)

# Mostrar información de la semana
semana.mostrar_semana()


