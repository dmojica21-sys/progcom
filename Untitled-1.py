#  funciones
def sumar():
    x = int(input("valor de x: "))
    y = int(input("valor de x: "))
    z = x + y # - w
    print(z)
# toma valor del orden
''' w = 10
sumar()
w = 40
sumar() '''

# Funcion condicionada
def sumar2(A,B):
    C = A + B
    print(C)

''' sumar2(100, 50)
Ax = int(input("valor de A: "))
Bx = int(input("valor de B: "))
sumar2(Ax, Bx) '''

def sumar3(i, j):
    k = i + j
# return retira valor a rama principal
    return k
''' Ax = int(input("valor de A: "))
Bx = int(input("valor de B: "))
temp = sumar3(Ax, Bx)
print(temp) '''


def calcBisiesto(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

print("Año:")
yearUser = int(input())
if calcBisiesto(yearUser): 
    print(" Es bisiesto")
else:
    print("No bisiesto")
