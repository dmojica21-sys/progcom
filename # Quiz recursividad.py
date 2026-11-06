# Quiz recursividad
# Diego Alejandro Mojica Baez



def calcular_escalones_recursivo(altura, pasos):
    if altura > 0:
        altura = altura - pasos
        return 1 + calcular_escalones_recursivo(altura, pasos)
    else:
        return 0
   
    
altura = float(input("Ingrese la altura de la escalera: "))
pasos = int (input("Ingrese el # de pasos: "))
npasos = calcular_escalones_recursivo(altura, pasos)
print(npasos)