from main import Item
from main import Catalogo

catalogo = Catalogo()

product =Item((input("Ingrese producto 1:")), (input("Ingrese descripción 1:")), int(input("Ingrese precio 1:")))
catalogo.agregar_product(product)

#MOTOR
#Motor modelo Diesel
#7600

product1 = Item((input("Ingrese producto 2:")), (input("Ingrese descripción 2:")), int(input("Ingrese precio 2:")))
catalogo.agregar_product(product1)
#ACEITE
#Aceite Mobil 7500
#230

product1 = Item("Filtro", "Filtro de aire acondicionado", 239)
catalogo.agregar_product(product1)

product1 = Item("Bateria", "Bateria marca DXL", 120)
catalogo.agregar_product(product1)

catalogo.mostrar_products()