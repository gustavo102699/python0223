class Item:
    def __init__(self, name, descrip, prec):
        self.name = name
        self.descrip = descrip
        self.prec = prec
        
    def __str__(self):
        return f"{self.name}: {self.descrip} (${self.prec})"

class Catalogo:
    def __init__(self):
        self.products = []
    
    def agregar_product(self, product):
        self.products.append(product)
    
    def mostrar_products(self):
        for product in self.products:
            print(f"\n{product}")

#---

def dividir(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:
        return resultado

#---

import os

class Product:
    def __init__(self, name, cod):
        self.name = name
        self.cod = cod
    
    def __str__(self):
        try:
            pais, lote, anio = self.cod.split("-")
        except ValueError:
            print("Error")
        else:
            print(f"Ruta: {os.getcwd()}")
            return f"Nombre del producto: {self.name}\nCódigo de producto: {self.cod}\nPais de origen: {pais}\nLote: {lote}"
        finally:
            print("Proceso terminado")

#---

class Productos:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"ID: {self.id} -- el producto {self.nombre} con precio de {self.precio} cuenta con {self.stock} stock"
    def updateStock(self,stock):
        self.stock=stock
    
  