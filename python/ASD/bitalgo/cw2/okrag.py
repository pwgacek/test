from math import sqrt
from math import floor
from random import randint
def radius(T):
    return sqrt(T[0]*T[0] + T[1]*T[1])

def bucket_sort(T,k):
    n = len(T)
    B = [0]*n
    for i in range(n):
        B[i] = []
    
    for i in range(n):
        rad =radius(T[i])
        q = rad/k
        if q == 1:
            B[n-1].append([T[i],rad])
        else:
            B[floor(((rad/k)**2)*n)].append([T[i],rad])
    
    for i in range(n):
        insertion_sort(B[i])
        print(B[i])
    
    j = 0
    
    for i in range(n):
        while B[i]:
            T[j] = (B[i].pop(0))[0]

            j+=1

def insertion_sort(T):
    n = len(T)
    for i in range(1,n):
        val = T[i]
        j = i - 1 
        while val[1] < T[j][1] and j >= 0:
            T[j+1] = T[j]
            j-=1
        T[j+1] = val
    
T= [[randint(0,7),randint(0,7)] for i in range(10) ]
bucket_sort(T,10)
print(T)