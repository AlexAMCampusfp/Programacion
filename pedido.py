from cliente import Cliente
from producto import Producto

clientes = []
pedidos = []
productos = [
    Producto("Producto A", 10.0),
    Producto("Producto B", 15.0),
    Producto("Producto C", 20.0)
]

def registrar_cliente(): #Pedimos los datos del cliente para enviarle el producto
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo (único): ")
    telefono = input("Ingrese su teléfono: ")

    if any(cliente.correo == correo for cliente in clientes): #Si el correo se repite al usuario le saltara un error de que ese correo ya esta en uso
        print("Error: El correo ya está registrado.")
    else:
        nuevo_cliente = Cliente(nombre, apellido, correo, telefono) #En el caso de que el correo sea nuevo no dara ningun problema y le registrara 
        clientes.append(nuevo_cliente)
        print("Registro exitoso.")

def mostrar_productos(): #Funcion para mostrar a los usuarios los productos que pueden comprar 
    print("Productos disponibles:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto.nombre} - ${producto.precio}")

def realizar_compra(): #Para realizar la compra simplemente nos dara el correo que puso cuando se registro y si esta ese correo registrado la funcion se realizara perfectamente y le mostrara los productos que tiene su pedido
    correo = input("Ingrese su correo para identificarse: ")
    cliente = next((c for c in clientes if c.correo == correo), None)

    if cliente is None:
        print("Error: Cliente no encontrado.")
        return

    mostrar_productos()
    seleccionados = []
    while True:
        opcion = input("Seleccione el número del producto para añadir a la compra (o '0' para finalizar): ")
        if opcion == '0':
            break
        try:
            index = int(opcion) - 1
            if 0 <= index < len(productos):
                seleccionados.append(productos[index])
                print(f"{productos[index].nombre} añadido a la compra.")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if seleccionados:
        nuevo_pedido = Pedido(cliente, seleccionados)
        pedidos.append(nuevo_pedido)
        print(f"Compra realizada. Número de pedido: {nuevo_pedido.numero_pedido}")
    else:
        print("No se ha realizado ninguna compra.")

class Pedido: #Para identificar el numero del pedido el cliente nos dira qien es y que productos lleva su producto y le diremos por ejemplo que su pedido es el numero 7
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.numero_pedido = self.generar_numero_pedido()

    def generar_numero_pedido(self):
        return len(pedidos) + 1  # Simplemente incrementa el contador de pedidos
