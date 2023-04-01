import os
import requests

def borrarPantalla():
    os.system('cls' if os.name=='nt' else 'clear')
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

menu = """
        OPCIONES DEL MENU
        1)Sunat
        2)Pokemon
        3)Salir
        """
menuSunat = """
        SUNAT
        1)Ver tipo de cambio
        2)Opción comprar
        3)Opción vender
        4)Salir
"""
menuPokemon = """
        POKEDEX
        1)Mostrar
        2)Buscar
        3)Salir
"""
while True:
    print(menu)
    opcion = int(input("Selecione una opcion: "))
    if opcion == 1:
        borrarPantalla()
        print(menuSunat)
        opcion = int(input("Selecione una opcion: "))
        if opcion == 1:
            data = sunat()
            compra = data["compra"]
            venta = data["venta"]
            print(f"La compra esta: {compra}")
            print(f"La venta esta: {venta}")
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
        if opcion == 2:
            uno = casaCambio()
            cantidad = float(input("Ingrese la cantidad de dolar que desea comprar: "))
            soles = uno.compra(cantidad)
            print(f"La cantidad de soles a pagar es: {soles} ")
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
            continue
        if opcion == 3:
            uno = casaCambio()
            cantidad = float(input("Ingrese la cantidad de soles que desea vender: "))
            dollar = uno.venta(cantidad)
            print(f"La cantidad de dolares a recibir es: {dollar} ")
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
            continue
        if opcion == 4:
            break

    if opcion == 2:
        borrarPantalla()
        print(menuPokemon)
        opcion = int(input("Selecione una opcion: "))
        if opcion == 1:
            pokeVariable = pokeclas()
            pokeVariable.listar()
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
        if opcion == 2:
            data = pokedex()
            pokeVariable = pokeclas()
            nombre = input("Ingrese el nombre del pokemon: ")
            pokeVariable.buscar(nombre)
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
        if opcion == 3:
            break

    if opcion == 3:
        break