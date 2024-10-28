import numpy as np
import random

def crear_tablero():
    """Crea un tablero de 5x5 lleno de ceros."""
    return np.zeros((5, 5), dtype=int)

def colocar_barco(tablero):
    """Coloca un barco en una posición aleatoria del tablero."""
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)
    tablero[fila, columna] = 1  # Marca la posición del barco con un 1
    return fila, columna  # Devuelve la posición del barco

def mostrar_tablero(tablero, barco_hundido=False):
    """Muestra el estado del tablero."""
    tablero_mostrado = np.copy(tablero)
    if not barco_hundido:
        tablero_mostrado[tablero_mostrado == 1] = 0  # Oculta el barco si no ha sido hundido
    print(tablero_mostrado)

def jugar():
    """Función principal del juego."""
    tablero = crear_tablero()
    fila_barco, columna_barco = colocar_barco(tablero)
    intentos = 0

    print("¡Bienvenido a Hundir la Flota!")
    print("Adivina la posición del barco en el tablero de 5x5.")
    
    while True:
        try:
            fila_adivina = int(input("Introduce la fila (0-4): "))
            columna_adivina = int(input("Introduce la columna (0-4): "))
            intentos += 1
            
            if tablero[fila_adivina, columna_adivina] == 1:
                print("¡Has hundido el barco!")
                mostrar_tablero(tablero, barco_hundido=True)
                print(f"Número total de intentos: {intentos}")
                break
            else:
                print("Agua. Intenta de nuevo.")
                tablero[fila_adivina, columna_adivina] = -1  # Marca la posición atacada
                mostrar_tablero(tablero)
        
        except (ValueError, IndexError):
            print("Entrada inválida. Asegúrate de introducir números entre 0 y 4.")
            
if __name__ == """__main__""":
    jugar()
