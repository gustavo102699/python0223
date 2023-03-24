from main import Productos
class CarritoCompra:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,produc= Productos):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock)
        else:
            print("el producto no tienen stock")
         
    def quitarProducto(self, produc=Productos):
        carrito.mostrarProductos()
        if len(self.listaProductos)>0:            
            idd = int(input("ID producto a eliminar: "))                    
            for product in self.listaProductos:
                if product.id == int(idd):
                    self.listaProductos.remove(product)
                    product.updateStock(product.stock+1)
                    print("Se eliminó el producto.")  
                else:
                    print("ID No existe")
            else:
             print("El carrito está vacío ...")                  
        
    def quitarProduct(self,id):
            for index in self.listaProductos:
                if index.id==id:
                    self.listaProductos.remove(index)
                    print("--Producto eliminado--")
                    for a in self.listaProductos:
                        if a.id>id:
                            a.updateID(a.id-1) 
                else:
                    print("--No existe producto con ese id--")   
    def calcularPrecio(self):
            for i in self.listaProductos:
                self.precioTotal+=i.precio
            print(f"Precio total: {self.precioTotal}")
    def validarStock(self,product:Productos):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print("Cantidad de productos:",len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("El carro está vacío")    

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Quitar Producto
    4)Calcular precio
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opción a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del producto:")
            stock=int(input("ingrese el stock del producto:"))
            release=int(input("ingrese el release del producto:"))
            product=Productos(id,name,precio,tipo,stock,release)
            carrito.agregarProducto()
        except Exception as Error:
                print("sucedio un error",Error)
        else:
            print("agregando en el menu...")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion ==3:
        carrito.quitarProducto()        
    if opcion==4:
        carrito.calcularPrecio()
    if opcion ==5:
        print ("Hasta luego")
        break
    else:
        print("La opción ingresada no existe.")