import time

from random import randint



def bubble_sort(tab):
    n = len(tab)
 
    for i in range(1,n):
      
        for j in range(n-1,i-1,-1):
            if tab[j] < tab [j-1]:
                tab[j] , tab[j-1] = tab[j-1] , tab[j]
    return tab




def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        var = tab[i]
        j = i - 1 
        while var < tab[j] and j >= 0:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = var
    
    return tab



def selection_sort(tab):
    n = len(tab)
   
    for s in range(0,n-1):
        min_i = s
        
        for i in range(s+1,n):

            if tab[min_i] > tab[i] :
                min_i = i 
        
        tab[s] , tab[min_i] = tab[min_i] , tab[s]
       
    return tab


def quick_sort(tab,start,end):

    pivot = end
    a = start
    b = start
    while a != pivot :
        if tab[a] <= tab[pivot]:
            tab[a] ,tab[b] = tab[b],tab[a]
            a+=1
            b+=1
        else:
            a+=1
     
    tab[a],tab[b] = tab[b],tab[a]

    pivot = b
    if start < pivot - 1: 
        tab=quick_sort(tab,start,pivot-1)
    if end > pivot + 1 :
        tab=quick_sort(tab,pivot+1,end)
    return tab













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


def merge_sort2(T):
    n = len(T)
    if n > 1:
        middle = n // 2
        lt = merge_sort2(T[0:middle])
        rt = merge_sort2(T[middle:n])
        return  merge(lt,rt)
    else: return T












def merge_sort3(T):
    f = 0
    l = len(T) - 1
    
    def sort(T,first,last):
        if first < last :
            middle = (first + last) // 2
            
            T = sort(T,first,middle)
            T = sort(T,middle + 1,last)

            return merge3(T,first,last)

        else : return T
    
    return sort(T,f,l)




def merge3(T,first,last):
    T_joined = T[0:]
    middle = (first + last) // 2
    i = first
    j = middle + 1
    #print(first,last,middle)
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
       # print(">",T)
    return T_joined




def merge_sort4(T):
   
    n = len(T)
    if n > 1:
        middle = n // 2
        return merge4(T,merge_sort4(T[0:middle]),merge_sort4(T[middle:n]))
    else:
        return T

from random import randint
def merge4(T,lt,rt):
   
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
    




tab = [randint(0,10000) for i in range(100000)]
tab2=tab[0:]
tab3=tab[0:]
tab4=tab[0:]

start = time.time()
merge_sort(tab)
end = time.time()

total = end - start
print("pierwszy: {0:02f}s".format(total))

start = time.time()
merge_sort2(tab2)
end = time.time()

total = end - start
print("drugi:{0:02f}s".format(total))


start = time.time()
merge_sort4(tab4)
end = time.time()

total = end - start
print("czwarty:{0:02f}s".format(total))






