import random
import sys


# Alert the user if he/she inserted a unexpected algorithm
def error(algorithm):
    print(algorithm + ' is not valid.')
    print('Avaliable algorithms: ')
    print('-InsertSort')
    print('-SelectSort')
    print('-ShellSort')
    print('-QuickSort')
    print('-MergeSort')
    print('-HeapSort')
    print('-CountSort')
    print('-RadixSort')

# Teaches how to use the code
def how_to_use():

    print('---------------------------------------------------------')
    print(' Example: python3 main.py -a InsertSort -s 100 -m random ')
    print('---------------------------------------------------------')

# Generate a list with properties given
def create_random_integers(my_list, elements, method):

    if elements > 0 and elements <= 1000000:

        if method == 'random':
            my_list = random.sample(range(elements), elements)

        elif method == 'ascending':
            for i in range(1, elements):
                my_list.append(i)

        elif method == 'descending':
            for i in range(elements, 1, -1):
                my_list.append(i)

        else:
            print('Please, insert a valid method')

    else:

        print('Please, insert a size between 0 and 1000000')

        tools.how_to_use()
        sys.exit(2)

    return my_list
