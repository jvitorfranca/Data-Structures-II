import sys
import time
import tools
import numpy as np
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

    arr, execution_time = sort.ShellSort()

    print(arr)
    print("execution time (Shell): ", "%.5f" % execution_time)

    #array = np.array(list)
    arr, execution_time = sort.MergeSort(list)

    print(arr)
    print("execution time (Merge): ", "%.5f" % execution_time)

    #array = np.array(list)

    arr, execution_time = sort.HeapSort(list)

    print(arr)
    print("execution time (Heap): ", "%.5f" % execution_time)

if __name__ == "__main__":
    main(sys.argv)
