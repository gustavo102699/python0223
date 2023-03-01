#10.Defina un diccionario que tenga las siguientes llaves (nombre de curso,cantidad
#de alumnos,activo(tipo boleano),nombre de profesor,max nota,alumnos(lista)) a
#todos ellos como valor que lleven un valor de inicializacion ,por ejemplo si es entero 0 ,si es string una cadena vacia.
# -Realizar al menos 3 inputs para ingresar por teclado nuevos valores para el diccionario .
# -Imprimir el diccionario.

Curso = {
    
        "Nombre de curso": "",
        "Cantidad de Alumnos": 0,
        "Activo": True,
        "Nombre Profesor": "",
        "Max Nota": 0,
        "Alumnos" : []
        }

Curso["Nombre de curso"] = input("Ingrese Nombre de curso: ")
Curso["Cantidad de Alumnos"] = int(input("Ingrese cantidad de alumnos: "))
Curso["Nombre Profesor"] = input("Profesor: ")
Curso["Max Nota"] = int(input("Max Nota: "))
Curso["Alumnos"] = input("Alumnos (separar con guión): ").split("-")
print(Curso) 