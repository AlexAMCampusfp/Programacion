#Funcion para el cuadrado
def mostrar_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    print(f"Cuadrado:\nLado: {lado}\nÁrea: {area}\nPerímetro: {perimetro}") 
#Funcion para el rectangulo
def mostrar_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Rectángulo:\nBase: {base}\nAltura: {altura}\nÁrea: {area}\nPerímetro: {perimetro}")

while True:
    print("Que figura quieres mostrar:")
    print("1 - Cuadrado")
    print("2 - Rectángulo")
    
    opcion = input("Ingrese su opción (1 o 2): ") #Depende de la opcion que elija se mostrara o el cuadrado o el rectaangulo
    
    if opcion == '1':
        lado = float(input("Ingrese el lado del cuadrado: "))
        mostrar_cuadrado(lado)
        print("**")
        print("**")
        break
    elif opcion == '2':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        mostrar_rectangulo(base, altura)
        print("***")
        print("***")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.") #En el caso de q no sea ni uno ni dos saldra que esa opcion es incorrecta
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

def main():
    # Solicitar saldo inicial
    while True:
        try:
            saldo = float(input("Introduce el saldo inicial de la cuenta: "))
            if saldo < 0:
                print("El saldo no puede ser menor que 0. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

    while True:
        print("\nMenú:")
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar saldo")
        print("4 - Salir")

        # Solicitar opción del menú
        while True:
            try:
                opcion = int(input("Selecciona una opción: "))
                if opcion not in [1, 2, 3, 4]:
                    print("Opción no válida. Por favor, selecciona de nuevo.")
                else:
                    break
            except ValueError:
                print("Por favor, introduce un número válido.")

        if opcion == 1:  # Ingresar dinero
            while True:
                try:
                    cantidad = float(input("Introduce la cantidad a ingresar: "))
                    if cantidad < 0:
                        print("No se pueden ingresar cantidades negativas. Inténtalo de nuevo.")
                    else:
                        saldo += cantidad
                        print(f"Se han ingresado {cantidad}. Nuevo saldo: {saldo:.2f}")
                        break
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif opcion == 2:  # Retirar dinero
            while True:
                try:
                    cantidad = float(input("Introduce la cantidad a retirar: "))
                    if cantidad < 0:
                        print("No se pueden retirar cantidades negativas. Inténtalo de nuevo.")
                    elif cantidad > saldo:
                        print("No se puede retirar más de lo que hay en la cuenta.")
                    else:
                        saldo -= cantidad
                        print(f"Se han retirado {cantidad}. Nuevo saldo: {saldo:.2f}")
                        break
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif opcion == 3:  # Mostrar saldo
            print(f"El saldo actual es: {saldo:.2f}")

        elif opcion == 4:  # Salir
            print("Gracias por usar el sistema bancario. Adios")
            break

if __name__ == "__main__":
    main()
