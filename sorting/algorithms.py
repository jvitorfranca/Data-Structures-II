import tools
import time
import numpy as np

class Algorithms():
    execution_time = -1

    def __init__(self, list):
        self.list = list

    def InsertSort(self):

        start_time = time.time()

        arr = np.array(self.list, dtype=int)

        print(arr)

        for i in range(1, arr.size):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

        self.execution_time = time.time() - start_time

        return arr, self.execution_time

    def SelectionSort(self):

        start_time = time.time()

        arr = np.array(self.list, dtype=int)

        print(arr)

        for j in range(0, arr.size - 1):
            min = j
            for i in range(j + 1, arr.size):
                if arr[i] < arr[min]:
                    min = i
            if min != j:
                arr[j], arr[min] = arr[min], arr[j]

        self.execution_time = time.time() - start_time

        return arr, self.execution_time
