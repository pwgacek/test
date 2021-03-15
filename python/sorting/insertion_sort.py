from random import randint
def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        val = tab[i]
        j = i - 1 
        while val < tab[j] and j >= 0:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = val
    
    return tab
tab = [randint(0,10) for i in range(20)]
print(tab)
print(insertion_sort(tab))

