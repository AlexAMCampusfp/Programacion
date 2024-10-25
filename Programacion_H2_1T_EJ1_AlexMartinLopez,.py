#Ejercicio 1
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


