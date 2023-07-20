class Comida:

    def __init__(self, nombreComida, precio):
        self.nombreComida = nombreComida
        self.precio = precio
    
    def getNombre(self):
        return self.nombreComida

    def getPrecio(self):
        return self.precio     
    
    def __str__(self):
        return f"{self.nombreComida.capitalize()}, ${self.precio}"
    
    def __repr__(self):
        return str(self.__dict__)