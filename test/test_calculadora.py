import pytest
from Calculadora import calcularPrecio
from MenuComidas import crearMenu

diccionarioFinal, todasComidas, todasEspeciales, todosPrecios = crearMenu()

def test_calcularPrecio():
    assert calcularPrecio([["bandera", 2], ["hornado", 4], ["yapingacho", 2]], todosPrecios, todasEspeciales) == 50.80
    assert calcularPrecio([["bandera", 30], ["hornado", 30], ["yapingacho", 30], ["locro de choclo", 30]], todosPrecios, todasEspeciales) == -1
    assert calcularPrecio([["bandera", 30], ["yapingacho", 30], ["locro de choclo", 30]], todosPrecios, todasEspeciales) == 419.00

 