from capalogica import*
message="""
    ---MENU DE OPCIONES---
    1)Tabla Ventas 2023
    2)Crear nueva tabla Ventas2024
"""
print(message)
option=int(input("Ingrese una opción: "))

consultar(option)