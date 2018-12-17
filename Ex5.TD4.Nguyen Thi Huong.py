def RangdutermeDepassant(A):
    Sn = 0
    k = 0
    while Sn <= A:
        Un = (2*k - 3)**2
        Sn += Un
        if Sn <= A: 
            k += 1
    return k

A = int(input("Donnez moi votre nombre: "))
print(RangdutermeDepassant(A))


    
        

