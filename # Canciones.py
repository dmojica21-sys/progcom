# Canciones

class Cancion:
    def __init__(self, titulo = None, autor = None, duracion = None):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion
    def mostrarDatos(self):
        print("Titulo: ", self.titulo)    
        print("Autor: ", self.autor) 
        print("Duracion: ", self.duracion, "min") 
    def registDatos(self):
        print("Ingrese titulo: ")
        self.titulo = str(input())
        print("Ingrese autor: ")
        self.autor = str(input())
        print("Ingrese duracion: ")
        self.duracion = float(input())

a = Cancion("Aa", "Bb", 1.2)
b= Cancion("VV", "IJ", 234)
c = Cancion("JK", "FWE", 938)
d= Cancion()
d.registDatos()
d.mostrarDatos()