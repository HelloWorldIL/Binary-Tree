class Node:
    value = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val

    def add_node(self, val):
        if val < self.value:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.add_node(val)
        if val > self.value:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.add_node(val)

    def traverse(self):
        if self.left is not None:
            self.left.traverse()

        if self.value is not None:
            print(self.value)

        if self.right is not None:
            self.right.traverse()
    
    def search(self, n):
        if self.value == n:
            print("Match Found")
            return True
        elif n < self.value:
            if self.left is not None:
                self.left.search(n)
            else:
                print("No match was found")
                return False
        elif n > self.value:
            if self.right is not None:
                self.right.search(n)
            else:
                print("No match was found")
                return False
