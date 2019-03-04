def rabin_karp_matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    
    #preprocessing
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t+ord(text[i])) % q  
        
    #matching
    for s in range((n-m+1)):
        if (p == t):
            if (pattern == text[s:(s+m)]):
                return True
        if (s < (n-m)):
            t = (d*(t-h*ord(text[s])) + ord(text[s+m])) % q 
    return False
