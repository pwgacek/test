from random import randint

def decomposition(num):
    tab=[]
    devider = 2
    while devider*devider <= num:
        while num % devider == 0:
            tab.append(devider)
            num//=devider
        devider+=1
    if num != 1 :
        tab.append(num)
    return tab




num = randint(2,10000)
print(num)
print(decomposition(num))