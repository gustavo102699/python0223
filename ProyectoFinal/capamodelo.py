import pandas as pd
import sqlite3
conn=sqlite3.connect('demo.db')
cur=conn.cursor()
url="C:\Users\gus26\Desktop\WKPythonDatux\python0223\ProyectoFinal\Ventas2023.csv"
df= pd.read_csv(url)
class Ventas2023:    
    def MostrarVenta():
        print(df)
    def TiposDatos():
        print(df.dtypes)
    def NuevaColumna():
        data=input ("Ingrese columna: ")
        df['Nueva columna']= data
        print(df.head())
class Tablas:
    def crear_table():              
        cur.execute("CREATE TABLE IF NOT EXISTS VENTAS2024 (Producto TEXT,Venta INTERGER)")
        conn.commit()

    def insertar_data():
            cantdatos= int(input("Ingrese la cantidad de datos a registrar: "))            
            for i in range(cantdatos):
                producto=input("Ingrese producto vendido: ")
                nventa= int(input("Ingrese ventas: "))
                cur.execute("insert into VENTAS2024 values(?,?)"),(producto,nventa)
                conn.commit()

    def mostrar_tabla():
            cur.execute("SELECT * FROM VENTAS2024")
            x= cur.fetchall()            
            for i in x:
                 print(i)
                 


            

       