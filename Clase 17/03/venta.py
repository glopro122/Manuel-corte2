from Nodo import Nodo
class Venta(Nodo):
    def __init__(self, id_venta, id_producto, id_cliente, fecha_venta, cantidad):
        super().__init__(id_venta)
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.fecha_venta = fecha_venta
        self.cantidad = cantidad

    def __str__(self):
        return f"Venta({self.id_venta}, {self.id_producto}, {self.id_cliente}, {self.fecha_venta}, {self.cantidad})"