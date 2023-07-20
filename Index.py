from MenuComidas import crearMenu
from Calculadora import calcularPrecio
import Auxiliares

#------------------------------PROGRAMA PRINCIPAL------------------------------
def programaPrincipal():
    
    diccionarioComidasporTipo, nombresTodasComidas, nombresEspeciales, NombreyPrecioTodos = crearMenu()
    
    print("Bienvenido al menu de comidas, tenemos las siguientes: \n")
    
    Auxiliares.mostrarComidas(diccionarioComidasporTipo)

    print("¿Desea hacer un pedido?, s/n")
  
    hacePedido = Auxiliares.hacePedido()

    if(hacePedido == "S"):
        print("\n")
        misPedidos = Auxiliares.recibirTodosPedidos(nombresTodasComidas)
        print("\n----------El precio de su pedido se detalla a continuacion----------")
        totalPagar = calcularPrecio(misPedidos, NombreyPrecioTodos, nombresEspeciales)
        if(totalPagar > 0):
            print(f"\nTotal a pagar = ${'{:.2f}'.format(totalPagar)}")
            Auxiliares.seCompra(totalPagar)
        else:
            print("\nSe ingresaron mas de 100 platos de comida, por favor ingrese menos.")
    else:
        print("\n")
        Auxiliares.mensajeDespedida()


programaPrincipal()