# carrito de compras
# Diego Alejandro Mojica Baez
class producto:
    def __init__(self, nombre = None, precio = None):
        self.nombre = nombre
        self.precio = precio
    def showDatos(self):
        print("Nombre: ", self.nombre)    
        print("Precio: ", self.precio) 
carrito = []
def addProducto():
    temp = producto()
    print("Ingrese Nombre: ")
    temp.nombre = str(input())
    print("Ingrese precio: ")
    temp.precio = float(input())
    carrito.append(temp)

def showTotal():
    total = 0
    for i in range(len(carrito)):
        total = total + carrito [i].precio
        round(total,3)
    print(total)

def resumen():
    for i in range(len(carrito)):
        print(f"Producto : {carrito [i].nombre} , Precio: {carrito [i].precio}")

opcion = 0
while opcion !=-1:
    print("Bienvenido")
    print("1.Agregar productos")
    print("2. Mostrar total")
    print("3. Resumen del carrito")
    print("Salir (-1) ")
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        addProducto()
    elif opcion == 2: 
        showTotal()
    elif opcion == 3:
        resumen()
    elif opcion == -1:
        break
    else:
        opcion == 0
