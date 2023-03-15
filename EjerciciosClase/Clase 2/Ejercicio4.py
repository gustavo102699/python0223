import sys

def imprimir_argumentos():
    argumentos = sys.argv[1:]
    print("Argumentos ingresados:")
    for argumento in argumentos:
        print(argumento)

imprimir_argumentos()