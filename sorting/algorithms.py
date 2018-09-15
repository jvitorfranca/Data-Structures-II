import tools
import time
import random


# Class with all the algorithms supported
class Algorithms():

    # The properties are basically execution time
    # And a list of integers
    execution_time = -1

    def __init__(self, list):
        self.list = list

    def InsertSort(self):

        start_time = time.time()

        # Walking through the list
        for i in range(1, len(self.list)):
            j = i
            # Examine each item and compare it to items on its left
            while j > 0 and self.list[j-1] > self.list[j]:
                self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
                j -= 1

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def SelectSort(self):

        start_time = time.time()

        # During each iteration we'll select the smallest item
        # From the unsorted partition and move it to the sorted partition
        for j in range(0, len(self.list) - 1):
            min = j
            for i in range(j + 1, len(self.list)):
                if self.list[i] < self.list[min]:
                    min = i
            if min != j:
                self.list[j], self.list[min] = self.list[min], self.list[j]

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def CountSort(self):

        start_time = time.time()

        # Counting the number of objects having distinct key values
        max = 0
        for i in range(0, len(self.list)):
            if self.list[i] > max:
                max = self.list[i]

        max = max + 1

        # Create a count array to store the count of each unique object
        count = [0] * max

        for j in self.list:
            count[j] += 1

        # Count each element in the given array and place the count
        # At the appropriate index
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

        while not maxLength:
            maxLength = True
            # Declare and initialize buckets
            buckets = [list() for _ in range( RADIX )]

            # Split aList between lists
            for i in self.list:
                tmp = i / placement
                buckets[int(tmp % RADIX)].append(i)
                if maxLength and tmp > 0:
                    maxLength = False

            # Empty lists into aList array
            a = 0
            for b in range( RADIX ):
                buck = buckets[b]
                for i in buck:
                    self.list[a] = i
                    a += 1

            # Move to next digit
            placement *= RADIX

        self.execution_time = time.time() - start_time

        return self.list, self.execution_time

    def ShellSort(self):

        start_time = time.time()

        # We compare elements that are a distance apart rather
        # Than adjacent
        n = len(self.list)

        # We calculate "gap" for each pass, and then select the
        # Elements towards the right gap
        gap = n/2

        # One by one select elements to the right of the gap
        # and place them at their appropriate position
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

            # Divide the array in two parts initially
            mid = len(arr)//2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Do the same recursively
            self.MergeSort(left_half)
            self.MergeSort(right_half)

            # We divide the array in smaller portions and
            # Compare with it's neighbors, after doing this,
            # We "merge" by combining the small portions
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

    def Partition(self, arr, low, high):
        pivot = arr[high-1]
        start = low
        end = low
        for i in range(low, high):
            if arr[i] > pivot:
                end += 1
            else:
                end += 1
                start += 1
                aux = arr[start-1]
                arr[start-1] = arr[i]
                arr[i] = aux
        return start-1

    def QuickSort(self, arr, low, high):

        start_time = time.time()

        if low < high:
            pivot_position = self.RandPartition(arr, low, high)
            self.QuickSort(arr, low, pivot_position)
            self.QuickSort(arr, pivot_position+1, high)

        self.execution_time = time.time() - start_time

        return arr, self.execution_time

    def RandPartition(self, arr, low, high):
        rand = random.randrange(low, high)
        aux = arr[high-1]
        arr[high-1] = arr[rand]
        arr[rand] = aux
        return self.Partition(arr, low, high)
