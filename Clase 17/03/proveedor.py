from Nodo import Nodo
class proveedor(Nodo):
    def __init__(self, id, nombre, contacto, direccion):
        ssuper().__init__(id)
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

    def __repr__(self):
        return f"Proveedor({self.id}, {self.nombre}, {self.contacto}, {self.direccion})"