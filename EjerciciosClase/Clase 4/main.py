import random
#import requests
import re

class sorteo:
    lista = []
    def __init__(self,valorMax:float,cantidad:float) -> None:
        self.valorMax = valorMax
        self.cantidad  = cantidad
    
    def sorteoNumeros(self):
        for i in range(self.cantidad):
            self.lista.append(int(random.random()*self.valorMax+1))
            
def ValidarNumero(numero):
    patron = r'^9\d*$'
    if re.match(patron,numero):
        print("El numero es valido")
    else:
        print("Número NO VALIDO (Debe empezar por 9)")
        

class Registro:
    def __init__(self) -> None:
        self.archivo = open("texto.txt", "a")
    def guardar(self,contenido):
        self.archivo = open("texto.txt","a") 
        self.archivo.write(contenido)
        self.archivo.close()
    def mostrar(self):
        self.archivo = open("texto.txt","r")
        contenido = self.archivo.read()
        print(contenido)
        self.archivo.close()