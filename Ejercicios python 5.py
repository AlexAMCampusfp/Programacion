#Ejercicio 1

# Definimos la función que suma 5
def sumar_cinco(numero):
    return numero + 5

# Lista de números
numeros = [1, 2, 3, 4, 5]

resultado = list(map(sumar_cinco, numeros))

# Imprimimos el resultado
print(resultado)

#Ejercicio 2

# Lista de frases
frases = [
    "hola mundo",
    "bienvenido a python",
    "programación es divertida",
    "aprendiendo funciones"
]

resultado = list(map(str.title, frases))

# Imprimimos el resultado
print(resultado)

#Ejercicio 3

# Definimos la función que calcula el doble
def calcular_doble(numero):
    return numero * 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos map() para aplicar la función a cada elemento de la lista
resultado = list(map(calcular_doble, numeros))

# Imprimimos el resultado
print(resultado)

#Ejercicio 4

# Lista de números decimales
numeros_decimales = [1.2, 2.5, 3.7, 4.1, 5.9]

resultado = list(map(round, numeros_decimales))

# Imprimimos el resultado
print(resultado)

#Ejercicio 5

# Definimos la función que calcula la longitud de una palabra
def calcular_longitud(palabra):
    return len(palabra)


# Lista de palabras
palabras = ["hola", "mundo", "programación", "python", "inteligencia"]

resultado = list(map(calcular_longitud, palabras))

# Imprimimos el resultado
print(resultado)
