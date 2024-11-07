def menu():
    while True:
        print("\n--- Menú de Categorías ---")
        print("1. Crear categoría")
        print("2. Leer categorías")
        print("3. Actualizar categoría")
        print("4. Eliminar categoría")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("Has elejido la opcion de crear una categoria")
        elif opcion == '2':
            print("Has elejido la opcion de leer categorias")
        elif opcion == '3':
            print("Has elejido la opcion de actualizar categorias")
        elif opcion == '4':
            print("Has elejido la opcion de eliminar categoria")
        elif opcion == '5':
            print("Has elejido la opcion de salir.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()


