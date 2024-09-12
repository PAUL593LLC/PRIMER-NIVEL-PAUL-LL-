import threading
import time


def tarea(barrera, nombre_hilo):
    """
    Simula una tarea que toma tiempo y requiere acceso exclusivo a una sección crítica.

    :param barrera: Barrera que sincroniza el acceso a la sección crítica.
    :param nombre_hilo: Nombre del hilo que ejecuta la tarea.
    """
    # Sección crítica: solo un hilo puede ejecutar este código a la vez
    print(f"Soy el hilo {nombre_hilo}")
    # Simulación de una tarea que toma tiempo
    time.sleep(2)
    print(f"Hilo {nombre_hilo} terminado")
    barrera.wait()  # Esperar a que todos los hilos hayan terminado


def main():
    # Crear una barrera para sincronizar el acceso a la sección crítica
    barrera = threading.Barrier(5)  # 5 hilos

    # Crear y iniciar varios hilos que ejecutan la tarea
    hilos = []
    for i in range(5):
        nombre_hilo = f"Hilo {i + 1}"
        hilo = threading.Thread(target=tarea, args=(barrera, nombre_hilo))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()


if __name__ == "__main__":
    main()
print("Programa terminado")
