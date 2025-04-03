from Nodo import Nodo
from product import producto

class LinkedList:
    # Constructor de la clase LinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Método para agregar un nodo al final de la lista con el valor
    def add (self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            print (self.tail.data)  # Cambiar 'id' a 'data'

    # Método para agregar un nodo al final de la lista con un append
    def append(self, valor): 
        new_node = Nodo(valor)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Método para imprimir la lista
    def __str__(self):
        if self.head is None:
            return 'Lista vacia'
        else:
            current = self.head
            resultado = ""
            while current is not None:
                resultado += str(current) + " -> "
                current = current.next
            return resultado
        
    # Método para agregar un nodo al inicio de la lista
    def add_at_start(self, valor):
        current = Nodo(valor)
        current.next = self.head
        self.head = current

    # Método para eliminar un nodo de la lista
    def eliminar_nodo(self, valor):
        current = self.head
        previous = None
        while current is not None:
            if current.data == valor:  # Cambiar 'id' a 'data'
                if previous is None:
                    self.head = current.next  # Cambiar 'head' de la lista
                else:
                    previous.next = current.next
                del current
                return
            previous = current
            current = current.next  # Cambiar 'siguiente' a 'next'
        print("Valor no encontrado en la lista.")

    # Método para eliminar un nodo de la lista
    def delete_value(self, search_value):
        if self.head is None:
            return "Lista vacia"
        if self.head.data == search_value:  # Cambiar 'id' a 'data'
            self.head = self.head.next
        current = self.head
        while current is not None and current.next is not None:
            if current.next.data == search_value:  # Cambiar 'id' a 'data'
                current.next = current.next.next
            current = current.next
        return "Valor no encontrado en la lista."

    # Método para ordenar la lista
    # def ordenar_lista(self):
    #   if self.head is None:
    #        return
    #    current = self.head
    #    while current is not None:
    #        index = current.next
    #        while index is not None:   
    #            if current.data > index.data:  # Si el valor de current es mayor que el de index, se deben intercambiar los apuntadores
    #                # Intercambiar los apuntadores
    #                current.next, index.next = index.next, current.next
    #                if current == self.head:  # Si current es la cabeza, actualizamos la cabeza de la lista
    #                    self.head = index
    #                elif index == la cabeza, actualizamos la cabeza de la lista
    #                    self.head = current
    #            index = index.next
    #        current = current.next

    # Metodo para ordenar la lista de manera ascendete:
    def ordenar(self):
        prev_before = None
        current = self.head.next if self.head else None
        before = self.head
        while before and before.next is None:
            while current is not None:
                t_before = before
                t_current = current
                if before.price > current.price:  # "> a <": <--- Cambiar esta comparacion cambia el sentido del ordenamiento, sea de menor a mayor o de mayor a menor
                    next_before = before.next
                    before.next = current.next
                if next_before == current:
                    current.next = before
                else:
                    current.next = next_before
                    prev_current.next = t_before
                if prev_before is None:
                    prev_before.next = current
                else:
                    self.head = current
                current = t_before
                before = t_current
                print(self)
                prev_current = current
                current = current.next
            prev_before = before
            before = before.next
            current = before.next

    # Metodo para buscar en la lista una id: 
    def buscar_id(self, id):
        if self.head is None:
            return"Lista vacia"
        else: 
            current = self.head
            while current is not None:
                if current.data == id:  # Cambiar 'id' a 'data'
                    return "Producto encontrado: " + str(current)
                current = current.next
            return "Producto no encontrado"
    
    # Metodo para buscar un atributo en la lista, recibe el nombre del atributo y el valor a buscar:
    def buscar_atributo(self, attributo, valor):
        if self.head is None:
            return "Lista vacia"
        else:
            current = self.head
            while current is not None:
                if getattr(current, attributo) == valor:
                    return "Valor encontrado: " + str(current)
                current = current.next
        return "Valor no encontrado en la lista"

# Ejemplo de uso
LinkedList1 = LinkedList()

# Instancias de los productos para su uso en la lista
Product1 = producto(1,"Laptop", 10)
Product2 = producto(2,"Mouse", 5)
Product3 = producto(3,"Teclado", 15)
product4 = producto(4,"Monitor", 20)

# Ejemplos de uso por funcion:
LinkedList1.add(Product1)  # Utilizando el metodo add
LinkedList1.add(Product2)
LinkedList1.add(Product3)
LinkedList1.add(product4)
print("Lista original:")
print(LinkedList1)
print("---------------------------------------------------------------------------------------------------------------------------")
LinkedList1.ordenar()  # Utilizando el metodo ordenar
print("Lista ordenada:")
print(LinkedList1)
LinkedList1.delete_value(2)  # Utilizando el metodo delete_value
print("---------------------------------------------------------------------------------------------------------------------------")
print(LinkedList1.buscar_atributo("name", "Teclado"))  # Utilizando el metodo buscar_atributo
print("---------------------------------------------------------------------------------------------------------------------------")
print(LinkedList1.buscar_id(3))  # Utilizando el metodo buscar_id