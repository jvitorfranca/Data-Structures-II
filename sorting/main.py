import sys
import time
import tools
import numpy
import resource
import algorithms


def main(argv):

    start_time = time.time()

    list = []

    list = tools.create_random_integers(list, 100, 'descending')

    arr = algorithms.InsertSort(list)

    execution_time = time.time() - start_time

    print(arr)
    print("loading time: ", execution_time)
    print("resource used", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

if __name__ == "__main__":
    main(sys.argv)
