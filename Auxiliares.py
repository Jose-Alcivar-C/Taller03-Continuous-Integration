def hacePedido():

    hacePedido = "N"

    while(True):
    
        pedir = input("Ingrese su eleccion: ")

        try:
            if( str(pedir).upper() == "S"):
                hacePedido = "S"
                break
            elif( str(pedir).upper() == "N" ):
                hacePedido = "N"
                break
            else:
                print("Eleccion erronea, intente nuevamente")
        except:
            print("ingrese un texto (S o N)")
    
    return hacePedido


def mensajeDespedida():
    print("Gracias por usar el sistema")


def mostrarComidas(diccionarioComidasporTipo):
    for valor1 in diccionarioComidasporTipo.keys():
        print(f"----------{valor1.upper()}----------")
        for valor2 in diccionarioComidasporTipo.get(valor1):
            print(valor2)
        print("\n")


def recibirUnPedido(nombresTodasComidas):
    
    comida = ""
    cantidad = 0
    while(True):
        comida = input("Ingrese nombre de la comida: ")
        if(comida.lower() in nombresTodasComidas):
            break
        else:
            print("comida no valida, ingrese nuevamente")
    
    while(True):
        try:
            cantidad = int(input("Ingrese cantidad de platos: "))
            if(int(cantidad) >= 1):
                break
            else:
                print("cantidad debe ser mayor o igual a 1")
        except:
            print("debe ingresar un valor numerico entero")
    
    return [comida.capitalize(), cantidad]


def recibirTodosPedidos(nombresTodasComidas):
    pedidos = []
    pedido = recibirUnPedido(nombresTodasComidas)
    pedidos.append(pedido)
    
    print("\nDesea seguir pidiendo?, s/n")

    while(True):
        sigue = input("Ingrese su eleccion: ")
        
        if( str(sigue).upper() == "S"):
            print("\n")
            pedido = recibirUnPedido(nombresTodasComidas)
            pedidos.append(pedido)
            print("\nDesea seguir pidiendo?, s/n")
        elif( str(sigue).upper() == "N" ):
            break
        else:
            print("Eleccion erronea, intente nuevamente")

    return pedidos


def seCompra(totalPagar):
    while(True):
        comprar = input("\n¿Confirmar pedido?: s/n ")
        try:
            if( str(comprar).upper() == "S" ):
                print(f"\nSe ha registrado su compra de ${'{:.2f}'.format(totalPagar)}, pronto le informaremos para que pueda retirarla")
                print("\n")
                mensajeDespedida()
                break
            elif( str(comprar).upper() == "N" ):
                print("Compra cancelada.")
                print("\n")
                mensajeDespedida()
                break
            else:
                print("\nSeleccion incorrecta, por favor escoja una opcion valida")
        except:
            print("\nIngrese un texto, S o N")