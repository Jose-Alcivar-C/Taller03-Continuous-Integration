import pytest
from Calculadora import calcularPrecio 
from MenuComidas import crearMenu
from Comida import Comida

diccionarioFinal, todasComidas, todasEspeciales, todosPrecios = crearMenu()

def test_calcularPrecio(): 
    assert calcularPrecio([["bandera", 2], ["hornado", 4], ["yapingacho", 2]], todosPrecios, todasEspeciales) == 50.80
    assert calcularPrecio([["bandera", 30], ["hornado", 30], ["yapingacho", 30], ["locro de choclo", 30]], todosPrecios, todasEspeciales) == -1
    assert calcularPrecio([["bandera", 30], ["yapingacho", 30], ["locro de choclo", 30]], todosPrecios, todasEspeciales) == 419.00
    assert calcularPrecio([["bandera", 2], ["hornado", 4], ["yapingacho", 4]], todosPrecios, todasEspeciales) ==  49.80

def test_Comida():
    #comidas
    comida1 = Comida("Moro", 5)
    comida2 = Comida("Asado", 6)
    
    #arrego de comidas
    arreglo_comidas = []
    arreglo_comidas.append(comida1)
    arreglo_comidas.append(comida2) 
    
    #imprimir comida1
    assert print(comida1) == None
    #imprimir comida2
    assert print(comida2) == None
    #imprimir arreglo de comida
    assert print(arreglo_comidas) == None