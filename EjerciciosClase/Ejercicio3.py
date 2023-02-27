##3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división y división entera.
num1=int(input("Valor 1: "))
num2=int(input("Valor 2: "))
num3=int(input("Valor 3: "))
suma=num1+num2+num3
resta=num1-num2-num3
multpl=num1*num2*num3
divi=round(num1/num2/num3,2)
diventera=num1//num2//num3
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multpl}")
print(f"La división es: {divi}")
print(f"La división entera es: {diventera}")
