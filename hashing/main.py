# Inverted Index implementation
# Author: João Vitor Ferreira França

import os
import psutil
import sys
import time
import utilities as ut


def main(argv):

	print("------------- Search Engine ------------\n")
	print("-- Insert the ADT to treat collisions --\n")

	option = int(input("1. RedBlack Tree\n2. Linear Probing\n3. Quadratic Probing\n"))

	# Parameter to count the time spent
	execution_time = 0

	# Getting the memory informations
	process = psutil.Process(os.getpid())

	mem_initial = process.memory_info().rss / float(2 ** 20)

	# Defining which ADT the program will run
	if option == 1:

		# Just a flag to know what ADT will be used
		tad_type = "redblack"
		start_time = time.process_time()

		# Loading the words from the initial files
		words = ut.loadWords(argv[1:])

		# Loading our ADT
		tad = ut.loadRedBlackTree(words)

		# Calculating the inverted index
		tad.invertedIndex()

		# Calculating the time spent
		execution_time = time.process_time() - start_time

		print("Execution time ", execution_time)

		mem_final = process.memory_info().rss / float(2 ** 20)

		print("Memory used: ", "%5f" % (mem_final - mem_initial))

	elif option == 2:

		tad_type = "hash"
		start_time = time.process_time()

		# Loading the words from the initial files
		words = ut.loadWords(argv[1:])

		# Loading our ADT
		tad = ut.loadHashTable(words, 'linear')

		# Calculating the inverted index
		tad.invertedIndex(words)

		# Calculating the time spent
		execution_time = time.process_time() - start_time
		print("Execution time ", execution_time)

		mem_final = process.memory_info().rss / float(2 ** 20)

		print("Memory used: ", "%5f" % (mem_final - mem_initial))

	elif option == 3:

		tad_type = "hash"
		start_time = time.process_time()

		# Loading the words from the initial files
		words = ut.loadWords(argv[1:])

		# Loading our ADT
		tad = ut.loadHashTable(words, 'quadratic')

		# Calculating the inverted index
		tad.invertedIndex(words)

		# Calculating the time spent
		execution_time = time.process_time() - start_time
		print("Execution time ", execution_time)

		mem_final = process.memory_info().rss / float(2 ** 20)

		print("Memory used: ", "%5f" % (mem_final - mem_initial))

	else:
		# If the user did not choose a valid ADT
		print("Error, you must choose a valid input")
		sys.exit(2)

	# Search method
	while True:

		option = int(input("1. IDF\n2. Exit\n"))

		if option == 2:
			sys.exit()
		elif option == 1:
			start_time = time.process_time()

			# Calculating the Inverse Document Frequency
			ut.IDF(argv[1:], tad, tad_type)
			
			# Calculating the time spent
			execution_time = time.process_time()
			print("Time to IDF: ", execution_time, start_time)

			mem_final = process.memory_info().rss / float(2 ** 20)

			print("Memory used: ", "%5f" % (mem_final - mem_initial))

if __name__ == "__main__":
	main(sys.argv)