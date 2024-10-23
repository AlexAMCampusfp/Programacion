def contar_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador += 1
    return contador

# Ejemplo de uso
print(contar_pares([1, 2, 3, 4, 5, 6]))  # Debería imprimir 3

def encontrar_maximo(numeros):
    if not numeros:
        return None  # Retorna None si la lista está vacía
    
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo

# Ejemplo de uso
print(encontrar_maximo([3, 5, 2, 9, 1]))  # Debería imprimir 9

def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible por i, no es primo
    return True  # Si no se encontró ningún divisor, es primo

# Ejemplo de uso
print(es_primo(7))   # Debería imprimir True
print(es_primo(10))  # Debería imprimir False

def suma_hasta_limite(limite):
    if limite < 1:
        return 0  # Retorna 0 si el límite no es un número entero positivo
    suma = 0
    for i in range(1, limite + 1):
        suma += i
    return suma

# Ejemplo de uso
print(suma_hasta_limite(5))  # Debería imprimir 15 (1 + 2 + 3 + 4 + 5)

def contar_vocales(cadena):
    contador = 0
    vocales = "aeiouAEIOU"  # Incluyendo vocales en mayúsculas
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Ejemplo de uso
print(contar_vocales("Hola Mundo"))  # Debería imprimir 4

