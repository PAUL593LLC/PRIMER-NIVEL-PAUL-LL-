class Pasajero:
    def __init__(self, nombre, edad, pasaporte):
        self.nombre = nombre
        self.edad = edad
        self.pasaporte = pasaporte

    def __str__(self):
        return f"Pasajero: {self.nombre} (Edad: {self.edad}, Pasaporte: {self.pasaporte})"


class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.capacidad = capacidad
        self.reservaciones = []

    def __str__(self):
        return f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino} el {self.fecha}"

    def hay_disponibilidad(self):
        return len(self.reservaciones) < self.capacidad

    def reservar_asiento(self, pasajero):
        if self.hay_disponibilidad():
            self.reservaciones.append(pasajero)
            print(f"Reserva confirmada para {pasajero.nombre}")
        else:
            print(f"Lo siento, no hay disponibilidad en el vuelo {self.numero_vuelo}")


class SistemaReservas:
    def __init__(self):
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
        print(f"Vuelo {vuelo.numero_vuelo} agregado al sistema de reservas")

    def mostrar_vuelos_disponibles(self):
        print("Vuelos disponibles:")
        for vuelo in self.vuelos:
            if vuelo.hay_disponibilidad():
                print(vuelo)
            else:
                print(f"{vuelo} (¡Vuelo lleno!)")

    def realizar_reserva(self, numero_vuelo, pasajero):
        for vuelo in self.vuelos:
            if vuelo.numero_vuelo == numero_vuelo:
                vuelo.reservar_asiento(pasajero)
                return
        print(f"No se encontró el vuelo con número {numero_vuelo}")


# Ejemplo de uso del sistema de reservas
if __name__ == "__main__":
    # Crear instancia del sistema de reservas
    sistema_reservas = SistemaReservas()

    # Agregar algunos vuelos al sistema
    vuelo1 = Vuelo("BA123", "Londres", "Nueva York", "2024-07-01", 250)
    vuelo2 = Vuelo("AF456", "París", "Tokio", "2024-08-15", 200)
    sistema_reservas.agregar_vuelo(vuelo1)
    sistema_reservas.agregar_vuelo(vuelo2)

    # Mostrar vuelos disponibles
    sistema_reservas.mostrar_vuelos_disponibles()

    # Crear algunos pasajeros
    pasajero1 = Pasajero("Alice", 30, "A12345")
    pasajero2 = Pasajero("Bob", 25, "B67890")

    # Realizar reservas
    sistema_reservas.realizar_reserva("BA123", pasajero1)
    sistema_reservas.realizar_reserva("AF456", pasajero2)
    sistema_reservas.realizar_reserva("BA123", pasajero2)  # Intentar reservar en un vuelo lleno
