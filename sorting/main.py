import sys
import time
import tools
from algorithms import Algorithms


def main(argv):

    list = []

    list = tools.create_random_integers(list, 10000, 'descending')

    sort = Algorithms(list)

    arr, execution_time = sort.SelectionSort()

    print(arr)
    print("execution time (Selection): ", "%.5f" % execution_time)

    arr, execution_time = sort.InsertSort()

    print(arr)
    print("execution time (Insertion): ", "%.5f" % execution_time)

    arr, execution_time = sort.CountingSort()

    print(arr)
    print("execution time (Counting): ", "%.5f" % execution_time)

    arr, execution_time = sort.RadixSort()

    print(arr)
    print("execution time (Radix): ", "%.5f" % execution_time)

if __name__ == "__main__":
    main(sys.argv)
