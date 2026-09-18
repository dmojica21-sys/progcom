# Aa
def obtenerPrecio(ID):
    if ID == "A1":
        precio = 1000
    elif ID == "A2":
        precio = 500
    elif ID == "B1":
        precio = 2000
    elif ID == "B2":
        precio = 5000
    elif ID == "C1":
        precio = 1800
    else:
        precio = -1
    return precio

print(" Maquina ")
print(" ID product?: ")
IDUser = str(input())
valorProducto = obtenerPrecio(IDUser)
if valorProducto != -1:
    print("El precio es: $", valorProducto)
else:
    print("ID Invalido")

