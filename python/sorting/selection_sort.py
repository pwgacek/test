from random import randint

def selection_sort(tab):
    n = len(tab)
   
    for s in range(0,n-1):
        min_i = s
        
        for i in range(s+1,n):

            if tab[min_i] > tab[i] :
                min_i = i 
        
        tab[s] , tab[min_i] = tab[min_i] , tab[s]
       
    
    return tab

tab=[randint(-10,10) for i in range(20)]  
print(tab)         
print(selection_sort(tab))
print(tab)
