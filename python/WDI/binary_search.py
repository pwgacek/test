from random import randint
import time
def binary_search(tab,l,r,val):
    middle = (r + l) // 2

    if l <= r:
        if tab[middle] == val:
            return True
    
        elif tab[middle] > val:
            return binary_search(tab,l,middle-1,val)
        else:
            return binary_search(tab,middle+1,r,val)

    else: return False


def binary_search2(tab,val):
    l = 0
    r = len(tab) - 1 
    if r == 0 :
        return True if val == tab[0] else  False
    while l <= r:
        middle = (r + l) // 2
        if tab[middle] == val: return True
        elif tab[middle] > val:
            r = middle - 1
        else:
            l = middle + 1
    return False

    

#tab=[i*3  for i in range(10000)]
tab = [2]
#val = randint(0,10000)
val = 2
print(val)

start = time.time()
print(binary_search(tab,0,len(tab)-1,val))
end = time.time()
print("rekurencja")
total = end - start
print("{0:02f}s".format(total))


start = time.time()
print(binary_search2(tab,val))
end = time.time()
print("iteracja")
total = end - start
print("{0:02f}s".format(total))




    