import sqlite3

def conectar_db():
    return sqlite3.connect('supermercado.db')

def crear_cliente(nombre, email):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()
    conn.close()

def leer_clientes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def actualizar_cliente(id_cliente, nombre, email):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nombre = ?, email = ? WHERE id = ?", (nombre, email, id_cliente))
    conn.commit()
    conn.close()

def eliminar_cliente(id_cliente):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    conn.close()

def menu_clientes():
    while True:
        print("\n--- Menú Clientes ---")
        print("1. Crear cliente")
        print("2. Leer clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            email = input("Email del cliente: ")
            crear_cliente(nombre, email)
            print("Cliente creado con éxito.")
        elif opcion == '2':
            clientes = leer_clientes()
            for cliente in clientes:
                print(cliente)
        elif opcion == '3':
            id_cliente = int(input("ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            actualizar_cliente(id_cliente, nombre, email)
            print("Cliente actualizado con éxito.")
        elif opcion == '4':
            id_cliente = int(input("ID del cliente a eliminar: "))
            eliminar_cliente(id_cliente)
            print("Cliente eliminado con éxito.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Operar sobre la tabla Clientes")
        print("2. Operar sobre la tabla Categorías (no implementado)")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            print("Operaciones sobre la tabla Categorías aún no implementadas.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()
