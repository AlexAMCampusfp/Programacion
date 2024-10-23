def crear_lista_reproduccion():
    lista_reproduccion = []
    
    print("Ingresa los nombres de las canciones que quieres agregar a tu lista de reproducción.")
    print("Escribe 'fin' para terminar.")
    
    while True:
        cancion = input("Agrega una canción: ")
        if cancion.lower() == 'fin':
            break
        lista_reproduccion.append(cancion)
    
    print("\nLista de reproducción completa:")
    for i, cancion in enumerate(lista_reproduccion):
        print(f"{i + 1}. {cancion}")
    
    while True:
        try:
            indice = int(input("\nSelecciona el índice de la canción que deseas reproducir (0 para salir): "))
            if indice == 0:
                print("Saliendo...")
                break
            if 1 <= indice <= len(lista_reproduccion):
                print(f"Reproduciendo: {lista_reproduccion[indice - 1]}")
            else:
                print("Índice fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    crear_lista_reproduccion()
