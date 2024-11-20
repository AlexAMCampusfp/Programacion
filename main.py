from pedido import registrar_cliente, realizar_compra, mostrar_productos

def menu():
    while True:
        #Menu principal
        print("\nMenú:")
        print("1. Registrar Cliente")
        print("2. Realizar Compra")
        print("3. Mostrar productos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
#Dependiendo de que opcion elija el usuario pasara una cosa diferente y si no selecciona ninguna de las opciones disponibles le saldra que esa opcion es incorrecta
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            realizar_compra()
        elif opcion == '3':
            mostrar_productos()
        elif opcion == '4':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
