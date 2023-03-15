Numero1 = int(input("Numero 1: "))
Numero2 = int(input("Numero 2: "))
def mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(f"El número mayor es: {mayor(Numero1,Numero2)}")