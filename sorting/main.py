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

    # Check if the user specified a algorithm
    if args.algorithm is None:
        print('Insert a algorithm: ')

        # Possible algorithms
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

    # Check if the user specified a lenght to the array
    if args.size is None:
        print('Insert a length to generate a array')

        tools.how_to_use()
        sys.exit(2)

    # Check if the user specified a method to generate the array
    if args.method is None:
        print('Insert a method to generate the array')

        # Possible methods
        print('ascending')
        print('descending')
        print('random')

        tools.how_to_use()
        sys.exit(2)

    return args

def run_algorithms(list, algorithm):

    # Creating a sort object
    sort = Algorithms(list)

    if algorithm == 'insertionsort' or algorithm == 'insertsort':
        return sort.InsertSort()

    elif algorithm == 'selectionsort' or algorithm == 'selectsort':
        return sort.SelectSort()

    elif algorithm == 'countingsort' or algorithm == 'countsort':
        return sort.CountSort()

    elif algorithm == 'shellsort':
        return sort.ShellSort()

    elif algorithm == 'quicksort':
        return sort.QuickSort(list, 0, len(list))

    elif algorithm == 'mergesort':
        return sort.MergeSort(list)

    elif algorithm == 'heapsort':
        return sort.HeapSort(list)

    elif algorithm == 'radixsort':
        return sort.RadixSort()

    else:
        tools.error(algorithm)
        sys.exit(2)

if __name__ == "__main__":

    # User's arguments
    arguments = main(sys.argv[1:])

    # Preparing the arguments to be used
    algorithm = arguments.algorithm.lower()

    size = arguments.size

    method = arguments.method.lower()

    size = int(size)

    list = []

    list = tools.create_random_integers(list, size, method)

    arr, execution_time = run_algorithms(list, algorithm)

    print(arr)
    print("execution time: ", "%5f" % execution_time)
