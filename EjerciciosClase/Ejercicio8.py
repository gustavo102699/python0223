#8.Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
password = "Python2023"
passwordnew = input("Ingresar contraseña: ")
if password.lower() == passwordnew.lower():
    print("La contraseña COINCIDE")
else:
    print("La contraseña NO COINCIDE")