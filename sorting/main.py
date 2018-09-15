import argparse, sys
import time
import tools
from algorithms import Algorithms


def main(argv):

    # Creating an argument parser
    parser = argparse.ArgumentParser()

	# Arguments used in this project
	parser.add_argument('-a', '--algorithm')
	parser.add_argument('-s', '--size')
	parser.add_argument('-m', '--method')

    # Saving the arguments
    args = parser.parse_args()

    if args.algorithm is None:
        print('Choose a algorithm: ')

        print('-InsertSort')
        print('-SelectionSort')
        print('-ShellSort')
        print('-QuickSort')
        print('-MergeSort')
        print('-HeapSort')
        print('-CountSort')
        print('-RadixSort')

        tools.how_to_use()
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv)
