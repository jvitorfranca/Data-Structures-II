import sys
import time
import tools
import random
import resource


def main(argv):

    #defining our reference of time
    time.start = time.clock()

    #our principal list
    list = []

    list = tools.create_random_integers(list, 100, 'descending')

    #calculating how long the algorithm worked
    time_elapsed = (time.clock() - time.start)

    #outputs
    print(list)
    print("loading time: ", time_elapsed)
    print("resource used", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

if __name__ == "__main__":
    main(sys.argv)
