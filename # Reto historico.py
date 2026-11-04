# Reto historico
# Diego Alejandro Mojica Baez

def invert_papiro(frase, tamano):
    if tamano <= 0:
        return ""
    return frase[tamano - 1] + invert_papiro(frase, tamano - 1)


frase = input("Ingrese frase: ")
invertido = invert_papiro(frase, len(frase))
print(invertido)