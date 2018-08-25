import sys
import random
import time
import resource

def how_to_use():
    print('------------------------------------------------------')
    print(' Example: python3 main.py -a insert -q 1000 -m random ')
    print('------------------------------------------------------')

#generating random numbers without repeats
def create_random_integers(my_list, elements, method):

    if method == 'random':
        my_list = random.sample(range(elements), elements)

    elif method == 'ascending':
        for i in range(1, elements):
            my_list.append(i)

    elif method == 'descending':
        for i in range(elements, 1, -1):
            my_list.append(i)

    return my_list

def main(argv):
    #defining our initial time
    time.start = time.clock()

    list = []

    list = create_random_integers(list, 100, 'descending')

    #calculating the time used to process the algorithms
    time_elapsed = (time.clock() - time.start)

    print(list)
    print("loading time: ", time_elapsed)
    print("resource used", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

if __name__ == "__main__":
    main(sys.argv)
