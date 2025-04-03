from Nodo import Nodo

class producto(Nodo):
    def __init__(self, data, name, price):
        super().__init__(data)
        self.name = name
        self.price = price
        self.next = None

    def __str__(self):
        return f"id_producto: {self.data} Producto: {self.name}, Price: {self.price}"