class Nodo:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Este es el dato: "+ str(self.data)
nodo = Nodo(3)
print(nodo)