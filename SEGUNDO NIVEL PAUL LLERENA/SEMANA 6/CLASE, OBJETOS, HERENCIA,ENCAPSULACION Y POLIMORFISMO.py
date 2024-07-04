# Defina una clase base llamada "Vehículo"
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Encapsulación: los atributos son privados y se accede a ellos a través de métodos.
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def descripcion(self):
        return f"{self.__marca} {self.__modelo} ({self.__año})"


# Defina una clase derivada llamada "Vehículo eléctrico" que herede de "Vehículo"
class VehiculoElectrico(Vehiculo):
    def __init__(self, marca, modelo, año, bateria_capacidad):
        super().__init__(marca, modelo, año)  # Llame al constructor de la clase base
        self.__bateria_capacidad = bateria_capacidad

    def get_bateria_capacidad(self):
        return self.__bateria_capacidad

    def descripcion(self):
        # Polimorfismo: anula el método "descripción" de la clase base
        return f"{super().descripcion()} con una batería de {self.__bateria_capacidad} kWh"


# Crear instancias de las clases.
mi_coche = Vehiculo("Toyota", "Corolla", 2015)
mi_coche_electrico = VehiculoElectrico("Tesla", "Modelo 3", 2020, 75)

# Utilice los métodos para demostrar la funcionalidad.
print(mi_coche.descripcion())  # Output: Toyota Corolla (2015)
print(mi_coche_electrico.descripcion())  # Output: Tesla Modelo 3 (2020) con una batería de 75 kWh

# Demostrar polimorfismo llamando al método de "descripción" en una lista de vehículos
vehiculos = [mi_coche, mi_coche_electrico]
for vehiculo in vehiculos:
    print(vehiculo.descripcion())

