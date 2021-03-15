def merge_sort(T):
    print(T)
    n = len(T)
    if n > 1:
        middle = n // 2
        return merge(T,merge_sort(T[0:middle]),merge_sort(T[middle:n]))
    else:
        return T

from random import randint
def merge(T,lt,rt):
    print("merge")
    print()
    n = len(lt) + len(rt)
   
    i=0
    j=0

    for k in range (n):

        if j == len(rt):
            T[k]=lt[i]
            i+=1
        elif i == len(lt):
            T[k]=rt[j]
            j+=1

        elif lt[i] <= rt[j]:
            T[k]=lt[i]
            i+=1
        else:
            T[k]=rt[j]
            j+=1
    return T
    

T=[randint(0,10) for i in range(15)]

print(T)
merge_sort(T)
print(T)
