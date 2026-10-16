# Quiz 
# Diego Alejandro Mojica Baez
class producto:
    def __init__(self, iD = None, nombre = None, precio = None, cantidad = None):
        self.iD = iD
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

lista = [
    producto("A4", "Palomitas", 20000, 50),
    producto("F5", "Gaseosa", 15000, 45),
    producto("R8", "Perro", 22000, 80),
    producto("9E", "Chocolatina", 5000, 75),
    producto("3Q", "Agua", 10000, 100)
]

def vender():
    temp = 0
    totalT = 0
    while temp == 0:
        tempId = str(input("Ingresa el Id del producto: "))
        for i in range(5):
            if tempId == lista [i].iD:
                ncantidad = int(input("Ingrese la cantidad: "))
                lista [i].cantidad = lista [i].cantidad - ncantidad
                total = lista [i].precio * ncantidad
        totalT = totalT + total
        break

def consultarLista():
    print()
    print("Lista de productos: ")
    for i in range(len(lista)):
        print(f"ID: {lista [i].iD}, Nombre: {lista [i].nombre}, Precio: {lista [i].precio}, Cantidad: {lista [i].cantidad}")  
    print() 

def cambiarCant():
    temp = 0
    nCantidad = 0
    while temp == 0:
        tempid = str(input("Ingresa el ID del producto a modificar su cantidad: "))
        print("Salir: 1 ")
        for i in range(5):
            if lista [i].iD == "tempid":
                nCantidad = float(input(f"Ingresa la nueva cantidad para el ID {lista [i].iD}"))
                lista [i].cantidad = nCantidad
            break

opcion = 0
while opcion != 4:
    print("Bienvenido")
    print("1. Vender")
    print("2. Consultar lista de productos")
    print("3. Actualizar cantidad de un producto especifico")
    print("4. Cerrar sesion")
    opcion = int(input("Ingresa la opcion: "))
    if opcion == 1:
        vender()
    elif opcion == 2:
        consultarLista()
    elif opcion == 3:
        cambiarCant()
    elif opcion == 4:
        break
    else:
        opcion = 0