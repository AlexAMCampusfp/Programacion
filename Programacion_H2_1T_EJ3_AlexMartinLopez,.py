#Ejercicio 3
def main():
    # Pedir el saldo inicial
    while True:
        try:
            saldo = float(input("Introduce el saldo inicial de la cuenta: "))
            if saldo >= 0:
                break
            else:
                print("El saldo no puede ser negativo. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    while True:
        print("\nMenú:")
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar saldo")
        print("4 - Salir")

        # Pedir opción al usuario
        while True:
            try:
                opcion = int(input("Selecciona una opción: "))
                if opcion in [1, 2, 3, 4]: 
                    break
                else:
                    print("Opción no válida. Por favor, selecciona una opción del menú.")
            except ValueError:
                print("Por favor, introduce un número válido.")

        if opcion == 1:  # Ingresar dinero
            while True:
                try:
                    cantidad = float(input("Introduce la cantidad a ingresar: "))
                    if cantidad >= 0:
                        saldo += cantidad
                        print(f"Se han ingresado {cantidad}. Nuevo saldo: {saldo}")
                        break
                    else:
                        print("La cantidad a ingresar no puede ser negativa.")
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif opcion == 2:  # Retirar dinero
            while True:
                try:
                    cantidad = float(input("Introduce la cantidad a retirar: "))
                    if cantidad < 0:
                        print("La cantidad a retirar no puede ser negativa.")
                    elif cantidad > saldo:
                        print("No puedes retirar más de lo que tienes en la cuenta.")
                    else:
                        saldo -= cantidad
                        print(f"Se han retirado {cantidad}. Nuevo saldo: {saldo}")
                        break
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif opcion == 3:  # Mostrar saldo
            print(f"El saldo actual es: {saldo}")

        elif opcion == 4:  # Salir
            print("Saliendo del programa. Adios")
            break
main()
