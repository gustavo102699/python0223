#9. Defina una lista con al menos 4 elementos que a su vez sean tuplas que tengan 
# la siguiente estructura ( ‘nombre’ ,’edad’, ‘dni’) y otra que sea una lista de dnis.
#-realizar un programa que filtre a la persona mayores de edad y a los que cumplen esa opción
#verificar que su dni se encuentre ahi, por ultimo imprimir el nombre de las personas que cumplen las condiciones anteriores
# - Definir una lista vacia , que luego se agregue el elemento que cumplio todas las condiciones.

listpersonas = [("Alberto", 15, 15660879), ("Brandon", 19, 65463871), ("Carlos", 18, 34356762), ("David", 31, 70865721)]
listdni = [15660879, 65463871, 34356762,70865721]

FiltroMayorEdad = []
FiltroListaVacia = []

for ListaNuevaPersona in listpersonas:
    Nombre, Edad, Dni = ListaNuevaPersona
    if Edad >= 18 and Dni in listdni:
        FiltroMayorEdad.append(Nombre)
        FiltroListaVacia.append(ListaNuevaPersona)
print(f"Personas mayores de 18 : {FiltroMayorEdad}")
print(f"La nueva lista es: {FiltroListaVacia}")