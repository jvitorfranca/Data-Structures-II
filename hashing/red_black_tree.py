BLACK = 'black'
RED = 'red'

class Node:
    def __init__(self, value=None, left=None, right=None, parent=None, color=RED):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

    def __str__(self):
        return str(self.value.getVal()) + str(self.color) + "\n"

    
class RedBlackTree:
    def __init__(self, root=None):
        self.__root = None
        
    def BSTInsert(self, value, comp):
        if self.__root is None:
            self.__root = Node(value, color=BLACK)
            return self.__root
        else:
            aux = self.__root
            while aux is not None:
                aux2 = aux
                if comp(aux.value.getVal(), value.getVal()) != -1:
                    aux = aux.left
                else:
                    aux = aux.right
                    
            if comp(aux2.value.getVal(), value.getVal()) != -1:
                aux2.left = Node(value, parent=aux2)
                return aux2.left
            else:
                aux2.right = Node(value, parent=aux2)
                return aux2.right
    
    def fixInsertion(self, node):
        parent_nd = None
        grand_parent_nd = None

        while (node != self.__root) and (node.color is not BLACK) and (node.parent.color is RED):
            parent_nd = node.parent
            grand_parent_nd = parent_nd.parent

            if node.parent == grand_parent_nd.left:
                uncle_nd = grand_parent_nd.right

                if uncle_nd is not None and uncle_nd.color is RED:
                    grand_parent_nd.color = RED
                    parent_nd.color = BLACK
                    uncle_nd.color = BLACK
                    node = grand_parent_nd
                else:
                    if node == parent_nd.right:
                        self.rotateLeft(parent_nd)
                        node = parent_nd
                        parent_nd = node.parent

                    self.rotateRight(grand_parent_nd)
                    aux = parent_nd.color
                    parent_nd.color = grand_parent_nd.color
                    grand_parent_nd.color = aux
                    node = parent_nd
            else:
                uncle_nd = grand_parent_nd.left

                if uncle_nd is not None and uncle_nd.color is RED:
                    grand_parent_nd.color = RED
                    parent_nd.color = BLACK
                    uncle_nd.color = BLACK
                    node = grand_parent_nd
                else:
                    if node == parent_nd.left:
                        self.rotateRight(parent_nd)
                        node = parent_nd
                        parent_nd = node.parent

                    self.rotateLeft(grand_parent_nd)
                    aux = parent_nd.color
                    parent_nd.color = grand_parent_nd.color
                    grand_parent_nd.color = aux
                    node = parent_nd

        self.__root.color = BLACK
        
    def rotateLeft(self, node):
        nd_right = node.right
        node.right = nd_right.left

        if node.right is not None:
            node.right.parent = node

        nd_right.parent = node.parent

        if node.parent is None:
            self.__root = nd_right
        elif node == node.parent.left:
            node.parent.left = nd_right
        else:
            node.parent.right = nd_right

        nd_right.left = node
        node.parent = nd_right

    def rotateRight(self, node):
        nd_left = node.left
        node.left = nd_left.right

        if node.left is not None:
            node.left.parent = node

        nd_left.parent = node.parent

        if node.parent is None:
            self.__root = nd_left
        elif node == node.parent.left:
            node.parent.left = nd_left
        else:
            node.parent.right = nd_left

        nd_left.right = node
        node.parent = nd_left

    def insert(self, value, comp):
        newnode = self.BSTInsert(value, comp)

        self.fixInsertion(newnode)

    def __height(self, node):
        if node is None:
            return -1
        hl = 0
        hr = 0
        hl = self.__height(node.left)
        hr = self.__height(node.right)
        if hl > hr:
            return 1 + hl
        else:
            return 1 + hr
        
    def height(self):
        return self.__height(self.__root)

    def __preOrder(self, node):
    	if node:
    		print("%d -> %s" % (node.value, node.color))
    		self.__preOrder(node.left)
    		self.__preOrder(node.right)

    def preOrder(self):
    	return self.__preOrder(self.__root)
        
    def search(self, key, comp):
        aux = self.__root
        while aux is not None:
            if comp(aux.value.getVal(), key) == 0:
                return aux.value
            if comp(aux.value.getVal(), key) == 1:
                aux = aux.left
            else:
                aux = aux.right

    def __invertedIndex(self, node):
        if node is None:
            return
        self.__invertedIndex(node.left)
        print(node.value)
        self.__invertedIndex(node.right)

    def invertedIndex(self):
        if self.__root is None:
            print("Árvore Vazia")
            return None
        self.__invertedIndex(self.__root)