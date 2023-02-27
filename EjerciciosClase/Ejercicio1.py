##1.Realizar un programa que ingrese sus datos personales e imprimirlos, poner en comentario su nombre completo.
    ##Gustavo Hurtado Benancio
name=input("Ingresa tu nombre: ")
lastname=input("Ingresa tus Apellidos: ")
message="Hola"
print(message,name,lastname)

##2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado.

menu=""" CALCULANDO ÁREAS
    1) Área del círculo
    2) Área del triangulo
    3) Área del triangulo
    4) Salir
"""
print(menu)
op=int(input("Ingreso opción :"))

if type(op) == int:
   
    if op==1:
        radio=int(input("Ingrese rádio: "))
        acirculo=3.14*radio
        print(f"El área del circulo es {acirculo}")
    elif op==2:
        base=int(input("Ingrese base: "))
        altura=int(input("Ingrese altura: "))
        atriangulo=(base*altura)/2
        print(f"El área del triangulo es {atriangulo}")
    elif op==3:
        lado=int(input("Ingrese lado: "))
        acuadrado=lado**2
        print(f"El área del cuadrado es {acuadrado}")
    elif op==4:
        exit
    else: 
        print("Opción no válida")
else:
    print("Por favor, ingresar un número permitido")
