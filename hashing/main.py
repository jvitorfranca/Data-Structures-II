import sys
import time
import red_black_tree as rb
import utilities as ut


def main(argv):

	words = ut.loadWords(argv[1:])

	choice = int(input("1. RedBlack Tree \n2. Linear Probing\n"))

	if choice == 1:
		tad = ut.loadRedBlackTree(words)
		tad.invertedIndex()
	elif choice == 2:
		tad = ut.loadHashTable(words)
		tad.invertedIndex(words)
	else:
		print("Invalid argument")
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv)