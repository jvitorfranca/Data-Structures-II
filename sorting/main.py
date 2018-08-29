import sys
import time
import tools
import algorithms


def main(argv):

    start_time = time.time()

    list = []

    list = tools.create_random_integers(list, 100, 'descending')

    arr = algorithms.InsertSort(list)

    execution_time = time.time() - start_time

    print(arr)
    print("loading time: ", "%.5f" % execution_time)

if __name__ == "__main__":
    main(sys.argv)
