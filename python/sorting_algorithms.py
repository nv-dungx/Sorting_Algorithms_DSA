import sys
import numpy as np
import random

sys.setrecursionlimit(10**7)


def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def mergesort(arr):
    def merge(left, mid, right):
        l = arr[left:mid+1]
        r = arr[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                k += 1
                i += 1
            else:
                arr[k] = r[j]
                k += 1
                j += 1
        while i < len(l):
            arr[k] = l[i]
            k += 1
            i += 1
        while j < len(r):
            arr[k] = r[j]
            k += 1
            j += 1


    def sort(left, right):
        if left < right:
            mid = (left + right) // 2
            sort(left, mid)
            sort(mid+1, right)
            merge(left, mid, right)
    
    sort(0, len(arr)-1)
    return arr


def quicksort(arr):
    def partition(low, high):
        mid = (low + high)//2
        arr[mid], arr[high] = arr[high], arr[mid]
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1
    
    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p-1)
            sort(p+1, high)

    sort(0, len(arr)-1)
    return arr

def numpysort(arr):
    return np.sort(arr)