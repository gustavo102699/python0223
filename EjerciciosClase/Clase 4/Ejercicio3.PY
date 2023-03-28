import os
from main2 import casaCambio
from main2 import pokeclas

def borrarPantalla():
    os.system('cls' if os.name=='nt' else 'clear')

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