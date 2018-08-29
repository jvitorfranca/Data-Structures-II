import random


def how_to_use():

    print('------------------------------------------------------')
    print(' Example: python3 main.py -a insert -q 1000 -m random ')
    print('------------------------------------------------------')


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
