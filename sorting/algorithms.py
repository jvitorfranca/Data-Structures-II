import tools
import numpy as np

class Algorithms():
    def __init__(self, list):
        self.list = list

    def InsertSort(self):

        arr = np.array(self.list, dtype=int)

        print(arr)

        for i in range(1, arr.size):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

        return arr
