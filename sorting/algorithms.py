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

    def CountingSort(self):

        start_time = time.time()

        arr = np.array(self.list, dtype=int)

        print(arr)

        max = arr.max() + 1

        count = [0] * max

        for j in arr:
            count[j] += 1

        i = 0
        for j in range(max):
            for k in range(count[j]):
                arr[i] = j
                i += 1

        self.execution_time = time.time() - start_time

        return arr, self.execution_time

    def RadixSort(self):

        start_time = time.time()

        RADIX = 10
        maxLength = False
        tmp , placement = -1, 1

        arr = np.array(self.list, dtype=int)

        print(arr)

        while not maxLength:
            maxLength = True
            # declare and initialize buckets
            buckets = [list() for _ in range( RADIX )]

            # split aList between lists
            for i in arr:
                tmp = i / placement
                buckets[int(tmp % RADIX)].append(i)
                if maxLength and tmp > 0:
                    maxLength = False

            # empty lists into aList array
            a = 0
            for b in range( RADIX ):
                buck = buckets[b]
                for i in buck:
                    arr[a] = i
                    a += 1

            # move to next digit
            placement *= RADIX

        self.execution_time = time.time() - start_time

        return arr, self.execution_time

    def ShellSort(self):

        start_time = time.time()

        arr = np.array(self.list, dtype=int)

        print(arr)

        n = arr.size

        gap = n/2

        while gap > 0:
            gap = int(gap)
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j-gap] > temp:
                    arr[j] = arr[j-gap]
                    j -= gap

                arr[j] = temp

            gap /= 2

        self.execution_time = time.time() - start_time

        return arr, self.execution_time
