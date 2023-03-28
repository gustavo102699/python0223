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
            

"""
def sunat():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    data = requests.get(url).json()
    return data

def pokedex():
    url = "https://pokeapi.co/api/v2/pokedex/1/"
    data = requests.get(url).json()
    return data

def pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/"
    data = requests.get(url).json()

class casaCambio:
    data = sunat()
    compraActualizado = data["Cambio Compra"]
    ventaActualizado = data["Cambio Venta"]
    def compra(self,cantidadDollar):
        cantidadSoles = cantidadDollar*self.compraActualizado
        return cantidadSoles
    def venta(self,cantidadSoles):
        cantidadDollar = cantidadSoles/self.ventaActualizado
        return cantidadDollar

class pokeclas:
    data = pokedex()
    def listar(self):
        lista = self.data['pokemon_entries']
        for i,value in enumerate(lista):
            nombre = value['pokemon_species']['name']
            print(i,")",nombre)
    def buscar(self,nombre):
        lista = self.data['pokemon_entries']
        for i,valor in enumerate(lista):
            if valor['pokemon_species']['name'] == nombre:
                    print("¡Esta en la lista!")
                    print(valor['pokemon_species']['name'], ",enlace: ",valor['pokemon_species']['url'])
                    condicion = False
                    break
            else:
                    condicion = True
        if condicion:
                print("POKEMÓN NO ENCONTRADO EN LISTA")
"""
              
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