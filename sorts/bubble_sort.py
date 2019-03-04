from utils.utils import swap

def bubble_sort(array):
    for j in range(0, len(array)):
        for j in range(len(array)-1, 0, -1):
            if (array[j] < array[j-1]):
                swap(array, j, j-1) 
