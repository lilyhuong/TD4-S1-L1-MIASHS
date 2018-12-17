def termedelaSuite(n):
    u = 2 #c'est valeur de u
    for k in range(1,n+1):
        u = 1/2 *(u + 1/u)
    
    return u
print(termedelaSuite(5))
