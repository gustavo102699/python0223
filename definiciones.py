#consideraciones para crear un programa archivo de python
# nombre del archivo inicar en letras y al terminar puede ser un numero
# no iniciar en numeros (opcional)
# sin espacios 
# sin caracteres especiales
# EJEMPLOS QUE NO HACER : *PROGRAMA.PY
### entorno de trabajo
## python en cualquier version desde la 3.9 en adelante
## visual studio code o anaconda 
## Cuenta de github 
## git instalado y github desktop
## material ->https://github.com/gdelgador/PythonFundamentos
# Definir el diccionario
curso = {'nombre de curso': '',
         'cantidad de alumnos': 0,
         'activo': False,
         'nombre de profesor': '',
         'max nota': 0,
         'alumnos': []}


# Permitir al usuario ingresar nuevos valores para el diccionario
curso['nombre de curso'] = input("Ingrese el nombre del curso: ")
curso['cantidad de alumnos'] = int(input("Ingrese la cantidad de alumnos: "))
curso['activo'] = bool(input("¿El curso está activo? (True/False): "))
curso['nombre de profesor'] = input("Ingrese el nombre del profesor: ")
curso['max nota'] = float(input("Ingrese la nota máxima: "))
alumnos = input("Ingrese los nombres de los alumnos separados por comas: ")
curso['alumnos'] = alumnos.split(' ')

# Imprimir el diccionario
print(curso)
