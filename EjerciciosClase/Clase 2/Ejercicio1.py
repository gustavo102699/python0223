while True:
    print("Menu")
    print("1) Dibujar un cuadrado")
    print("2) Multiplos de 2 en la lista")
    print("3) Mayores de edad de la lista")
    print("4) Exit")

    opc = (input("Digite una opción: "))

    if opc == "1":
        cuadrado = int(input("Ingrese el tamaño del cuadrado a dibujar: "))

        for i in range(cuadrado):
            for j in range(cuadrado):
                if i == 0 or i == cuadrado-1 or j == 0 or j == cuadrado-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    
    elif opc == "2":
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,14,16]
        for numero in lista:
            if numero % 2 == 0:
                print(numero)
    
    elif opc == "3":
        listpersonas = [["Gustavo", 20], ["Alejandro", 27], ["Antonio", 15], ["Jose", 18]]

        for persona in listpersonas:
            if persona[1] >= 18:
                print(persona[0])
    elif opc == "4":
        print("Adios")
        break
    else:
        print("Valor ingresado invalido")