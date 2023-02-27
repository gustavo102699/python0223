#7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
#● Si los dos números son iguales
#● Si los dos números son diferentes
#● Si el primero es mayor que el segundo
#● Si el segundo es mayor o igual que el primero

valor1=int(input("Ingrese el valor1: "))
valor2=int(input("Ingrese el valor2: "))

igual=(valor1==valor2)
dift=(valor1!=valor2)
mayorval1=(valor1>valor2)
mayorval2=(valor2>=valor1)

print(f"¿Son iguales? : {igual}")
print(f"¿Son diferentes? : {dift}")
print(f"¿El primero es mayor que el segundo? : {mayorval1}")
print(f"¿El segundo es mayor o igual que el primero? : {mayorval2}")

