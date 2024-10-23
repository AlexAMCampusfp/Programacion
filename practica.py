def mayor_a_10(num):
    return num > 10

numeros = [4, 9, 16, 25, 1, 7, 12]
numeros_filtrados = list(filter(mayor_a_10, numeros))

print(numeros_filtrados)

def metros_a_centimetros(metros):
    return metros * 100

alturas_metros = [1.60, 1.75, 1.80, 1.50]
alturas_centimetros = list(map(metros_a_centimetros, alturas_metros))

print(alturas_centimetros)

