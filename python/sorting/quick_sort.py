from random import randint
import time




def quick_sort(T,p,r):

    if p < r :
        pivot = partition2(T,p,r)

        quick_sort(T,p,pivot-1)
        quick_sort(T,pivot+1,r)
   


def partition(T,p,r):
    pivot = r
    a = p
    b = p
    while a != pivot:
        if T[a] <= T[pivot]:
            T[a] ,T[b] = T[b],T[a]
            a+=1
            b+=1
        else:
            a+=1
    T[a],T[b] = T[b],T[a]
    
    return b

def partition2(T,p,r):
  
    a = p
    b = p - 1
    x = T[r]
    for a in range(p,r):
        if T[a] <= x:
            b+=1
            T[a] , T[b] = T[b] , T[a]
    T[b+1],T[r] = T[r],T[b+1]
   
    return  (b+1)





T=[randint(0,100) for i in range(1000)]

quick_sort(T,0,len(T)-1)


