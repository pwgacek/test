from random import randint
from math import floor
def bucket_sort(T):
    n = len(T)
    B = [0]*n
    for i in range(n):
        B[i] = []

    for i in range(n):
        B[floor(T[i] * n )].append(T[i])
   
    for i in range(n):
        insertion_sort(B[i])
    
    j = 0
    
    for i in range(n):
        while B[i]:
            T[j] = B[i].pop(0)
            j+=1


def bucket_sort2(T):
    n = len(T)
    B = [0]*n
    for i in range(n):
        B[i] = []

    mx = find_max(T)
    mn = find_min(T)
    
    for i in range(n):
        B[floor(((T[i] - mn )/ (mx-mn+0.0001)) * n )].append(T[i])
   
    for i in range(n):
        insertion_sort(B[i])
    print(B)
    
    j = 0
    
    for i in range(n):
        while B[i]:
            T[j] = B[i].pop(0)
            j+=1


def find_max(T):
    maximum = T[0]
    for i in range(len(T)):
        if maximum < T[i]:
            maximum = T[i]
    return maximum


def find_min(T):
    minimum = T[0]
    for i in range(len(T)):
        if minimum > T[i]:
            minimum = T[i]
    return minimum

def insertion_sort(T):
    n = len(T)
    for i in range(1,n):
        val = T[i]
        j = i - 1 
        while val < T[j] and j >= 0:
            T[j+1] = T[j]
            j-=1
        T[j+1] = val
    
    


T = [randint(50,99) for i in range(20)]
print(T)
bucket_sort2(T)
print(T)