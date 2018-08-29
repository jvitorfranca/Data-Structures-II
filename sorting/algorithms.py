import tools
import numpy as np

'''Insert Sort'''
list = []

list = tools.create_random_integers(list, 100, 'descending')

arr = np.array(list, dtype=int)

print(arr)

for i in range(1, arr.size):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        aux = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = aux
        j -= 1

print(arr)
