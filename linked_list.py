 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    def add_elem(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            yield f'{current.value} ->'
            current = current.next
        return None
    
    def eliminar(self, elem):
        current = self.head
        prev = None
        if not current:
            return
        if current.value == elem:
            self.head = current.next
            return
        
        while current:
            if current.value == elem:
                prev.next = current.next
            prev = current
            current = current.next

# forma mas sencilla con recursividad 

class Node1:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def add_node(self, valor):
        if self.next:
            self.next.add_node(valor)
        else:
            self.next = Node1(valor)  

    def listar(self):
        if self.next:
            prev = self.next.listar()
        else:
            return self.valor
        return f'{self.valor} {prev}'
    
    def size(self):
        return 1 + self.next.size() if self.next else 1
        
    def delete(self):
        if not self.next:
           return None
        else:
            current = self
            while current.next.next:
                current = current.next
        current.next = None
        return self
        
if __name__ == "__main__":            
    l1 = Linked_list()
    l1.add_elem(2)
    l1.add_elem(4)
    l1.add_elem(5)
    l1.add_elem(6)
    l1.eliminar(2)
    for i in l1.display():
        print(i)

    n = Node1(1)
    n.add_node(3)
    n.add_node(4)
    n.add_node(8)
    print(n.listar())
    print(f"El contador es {n.size()}")
    n.delete()
    print(n.listar())
