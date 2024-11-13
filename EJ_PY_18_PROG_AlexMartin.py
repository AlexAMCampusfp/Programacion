import sqlite3
#Funciones
def conectar_db():
    return sqlite3.connect('supermercado.db')

def crear_pedido(fecha, cliente):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pedidos (fecha, cliente) VALUES (?, ?)", (fecha, cliente))
    conn.commit()
    conn.close()

def leer_pedidos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

def actualizar_pedido(id, fecha, cliente):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Pedidos SET fecha = ?, cliente = ? WHERE id = ?", (fecha, cliente, id))
    conn.commit()
    conn.close()

def eliminar_pedido(id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pedidos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
#Menu principal
def menu_principal():
    while True:
        print("Menú de Opciones:")
        print("1. Pedidos")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_pedidos()
        elif opcion == '2':
            break
        else:
            print("Opción no válida.")
#Menu pedidos
def menu_pedidos():
    while True:
        print("\nMenú de Pedidos:")
        print("1. Crear Pedido")
        print("2. Leer Pedidos")
        print("3. Actualizar Pedido")
        print("4. Eliminar Pedido")
        print("5. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            cliente = input("Ingrese el nombre del cliente: ")
            crear_pedido(fecha, cliente)
            print("Pedido creado exitosamente.")
        elif opcion == '2':
            pedidos = leer_pedidos()
            for pedido in pedidos:
                print(pedido)
        elif opcion == '3':
            id = int(input("Ingrese el ID del pedido a actualizar: "))
            fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
            cliente = input("Ingrese el nuevo nombre del cliente: ")
            actualizar_pedido(id, fecha, cliente)
            print("Pedido actualizado exitosamente.")
        elif opcion == '4':
            id = int(input("Ingrese el ID del pedido a eliminar: "))
            eliminar_pedido(id)
            print("Pedido eliminado exitosamente.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()

