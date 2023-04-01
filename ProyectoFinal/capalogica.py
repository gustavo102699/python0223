from capamodelo import *
msj1 ="""
---MENU DE OPCIONES---
1) Tabla Ventas 2023
2) Mostrar tipo de datos de la tabla
3) Añadir una columna
4) Salir
"""
msj2 =""" 
1) Ingresar datos
2) Mostrar Tabla
3) Salir
"""
def consultar(opcion:int):
    match opcion:
        case 1:
            while True:
                print(msj1)
                op= int(input("Seleccione una opción: "))
                match op:
                    case 1:
                        Ventas2023.MostrarVenta()                
                    case 2:
                        Ventas2023.TiposDatos()
                    case 3:
                        Ventas2023.NuevaColumna()
                    case 4:
                        break
                    case _:
                        print("Ingrese una opción Valida.")
            
        case 2:
            while True:
                Tablas.crear_table()                          
                print(msj2)
                op= int(input("Seleccione una opción: "))
                match op:
                    case 1:
                        Tablas.insertar_data()
                        print("Datos registrados exitosamente") 
                    case 2:
                        Tablas.mostrar_tabla()
                    case 3:
                        break 
                    case _:
                        print("Ingrese una opción Valida.")
                    