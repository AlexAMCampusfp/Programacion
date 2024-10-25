#Ejercicio 2
#Piedra papel o tijera
import random

def obtener_opcion_usuario():
    while True:
        print("Seleccione una opción:")
        print("1 - Piedra")
        print("2 - Papel")
        print("3 - Tijera")
        
        opcion = input("Ingrese su opción (1, 2 o 3): ")
        
        if opcion in ['1', '2', '3']:
            return int(opcion)
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def determinar_ganador(usuario, maquina):
    if usuario == maquina:
        return "Empate"
    elif (usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2):
        return "Ganaste"
    else:
        return "Perdiste"

# Opciones de la máquina
opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

# Obtener opción del usuario
opcion_usuario = obtener_opcion_usuario()

# Generar opción de la máquina
opcion_maquina = random.randint(1, 3)

# Mostrar resultados
print(f"\nTu opción: {opciones[opcion_usuario]}")
print(f"Opción de la máquina: {opciones[opcion_maquina]}")
resultado = determinar_ganador(opcion_usuario, opcion_maquina)
print(f"Resultado: {resultado}")