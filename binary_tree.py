class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def add_node(self, value: int) -> None:
        if self.root:
            self.root.add_node(value)
        else:
            self.root = NodeTree(value)
    
    def search_node(self, value) -> bool:
        if self.root:
            return self.root.search_node(value)
        else:
            return False
        
class NodeTree:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.rigth = None

    def add_node(self, value: int) -> None:
        if self.value > value:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = NodeTree(value)
        else:
            if self.rigth:
                self.rigth.add_node(value)
            else:
                self.rigth = NodeTree(value)
    
    def search_node(self, value: int) ->bool:
        if value == self.value:
            return True
        elif value > self.value:
            if self.rigth:
                return self.rigth.search_node(value)
            else:
                return False
        else:
            if self.left:
                return self.left.search_node(value)
            else:
                return False
            
if __name__ == "__main__":
    arr = [34,56,78,23,45,67]
    tree = Tree()
    for i in arr:
        tree.add_node(i)
    
    elem = 78
    print(tree.search_node(elem))