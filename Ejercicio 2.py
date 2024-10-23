# Ejercicio 1
palabra = input("Introduce una palabra: ")
palabra_invertida = ""
for i in range(len(palabra) - 1, -1, -1):
    palabra_invertida += palabra[i]
print("La palabra invertida es:", palabra_invertida)
#Ejercicio 2
suma_total = 0
contador = 0
while True:
    numero = int(input("Introduce un número entero (0 para terminar): "))   
    if numero == 0:
        break
    suma_total += numero
    contador += 1
if contador > 0:
    promedio = suma_total / contador
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se han ingresado números.")
#Ejercicio 3
nombres = []
while True:
    nombre = input("Introduce un nombre (escribe 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nombres.append(nombre)
print("\nLista de nombres ingresados:")
print(nombres)
print("\nNombres ingresados uno por uno:")
for nombre in nombres:
    print(nombre)
#Ejercicio 4
contraseña_correcta = "python123"
while True:
    contraseña_ingresada = input("Introduce la contraseña: ")
    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
    else:
        print("Contraseña incorrecta, intenta de nuevo.")
#Ejercicio 5
numeros = []
while True:
    entrada = input("Introduce un número (escribe 'hecho' para terminar): ")
    if entrada.lower() == "hecho":
        break
    try:
        numero = float(entrada) 
        numeros.append(numero)
    except ValueError:
        print("Por favor, introduce un número válido.")
if numeros:
    numero_mayor = numeros[0]  
    for numero in numeros:
        if numero > numero_mayor:
            numero_mayor = numero
    print("El número mayor ingresado es:", numero_mayor)
else:
    print("No se han ingresado números.")



