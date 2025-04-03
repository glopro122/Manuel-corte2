from Nodo import Nodo

class Compra(Nodo):
    def __init__(self, data, id_producto, id_proveedor, fecha_compra, cantidad):
        super().__init__(data)
        self.id_producto = id_producto
        self.id_proveedor = id_proveedor
        self.fecha_compra = fecha_compra
        self.cantidad = cantidad

    def __repr__(self):
        return f"Compra({self.data}, {self.id_producto}, {self.id_proveedor}, {self.fecha_compra}, {self.cantidad})"