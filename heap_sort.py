def heap_sort(array):
    build_heap(array)
    for item in range(len(array), 0, -1):
        exchange(array, 0, item-1)
        max_heapify(array, 0, item-1)

    return array

def build_heap(array):
    length = (len(array) >> 1) - 1
    for i in range(length, -1, -1):
        max_heapify(array, i)

def max_heapify(array, i, size=None):
    size =  heap_size(array) if size == None else size
    left_node = left(i)
    right_node = right(i) 
    
    if (left_node < size) and (array[left_node] > array[i]):
        largest = left_node
    else:
        largest = i
    
    if (right_node < size) and (array[right_node] > array[largest]):
        largest = right_node

    if largest != i:
        exchange(array, i, largest)
        max_heapify(array, largest, size)
    return array

def exchange(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def heap_size(array):
    return len(array)

def left(index):     
    return (index << 1) | 1

def right(index):   
    return ((index << 1)) + 2 

def parent(index):
    return index >> 1