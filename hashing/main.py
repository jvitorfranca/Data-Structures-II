import sys
import time
import red_black_tree as rb
import utilities as ut


def main(argv):

	option = int(input("1. RedBlack Tree\n2. Linear Probing\n3. Quadratic Probing\n"))

	execution_time = 0

	if option == 1:
		start_time = time.time()
		words = ut.loadWords(argv[1:])
		tad = ut.loadRedBlackTree(words)
		tad.invertedIndex()
		execution_time = time.time() - start_time
		print("Tempo de execução ", "%5f" % execution_time)
	elif option == 2:
		start_time = time.time()
		words = ut.loadWords(argv[1:])
		tad = ut.loadHashTable(words, 'linear')
		tad.invertedIndex(words)
		execution_time = time.time() - start_time
		print("Tempo de execução ", "%5f" % execution_time)
	elif option == 3:
		start_time = time.time()
		words = ut.loadWords(argv[1:])
		tad = ut.loadHashTable(words, 'quadratic')
		tad.invertedIndex(words)
		execution_time = time.time() - start_time
		print("Tempo de execução ", "%5f" % execution_time)
	else:
		print("Error")
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv)