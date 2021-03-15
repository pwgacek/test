from random import randint
import time




def quick_sort2(T,p,r):

    while p < r :
        pivot = partition(T,p,r)

        if (pivot - p) < (r - pivot):
            quick_sort2(T,p,pivot-1)
            p = pivot + 1
        else:
            quick_sort2(T,pivot+1,r)
            r = pivot - 1
        
   
def quick_sort(T,p,r):
    if p < r :
        pivot = partition(T,p,r)
        quick_sort(T,p,pivot-1)
        quick_sort(T,pivot+1,r)

def partition(T,p,r):
  
    a = p
    b = p - 1
    x = T[r]
    for a in range(p,r):
        if T[a] <= x:
            b+=1
            T[a] , T[b] = T[b] , T[a]
    T[b+1],T[r] = T[r],T[b+1]
   
    return b+1





T1=[randint(0,100) for i in range(1000)]
T2=T1[0:]

quick_sort(T1,0,len(T1)-1)
quick_sort2(T1,0,len(T1)-1)

