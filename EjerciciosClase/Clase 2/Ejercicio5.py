import os
def listar(path):
    elementos = os.listdir(path)

    for elemento in elementos:
        ruta = os.path.join(path, elemento)
        
        if os.path.isdir(ruta):
            print(f"\nCarpeta: {ruta}")
            listar(ruta)
        else:
            print(f"Archivos: {ruta}")

listar(".")