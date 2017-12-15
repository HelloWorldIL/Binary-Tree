from tree import Tree
from random import randint

test = Tree()

test.add_value(6)
test.add_value(3)
test.add_value(7)
test.add_value(2)
test.add_value(1)
test.add_value(8)

test.to_string()
print(test.search_n(10))