#Ejercicio 1
def crear_lista_reproduccion():
    lista_reproduccion = []
    
    print("Ingrese los nombres de las canciones que desea agregar a su lista de reproducción.")
    print("Escriba 'fin' para terminar.")
    
    while True:
        cancion = input("Agregar canción: ")
        if cancion.lower() == 'fin':
            break
        lista_reproduccion.append(cancion)

    print("\nLista de reproducción completa:")
    for i, cancion in enumerate(lista_reproduccion):
        print(f"{i + 1}. {cancion}")
    
    while True:
        try:
            indice = int(input("\nSeleccione el número de la canción que desea reproducir (0 para salir): "))
            if indice == 0:
                print("Saliendo del programa.")
                break
            if 1 <= indice <= len(lista_reproduccion):
                print(f"Reproduciendo: {lista_reproduccion[indice - 1]}")
            else:
                print("Índice fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    crear_lista_reproduccion()

#Ejercicio 2
def agenda_contactos():
    contactos = {}

    print("Ingrese los contactos (nombre y número de teléfono).")
    print("Escriba 'fin' como nombre para terminar.")

    while True:
        nombre = input("Nombre: ")
        if nombre.lower() == 'fin':
            break
        numero = input("Número de teléfono: ")
        contactos[nombre] = numero

    print("\nContactos almacenados:")
    for nombre, numero in contactos.items():
        print(f"{nombre}: {numero}")

    while True:
        busqueda = input("\nIngrese el nombre del contacto que desea buscar (o 'fin' para salir): ")
        if busqueda.lower() == 'fin':
            print("Saliendo del programa.")
            break
        elif busqueda in contactos:
            print(f"Número de teléfono de {busqueda}: {contactos[busqueda]}")
        else:
            print("Contacto no encontrado.")

if __name__ == "__main__":
    agenda_contactos()
#Ejercicio 3
def itinerario_viaje():
    ciudades = ("Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao")
    print("Itinerario de viaje:")
    for i, ciudad in enumerate(ciudades, start=1):
        print(f"{i}. {ciudad}")
    while True:
        try:
            posicion = int(input("\nIngrese el número de la ciudad que desea consultar (0 para salir): "))
            if posicion == 0:
                print("Saliendo del programa.")
                break
            if 1 <= posicion <= len(ciudades):
                print(f"Ciudad en la posición {posicion}: {ciudades[posicion - 1]}")
            else:
                print("Posición fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
if __name__ == "__main__":
    itinerario_viaje()
#Ejercicio 4
def registrar_calificaciones():
    calificaciones = {}
    print("Ingrese las asignaturas y sus calificaciones.")
    print("Escriba 'fin' como asignatura para terminar.")
    while True:
        asignatura = input("Asignatura: ")
        if asignatura.lower() == 'fin':
            break
        try:
            calificacion = float(input("Calificación: "))
            calificaciones[asignatura] = calificacion
        except ValueError:
            print("Por favor, ingrese una calificación válida.")
    print("\nResumen de calificaciones:")
    for asignatura, calificacion in calificaciones.items():
        print(f"{asignatura}: {calificacion}")
    if calificaciones:
        media = sum(calificaciones.values()) / len(calificaciones)
        print(f"\nCalificación media: {media:.2f}")
    else:
        print("No se han ingresado calificaciones.")
if __name__ == "__main__":
    registrar_calificaciones()
#Ejercicio 5
def menu_cafeteria():
    menu = {
        "Café": (2.50, 5),
        "Té": (2.00, 3),
        "Pastel": (3.00, 250),
        "Sándwich": (4.50, 300),
        "Ensalada": (5.00, 150),
        "Galleta": (1.50, 100)
    }
    print("Menú de la cafetería:")
    for producto, (precio, calorias) in menu.items():
        print(f"{producto}: ${precio:.2f} - {calorias} calorías")
    pedido = []
    total_pago = 0
    total_calorias = 0
    while True:
        producto = input("\nIngrese el nombre del producto que desea pedir (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        elif producto in menu:
            precio, calorias = menu[producto]
            pedido.append(producto)
            total_pago += precio
            total_calorias += calorias
            print(f"Añadido: {producto} - Precio: ${precio:.2f}, Calorías: {calorias}")
        else:
            print("Producto no encontrado en el menú. Intente de nuevo.")
    print("\nResumen de su pedido:")
    for item in pedido:
        print(f"- {item}")
    print(f"\nTotal a pagar: ${total_pago:.2f}")
    print(f"Calorías totales: {total_calorias} kcal")
if __name__ == "__main__":
    menu_cafeteria()
