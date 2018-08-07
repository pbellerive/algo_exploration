import sys
from random import shuffle
from sorts.insertion_sort import insertion_sort
from sorts.heap_sort import build_heap
from sorts.heap_sort import heap_sort
from sorts.merge_sort import merge_sort
from utils.utils import *

length = 10
if (len(sys.argv) == 3):
    length = sys.argv[2]
    
original_array = [iter for iter in range(0, int(length))]
shuffle(original_array)

if (len(sys.argv) < 2):
    print('Need to specify algo')
    exit()

if (sys.argv[1] == 'insertion'):
    print('Insertion sort')
    clone_array = original_array[:]
    execute_and_time(insertion_sort, clone_array)
    print(validate_order(clone_array))
elif (sys.argv[1] == 'heap'):
    print('Heap sort')
    clone_array = original_array[:]
    execute_and_time(heap_sort, clone_array)
    print(validate_order(clone_array))
elif (sys.argv[1] == 'merge'):
    print('Merge sort')
    clone_array = original_array[:]
    execute_and_time(merge_sort, clone_array, 0, len(clone_array))
    print(validate_order(clone_array))
