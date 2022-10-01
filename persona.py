class persona():
    #metodo constructor
    def __init__(self,numero, nombre, direccion):
        self.numero=numero
        self.nombre=nombre
        self.direccion=direccion

    #creacion de GETTERS
    def vernumero(self):
        return self.numero

    def vernombre(self):
        return self.nombre

    def verdireccion(self):
        return self.direccion

    #creacion de SETTERS
    def modificarnumero(self, nuevonumero):
        self.numero= nuevonumero

    def modificarnombre(self, nuevonombre):
        self.nombre= nuevonombre

    def modificardireccion(self, nuevodireccion):
        self.direccion= nuevodireccion
