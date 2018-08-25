import sys
import random
import time
import resource

def how_to_use():
    print('------------------------------------------------------')
    print(' Example: python3 main.py -a insert -q 1000 -m random ')
    print('------------------------------------------------------')

def main(argv):
    #defining our initial time
    time.start = time.clock()

    list = []

    #generating random numbers without repeats
    list = random.sample(range(100), 15)

    #calculating the time used to process the algorithms
    time_elapsed = (time.clock() - time.start)

    print(list)
    print("loading time: ", time_elapsed)
    print("resource used", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

if __name__ == "__main__":
    main(sys.argv)
