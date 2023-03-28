from datetime import datetime
from main import Registro

objeto = Registro()
fecha = datetime.now()
objeto.guardar(fecha.strftime('%d/%m/%Y %H:%M:%S')+ " TEXTO GUARDADO\n")
objeto.mostrar()
