from random import randint
import time

def merge_sort(T,first,last):
    if first < last :
        middle = (first + last) // 2
            
        T = merge_sort(T,first,middle)
        T = merge_sort(T,middle + 1,last)

        return merge(T,first,last,middle)

    else : return T
    
    




def merge(T,first,last,middle):
    T_joined = T[0:]
 
    i = first
    j = middle + 1

    for k in range(first,last + 1):
        if j == last + 1:
            T_joined[k]=T[i]
            i+=1
        elif i == middle + 1:
            T_joined[k]=T[j]
            j+=1

        elif T[i] <= T[j]:
            T_joined[k]=T[i]
            i+=1
        else:
            T_joined[k]=T[j]
            j+=1
      
    return T_joined

tab = [randint(0,10000) for i in range(100000)]
start = time.time()
merge_sort(tab,0,len(tab)-1)
end = time.time()

total = end - start
print("czas: {0:02f}s".format(total))
