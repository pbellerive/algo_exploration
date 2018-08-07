import time 

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