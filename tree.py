from node import Node

class Tree:
    root = None

    def add_value(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.add_node(val)

    def to_string(self):
        self.root.traverse()

    def search_n(self, n):
        return (self.root.search(n))