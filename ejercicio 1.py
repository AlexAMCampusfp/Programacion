#Ejercicio 1
def calcular():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("Introduce la operación (suma, resta, multiplicación, división): ").lower()
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicación":
        resultado = num1 * num2
    elif operacion == "división":
        if num2 == 0:
            return "Error: No se puede dividir entre cero."
        resultado = num1 / num2
    else:
        return "Operación no válida."
    
    return f"El resultado de la {operacion} es: {resultado}"
print(calcular())
#Ejercicio 2
def verificar_par_impar():
    numero = int(input("Introduce un número: "))
    if numero % 2 == 0:
        resultado = "El número es par."
    else:
        resultado = "El número es impar."
    print(resultado)
verificar_par_impar()
#Ejercicio 3
def suma_hasta_n():
       n = int(input("Introduce un número entero positivo: "))
       if n < 1:
        print("Por favor, introduce un número entero positivo.")
        returnsuma = sum(range(1, n + 1))
        print(f"La suma de todos los números desde 1 hasta {n} es: {sum}")
        suma_hasta_n()
#Ejercicio 4
def contar_vocales():
       texto = input("Introduce una cadena de texto: ")
       vocales = "aeiouAEIOU"
       contador = sum(1 for letra in texto if letra in vocales)
       print(f"La cantidad de vocales en la cadena es: {contador}")
       contar_vocales()
#Ejercicio 5
import random
def adivinar_numero(): 
    numero_secreto = random.randint(1, 100)
    intentos = 0 
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:  
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1                
            if adivinanza < 1 or adivinanza > 100:
                print("Por favor, introduce un número entre 1 y 100.")
            elif adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Correcto! Has adivinado el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
adivinar_numero()



            
               