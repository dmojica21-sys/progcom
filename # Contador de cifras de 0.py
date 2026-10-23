# Contador de cifras de 0

def contarCifras(numero):
    if numero // 10 !=0:
        return 1 + contarCifras(numero//10)
    else:
        return 1

temp = contarCifras(18446)
print(temp)

