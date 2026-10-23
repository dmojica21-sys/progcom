# Sumatoria n de n hasta 1

def sumatoriaRegresiva(numero):
    if numero !=0:
        return numero + sumatoriaRegresiva(numero - 1)
    else:
        return 0

temp = sumatoriaRegresiva(5)
print(temp)