from MenuComidas import crearMenu
diccionarioFinal, todasComidas, todasEspeciales, todosPrecios = crearMenu()


def calcularPrecio(misPedidos, todosPrecios, comidasEspeciales):
    #valores iniciales
    tamanioPedido = 0
    precioInicial = 0
    cantidadDeEspeciales = 0
    recargoPorEspeciales = 0
    
    #Imprime la lista del pedido
    for pedido in misPedidos:
        nombre = pedido[0]
        cantidad = pedido[1]
        precioUnitario = todosPrecios.get(nombre.lower())

        print(f"Comida: {nombre}, cantidad: {cantidad}, precio unitario: ${todosPrecios.get(nombre.lower())}")
        precioInicial = precioInicial + (precioUnitario*cantidad)
        tamanioPedido = tamanioPedido + cantidad

        if(nombre.lower() in comidasEspeciales):
            cantidadDeEspeciales = cantidadDeEspeciales + cantidad
            recargoPorEspeciales = recargoPorEspeciales + 0.05*(cantidad*precioUnitario)

    print(f"\nCantidad de comidas: {tamanioPedido}.  Precio base: ${'{:.2f}'.format(precioInicial)}.")

    if(tamanioPedido <= 100):
        
        #Se piden entre 5 y 10 comidas
        if((tamanioPedido > 5) and ( tamanioPedido <= 10)):
            precioInicial = precioInicial*0.9
            print(f"\nSe pidieron entre 5 y 10 comidas (-10%): ${'{:.2f}'.format(precioInicial)}")
        
        #Se piden mas de 10 comidas
        if((tamanioPedido > 10)):
            precioInicial = precioInicial*0.8
            print(f"\nSe pidieron mas de 10 comidas (-20%): ${'{:.2f}'.format(precioInicial)}")
        
        #El costo esta entre $50 y $100
        if((precioInicial > 50) and (precioInicial <= 100)):
            precioInicial = precioInicial-10
            print(f"\nCosto entre $50 y $100 (-10$): ${'{:.2f}'.format(precioInicial)}")

        #El costo es mayor a $100
        if(precioInicial > 100):
            precioInicial = precioInicial-25
            print(f"\nCosto mayor a $100 (-25$): ${'{:.2f}'.format(precioInicial)}")

        #Se pidieron platos especiales
        if(cantidadDeEspeciales>0):
            precioInicial = precioInicial+recargoPorEspeciales
            print(f"\nSe pidieron {cantidadDeEspeciales} platos especiales (+5% del valor de cada plato especial -> +{'{:.2f}'.format(recargoPorEspeciales)}): ${'{:.2f}'.format(precioInicial)}")

        return round(precioInicial, 2)

    else:
        return -1
    

calcularPrecio([["bandera", 2], ["hornado", 4], ["yapingacho", 4]], todosPrecios, todasEspeciales)
