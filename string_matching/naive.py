
# Naive string search 
# No preprocessing,  execution time O((n-m + 1)m)
def naive_string_matching(T, P):
    n = len(T)
    m = len(P)
    print('n=', n, ',m=', m)
    for s in range(0, (n-m)+1):
        if (P == T[s:s+m]):
            print('Pattern found at position: ', s, '-', T[s:s+m])

