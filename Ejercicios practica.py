# import math
# def calcular_area_circulo(radio):
#      "Calcular el area de un circulo dado su radio"
#      area= math.pi * (radio * 2)
#      return area
#  #El usuario introduce el radio

# radio = float(input("Ingrese el radio: "))

# area_resultado= calcular_area_circulo(radio)
# print(f"El area del circulo con radio {radio} es: {area_resultado: .2f}")

# def contar_vocales(frase):
#      "Cuenta el número de vocales en una frase dada."
#      vocales = "aeiouAEIOU"
#      contador = 0
#      for letra in frase:
#          if letra in vocales:
#              contador += 1
#      return contador

# # # Solicitar al usuario que ingrese una frase
# frase = input("Ingrese una frase: ")

# # #Resultado final
# numero_vocales = contar_vocales(frase)
# print(f"El número de vocales es: {numero_vocales}")

# def generar_pares():
#     "Generar una lista de numeros pares del 1 al 50"
#     pares = [numero for numero in range(1,51) if numero % 2 == 0] #Si el numero que esta entre 1 y 51 dividido entre 2 el resto sale 0 le decimos que lo cuente y q lo repita
#     return pares
# #Resultado final
# lista_pares = generar_pares()
# print (f"Los numeros pares que estan entre 1 y 50 son:", lista_pares)

# def celsius_a_fahrenheit(celsius):
#     "Convierte una temperatura de Celsius a Fahrenheit."
#     return (celsius * 9/5) + 32

# # Lista de temperaturas en Celsius
# temperaturas_celsius = [0, 10, 20, 30, 40, 100]

# # Diccionario para almacenar las temperaturas convertidas
# temperaturas_fahrenheit = {}

# # Convertir cada temperatura y almacenar en el diccionario
# for temp in temperaturas_celsius:
#     temperaturas_fahrenheit[temp] = celsius_a_fahrenheit(temp)

# Resultado final
# print("Temperaturas en Celsius y sus equivalentes en Fahrenheit:")
# print(temperaturas_fahrenheit)

# def contar_palabras_largas(lista_palabras):
#     "Cuenta cuántas palabras en la lista tienen más de 5 letras."
#     contador = sum(1 for palabra in lista_palabras if len(palabra) > 5)
#     return contador

# # Lista de palabras
# palabras = ["hola", "amigo", "programación", "python", "función", "lista"]

# #Resultado final
# numero_palabras_largas = contar_palabras_largas(palabras)
# print(f"El número de palabras con más de 5 letras es: {numero_palabras_largas}")

# def contar_palabras(frase):
#     "Cuenta el número de palabras en una frase dada."
#     # Dividir la frase en palabras usando espacios como separadores
#     palabras = frase.split()
#     return len(palabras)

# # Solicitar al usuario que ingrese una frase
# frase = input("Ingrese una frase: ")

# # Resultado final
# numero_palabras = contar_palabras(frase)
# print(f"El número de palabras en la frase es: {numero_palabras}")

# def agregar_tarea(tareas, tarea):
#     "Agrega una tarea a la lista de tareas."
#     tareas.append(tarea)

# # Lista para almacenar las tareas
# tareas_pendientes = []

# # Bucle para solicitar tareas al usuario
# while True:
#     tarea = input("Ingrese una tarea (o escriba 'fin' para terminar): ")
#     if tarea.lower() == 'fin':
#         break
#     agregar_tarea(tareas_pendientes, tarea)

# #Resultado final
# print("\nLista de tareas pendientes:")
# for i, tarea in enumerate(tareas_pendientes, start=1):
#     print(f"{i}. {tarea}")

# def es_contraseña_segura(contrasena):
#     "Verifica si la contraseña es segura."
#     if len(contrasena) < 8:
#         return False
#     if not any(c.isupper() for c in contrasena):
#         return False
#     if not any(c.islower() for c in contrasena):
#         return False
#     if not any(c.isdigit() for c in contrasena):
#         return False
#     return True

# # Solicitar al usuario que ingrese una contraseña
# contrasena_usuario = input("Ingrese una contraseña: ")

# # Resultado final
# if es_contraseña_segura(contrasena_usuario):
#     print("La contraseña es segura.")
# else:
#     print("La contraseña no es segura. Asegúrese de que tenga al menos 8 caracteres, contenga mayúsculas, minúsculas y números.")

def agregar_asistente(asistentes, nombre, edad):
    "Agrega un asistente a la lista."
    asistente = {'nombre': nombre, 'edad': edad}
    asistentes.append(asistente)

# Lista para almacenar los asistentes
asistentes_evento = []

# Bucle para solicitar nombres y edades
while True:
    nombre = input("Ingrese el nombre del asistente (o escriba 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    edad = input("Ingrese la edad del asistente: ")
    
    # Agregar el asistente a la lista
    agregar_asistente(asistentes_evento, nombre, edad)

# Resultado final
print("\nLista de asistentes al evento:")
for i, asistente in enumerate(asistentes_evento, start=1):
    print(f"{i}. Nombre: {asistente['nombre']}, Edad: {asistente['edad']}")









