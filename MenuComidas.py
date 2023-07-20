from Comida import Comida

def diccionarioTotal(dicc1, dicc2):
    mezcla = {**dicc1, **dicc2}
    return mezcla


def listaTodasComidas(diccionarioTotal):
    resultado = []
    for valor1 in diccionarioTotal.values():
        for valor2 in valor1:
            resultado.append(valor2.getNombre().lower())
    return resultado


def listaEspeciales(diccionarioEspeciales):
    resultado = []
    for valor1 in diccionarioEspeciales.values():
        for valor2 in valor1:
            resultado.append(valor2.getNombre().lower())
    return resultado


def todasComidasyPrecios(diccionarioTotal):
    diccionarioNuevo = {}

    for valor1 in diccionarioTotal.values():
        for valor2 in valor1:
            diccionarioNuevo[valor2.getNombre().lower()] = valor2.getPrecio()

    return diccionarioNuevo

    
def crearMenu():
    diccionarioComidas = {"Platos fuertes":[], "Sopas y caldos":[], "Postres":[]}
    diccionarioEspeciales = {"Especiales del chef":[]}

    #----------COMIDAS CRIOLLAS----------
    arregloCriollo = diccionarioComidas.get("Platos fuertes")
    arregloCriollo.append(Comida("yapingacho", 5))
    arregloCriollo.append(Comida("menestra de frejol", 5))
    arregloCriollo.append(Comida("sango de verde", 5))

    #----------SOPAS Y CALDOS----------
    arregloSopas = diccionarioComidas.get("Sopas y caldos")
    arregloSopas.append(Comida("locro de choclo", 5))
    arregloSopas.append(Comida("caldo de mondongo", 5))
    arregloSopas.append(Comida("caldo de gallina criolla", 5))

    #----------POSTRES----------
    arregloPostres = diccionarioComidas.get("Postres")
    arregloPostres.append(Comida("torta tres leches", 5))
    arregloPostres.append(Comida("torta de naranja", 5))
    arregloPostres.append(Comida("tatido de galletas oreo", 5))

    #----------ESPECIALES DEL CHEF----------
    arregloChef = diccionarioEspeciales.get("Especiales del chef")
    arregloChef.append(Comida("pierna de cerdo al horno",7 ))
    arregloChef.append(Comida("bandera", 8))
    arregloChef.append(Comida("hornado", 7))

    diccionarioFinal = diccionarioTotal(diccionarioComidas, diccionarioEspeciales)
    todasComidas = listaTodasComidas(diccionarioFinal)
    todasEspeciales = listaEspeciales(diccionarioEspeciales)
    todosPrecios = todasComidasyPrecios(diccionarioFinal)

    return diccionarioFinal, todasComidas, todasEspeciales, todosPrecios