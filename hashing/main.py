import sys
import time
import red_black_tree as rb
import utilities as ut


def main(argv):

	words = ut.loadWords(argv[1:])

	# tad = ut.loadRedBlackTree(words)
	# tad.invertedIndex()

	tad = ut.loadHashTable(words)
	tad.invertedIndex(words)

if __name__ == "__main__":
	main(sys.argv)