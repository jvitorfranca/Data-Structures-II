import sys
import time
import tools
from algorithms import Algorithms


def main(argv):

    start_time = time.time()

    list = []

    list = tools.create_random_integers(list, 100, 'descending')

    sort = Algorithms(list)

    arr = sort.InsertSort()

    #arr = algorithms.InsertSort(list)

    execution_time = time.time() - start_time

    print(arr)
    print("loading time: ", "%.5f" % execution_time)

if __name__ == "__main__":
    main(sys.argv)
