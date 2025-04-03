from Nodo import Nodo

class producto (Nodo):
  def _init_(self,data,name,price):
    super()._init_(data)
    self.name=name
    self.price=price
    self.next=None

  def _str_(self):
    return f"id_producto:{self.data} Producto:{self.data}, Price:{self.price}"