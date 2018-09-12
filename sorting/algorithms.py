import tools
import time
import numpy as np


class Algorithms():
    execution_time = -1

    def __init__(self, list):
        self.list = list

    def InsertSort(self):

        start_time = time.time()

        #arr = np.array(self.list, dtype=int)

        for i in range(1, len(self.list)):
            j = i
            while j > 0 and self.list[j-1] > self.list[j]:
                self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
                j -= 1

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def SelectionSort(self):

        start_time = time.time()

        #arr = np.array(self.list, dtype=int)

        for j in range(0, len(self.list) - 1):
            min = j
            for i in range(j + 1, len(self.list)):
                if self.list[i] < self.list[min]:
                    min = i
            if min != j:
                self.list[j], self.list[min] = self.list[min], self.list[j]

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def CountingSort(self):

        start_time = time.time()

        #arr = np.array(self.list, dtype=int)

        max = 0
        for i in range(0, len(self.list)):
            if self.list[i] > max:
                max = self.list[i]

        max = max + 1

        count = [0] * max

        for j in self.list:
            count[j] += 1

        i = 0
        for j in range(max):
            for k in range(count[j]):
                self.list[i] = j
                i += 1

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def RadixSort(self):

        start_time = time.time()

        RADIX = 10
        maxLength = False
        tmp , placement = -1, 1

        #arr = np.array(self.list, dtype=int)

        while not maxLength:
            maxLength = True
            # declare and initialize buckets
            buckets = [list() for _ in range( RADIX )]

            #for i in range(RADIX):
            #    buckets[i] = []

            # split aList between lists
            for i in self.list:
                tmp = i / placement
                buckets[int(tmp % RADIX)].append(i)
                if maxLength and tmp > 0:
                    maxLength = False

            # empty lists into aList array
            a = 0
            for b in range( RADIX ):
                buck = buckets[b]
                for i in buck:
                    self.list[a] = i
                    a += 1

            # move to next digit
            placement *= RADIX

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def ShellSort(self):

        start_time = time.time()

        #arr = np.array(self.list, dtype=int)

        n = len(self.list)

        gap = n/2

        while gap > 0:
            gap = int(gap)
            for i in range(gap, n):
                temp = self.list[i]
                j = i
                while j >= gap and self.list[j-gap] > temp:
                    self.list[j] = self.list[j-gap]
                    j -= gap

                self.list[j] = temp

            gap /= 2

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time


    def MergeSort(self, arr):

        start_time = time.time()

        if len(arr)>1:
            mid = len(arr)//2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.MergeSort(left_half)
            self.MergeSort(right_half)

            i=0
            j=0
            k=0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k]=left_half[i]
                    i=i+1
                else:
                    arr[k]=right_half[j]
                    j=j+1
                k=k+1

            while i < len(left_half):
                arr[k]=left_half[i]
                i=i+1
                k=k+1

            while j < len(right_half):
                arr[k]=right_half[j]
                j=j+1
                k=k+1

        self.execution_time = time.time() - start_time

        return arr, self.execution_time

    def Heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i] # swap

            # Heapify the root.
            self.Heapify(arr, n, largest)

    # The main function to sort an array of given size
    def HeapSort(self, arr):

        start_time = time.time()

        n = len(arr)

        # maxheap.
        for i in range(n, -1, -1):
            self.Heapify(arr, n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] # swap
            self.Heapify(arr, i, 0)

        self.execution_time = time.time() - start_time

        return arr, self.execution_time
