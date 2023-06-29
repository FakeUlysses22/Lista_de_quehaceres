#
opcion = "nose"
datos = list()

def menu():
    print("Bienvenido a lista de que hacer")
    print("Opciones: ")
    print("")
    print("1.Añadir elemento a la lista")
    print("2.Borrar lista")
    print("3.Ver lista")
    print("4.Cerrar")
    

while opcion != 4:
    menu()
    print("")
    opcion = int(input("Inserte su opcion: "))

    if opcion == 1:
     elemento = input("inserte elemento: ")
     datos.append(elemento)
     print("elemento añadido:", elemento)
     print("")
    elif opcion == 2:
     print("Lista borrada")
     datos = []
     print("")
    elif opcion == 3:
        print("Esta es su lista estimado:")
        print("")
        print(datos)
        print("")
    elif opcion == 4:
        print("")
        print("Adios")
        
    else:
        print("")
        print("Dato invalido")
        print("Rompiste la matrix")
        print("")
