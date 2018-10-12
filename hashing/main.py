# Second implementation
# Autor: jvitorfranca
# Using hashing and red-black trees

import red_black_tree as rb

def comp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0

tree = rb.RedBlackTree()

tree.insert(12, comp)
tree.insert(15, comp)
tree.insert(10, comp)
tree.insert(11, comp)
tree.insert(19, comp)

tree.preOrder()