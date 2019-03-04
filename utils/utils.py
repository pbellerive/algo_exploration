import time 

withLog = False

def validate_order(array, order='asc'):
    previous = array[0]
    for item in range(1, len(array)):
        if (previous > array[item]):
            return False
        else: 
            previous = array[item]
    return True

def execute_and_time(function, *args):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    print(end_time - start_time)

def log(*args):
    global withLog

    if (withLog):
        print(*args)

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp