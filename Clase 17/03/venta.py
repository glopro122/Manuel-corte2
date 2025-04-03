class Venta:
    def __init__(self, id_venta, id_producto, id_cliente, fecha_venta, cantidad):
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.fecha_venta = fecha_venta
        self.cantidad = cantidad

    def __repr__(self):
        return f"Venta({self.id_venta}, {self.id_producto}, {self.id_cliente}, {self.fecha_venta}, {self.cantidad})"