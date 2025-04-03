class Compra:
    def __init__(self, id_compra, id_producto, id_proveedor, fecha_compra, cantidad):
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.id_proveedor = id_proveedor
        self.fecha_compra = fecha_compra
        self.cantidad = cantidad

    def __repr__(self):
        return f"Compra({self.id_compra}, {self.id_producto}, {self.id_proveedor}, {self.fecha_compra}, {self.cantidad})"