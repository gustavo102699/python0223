biblioteca = {
    "Categorias": ["Drama", "Animado", "Acción", "Ficción", "Fabula" ],
    "Libros": {
        "La Divina Comedia": "Dante Alighieri",
        "El capital": "Karl Marx",
        "Cien años de soledad": "Gabriel García Márquez",
        "El principito": "Antoine de Saint-Exupéry"
        },
    "Prestamos": {},
    "Clientes": ["Jose", "Carlos", "Gustavo", "Antonio"]
}

print("Categorías:")
for categoria in biblioteca["Categorias"]:
    print("-" + categoria)

print("\nLibros y Autores:")
for libro, autor in biblioteca["Libros"].items():
    print(""f"{libro} escrito por: {autor}")

prestamolibro = "Cien años de soledad"
biblioteca["Prestamos"][prestamolibro] = "Gustavo"
print(f"\nSe ha prestado el libro {prestamolibro} a -> {biblioteca['Prestamos'][prestamolibro]}.")
print("\nClientes de la biblioteca:")
for usuario in biblioteca["Clientes"]:
    print(usuario)