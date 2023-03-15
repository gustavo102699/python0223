def main():
    evento = obtEvent()
    validar(evento)
    procesar(evento)

def obtEvent():
    evento = input("Evento: ")
   
    return evento

def validar(evento):
    listaeventos = ['Festival', 'Concierto','Cine', 'Viaje', "Campamento"]
    if evento not in listaeventos:
        raise ValueError("Evento inválido.")

def procesar(evento):
    print(f"Su evento es:{evento}")

main()