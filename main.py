import sys
from random import shuffle
from sorts.insertion_sort import insertion_sort
from sorts.heapsort import build_heap
from sorts.heapsort import heapsort
from sorts.mergesort import mergesort
from sorts.bubblesort import bubblesort
from sorts.quicksort import quicksort
from string_matching.naive import naive_string_matching
from string_matching.rabin_karp import rabin_karp_matcher
from utils.utils import execute_and_time
from utils.utils import validate_order

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
    execute_and_time(heapsort, clone_array)
    print(validate_order(clone_array))
elif (sys.argv[1] == 'merge'):
    print('Merge sort')
    clone_array = original_array[:]
    execute_and_time(mergesort, clone_array, 0, len(clone_array))
    print(validate_order(clone_array))
elif (sys.argv[1] == 'bubble'):
    print('Bubble sort')
    clone_array = original_array[:]
    execute_and_time(bubblesort, clone_array)
    print(validate_order(clone_array))
elif (sys.argv[1] == 'quick'):
    print('Quicksort')
    clone_array = original_array[:]
    print(clone_array)
    execute_and_time(quicksort, clone_array, 0, len(clone_array)-1)
    print(validate_order(clone_array))
elif (sys.argv[1] == 'naive-string'):
    naive_string_matching(sys.argv[2], sys.argv[3])
elif (sys.argv[1] == 'rabin'):
    if (rabin_karp_matcher(sys.argv[2], sys.argv[3], 40999999, 9999999937)):
        print('found')
    else:
        print('lost')
