from insertion_sort import insertion_sort
from heap_sort import build_heap
from heap_sort import heap_sort

original_array = [5,76,4,175,78,9,43,99,12,]
print(original_array)
insertion_sort(original_array)
print(original_array)

original_array = [5,76,4,175,78,9,43,99,12,22]
print(original_array)
print(heap_sort(original_array))