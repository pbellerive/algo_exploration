def insertion_sort(array):
    for idx in range(1, len(array)):
        i = idx - 1 
        item = array[idx]
        while i >= 0 and array[i] > item:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = item




