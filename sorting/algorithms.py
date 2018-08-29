import tools
import numpy as np


def InsertSort(list):

    arr = np.array(list, dtype=int)

    print(arr)

    for i in range(1, arr.size):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr
