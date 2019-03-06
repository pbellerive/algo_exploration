def mergesort(array, p, r):       
    if (r-p > 1):
        q = (p+r)//2
        mergesort(array, p, q)  
        mergesort(array, q, r)    
        merge(array, p, q, r)
def merge(array, p, q, r):    
    left = array[p:q]
    right = array[q:r]

    left.insert(len(left), None)
    right.insert(len(right), None)
    print(left, right)
    i = 0
    j = 0
    for k in range (p, r):
        # % is the sentinel value as explain in Introduction to Algorithm second edition p.29
        if (right[j] == None) or (left[i] != None and left[i] <= right[j]):
            array[k] = left[i]
            i += 1
        else: 
            array[k] = right[j]
            j += 1
