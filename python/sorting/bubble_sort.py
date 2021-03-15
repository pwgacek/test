from random import randint
def bubble_sort(tab):
    n = len(tab)
 
    for i in range(1,n):
      
        for j in range(n-1,i-1,-1):
            if tab[j] < tab [j-1]:
                tab[j] , tab[j-1] = tab[j-1] , tab[j]
    return tab

tab = [randint(-10,10) for i in range(20)]
print(tab)

print(bubble_sort(tab))

