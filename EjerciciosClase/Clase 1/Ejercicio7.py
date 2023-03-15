#7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
#● Si los dos números son iguales
#● Si los dos números son diferentes
#● Si el primero es mayor que el segundo
#● Si el segundo es mayor o igual que el primero

valor1=int(input("Ingrese el valor1: "))
valor2=int(input("Ingrese el valor2: "))

if valor1==valor2 :
    print("Los valores son iguales")
elif valor1>valor2 and valor1!=valor2:    
    print("-Los valores son diferentes")
    print("-El primer valor es mayor al segundo")
elif valor2>=valor1 and valor1!=valor2:  
    print("-Los valores son diferentes")
    print("-El segundo valor es mayor o igual que el primero")
