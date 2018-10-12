# Second implementation
# Autor: jvitorfranca
# Using hashing and red-black trees

import red_black_tree as rb
import utilities as util

tree = rb.RedBlackTree()

tree.insert(12, util.comp)
tree.insert(15, util.comp)
tree.insert(10, util.comp)
tree.insert(11, util.comp)
tree.insert(19, util.comp)

num_files = int(input("Inform how much files you're going to submit: "))
print(num_files)

files = []

for i in range(num_files):
	id_file = input("Insert file %d name: " % (i+1))
	file = open(id_file, "r")
	files.append(file.readline())
	file.close()

for j in files:
	print(j)
