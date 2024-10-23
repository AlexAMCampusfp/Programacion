#Funciones Pyhton
def saludar():
    print("Hola")

#Codigo principal
saludar()


#Vamos a hacer una serie de funciones

def suma():
    suma = 2+3
    print(f"La suma es {suma}")

def resta():
    resta=3-2
    print(resta)

def multiplicacion():
    multiplicacion=3*2
    print(multiplicacion)

def dividir():
    dividir=4/2
    print(dividir)

#Los parametros son variables que la funcion puede utilizar

def sumapro(numero1, numero2):
    suma = numero1 + numero2
    print(f"La suma es {suma}")

#Iniciamos nuestro programa

num1 = int(input ("Dame el numero 1: "))
num2 = int(input ("Dame el numero 2: "))
sumapro (num1, num2)

def restapro(valor1, valor2):
    resta = valor1 - valor2
    print(f"La resta es {resta}")
#Iniciamos nuestro programa

val1 = int(input("Dame el valor 1: "))
val2 = int(input("Dame el valor 2: "))
restapro (val1, val2)

def multiplicapro(valor1, valor2):
    multiplicacion = valor1 * valor2
    print(f"La multiplicacion es {multiplicacion}")
#Iniciamos nuestro programa
val1 = int(input("Dame el valor 1: "))
val2 = int(input("Dame el valor 2: "))
multiplicapro (val1, val2)

def divisionpro(valor1, valor2):
    division = valor1 / valor2
    print(f"La division es {division}")
#Iniciamos nuestro programa
val1 = int(input("Dame el valor 1: "))
val2 = int(input("Dame el valor 2: "))
divisionpro (val1, val2)
