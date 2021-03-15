from random import randint
def merge_sort(T):
    n = len(T)

    if n > 1:
        middle = n // 2
        lt = [T[i] for i in range(0,middle)]
        rt = [T[i] for i in range(middle,n)]


        return merge(merge_sort(lt),merge_sort(rt))
    
    else : return T

        

def merge(lt,rt):

    n = len(lt) + len(rt)
    t_joined = [0 for k in range(n)]
    i=0
    j=0

    for k in range (n):

        if j == len(rt):
            t_joined[k]=lt[i]
            i+=1
        elif i == len(lt):
            t_joined[k]=rt[j]
            j+=1

        elif lt[i] <= rt[j]:
            t_joined[k]=lt[i]
            i+=1
        else:
            t_joined[k]=rt[j]
            j+=1
    
    return t_joined






T=[randint(-100,100) for i in range(100)]
print(merge_sort(T))


   
   

   