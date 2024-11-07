import sqlite3

# Conectar a la base de datos SUPERMERCADO (o crearla si no existe)
conn = sqlite3.connect('SUPERMERCADO.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS categoria (
    idcategoria INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
)
''')

def insertar_categoria():
    idcategoria = int(input("Ingrese el id de la categoría: "))
    nombre = input("Ingrese el nombre de la categoría: ")
    cursor.execute("INSERT INTO categoria (idcategoria, nombre) VALUES (?, ?)", (idcategoria, nombre))
    conn.commit()
    print("Categoría insertada exitosamente.")

def listar_categorias():
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    print("Categorías disponibles:")
    for categoria in categorias:
        print(f"ID: {categoria[0]}, Nombre: {categoria[1]}")

def actualizar_categoria():
    idcategoria = int(input("Ingrese el id de la categoría que desea modificar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
    cursor.execute("UPDATE categoria SET nombre = ? WHERE idcategoria = ?", (nuevo_nombre, idcategoria))
    conn.commit()
    print("Categoría actualizada exitosamente.")

def eliminar_categoria():
    idcategoria = int(input("Ingrese el id de la categoría que desea eliminar: "))
    cursor.execute("DELETE FROM categoria WHERE idcategoria = ?", (idcategoria,))
    conn.commit()
    print("Categoría eliminada exitosamente.")

def menu():
    while True:
        print("\n--- Menú de Categorías ---")
        print("1. Crear categoría")
        print("2. Leer categorías")
        print("3. Actualizar categoría")
        print("4. Eliminar categoría")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            insertar_categoria()
        elif opcion == '2':
            listar_categorias()
        elif opcion == '3':
            actualizar_categoria()
        elif opcion == '4':
            eliminar_categoria()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()

# Cerrar la conexión
conn.close()
