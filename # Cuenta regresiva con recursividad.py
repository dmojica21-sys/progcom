# Cuenta regresiva con recursividad
def cuentaRegresiva(numero):
    print(numero)
    numero = numero - 1
    if numero > 0:
        return cuentaRegresiva(numero)
    else:
        return print ("Lanzamiento")
# recursivo debe tener return
cuentaRegresiva(10)