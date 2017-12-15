from tree import Tree
from random import randint

test = Tree()

for x in range(20):
    test.add_value(randint(0, 100))

print(test.to_string())