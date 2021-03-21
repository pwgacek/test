from random import randint
def sort(T,k):
    n = len(T)
    B = [0]*2

    B[0] = [0]*10
    B[1] = [0]*(n-10)
    j = 0
    l = 0
    for i in range(len(T)):

        if T[i] < 0 or T[i] > k:
            
            B[0][j] = T[i]
            j+=1

        else:
            B[1][l] = T[i]
            l+=1

    
    B[1] = counting_sort(B[1],k+1)
   
    for i in range(n-10):
        T[i] = B[1][i]
    j = 0
    for i in range(n-10,n):
        T[i] = B[0][j]
        j+=1
    print(T)

    return(insertion_sort(T))

def counting_sort(A,k):
    n = len(A)
    B = [0]*n
    C = [0]*k
    for i in range(n):
        C[A[i]]+=1

    for i in range(1,k):
        C[i] +=C[i - 1]
    
    for i in range(n-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
        
    return B

def insertion_sort(tab):
    n = len(tab)
    for i in range(n-10,n):
        val = tab[i]
        j = i - 1 
        while val < tab[j] and j >= 0:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = val
    
    return tab

T=[randint(0,20) for i in range(20)]
for i in range(0,20,2):
    T[i] = randint(-5,-1)

print(T)
print(sort(T,20))