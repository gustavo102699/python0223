from main import Product

product = Product((input("Producto: ")), (input("Código (Separado por -): ")))

print(product.__str__())