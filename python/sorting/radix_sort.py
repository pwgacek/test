from random import randint
def radix_sort(A,d,base):
    n = len(A)
    T = [[0]*d]*n
    for i in range(n):
        T[i] = make_array(A[i],d)

    for p in range(d-1,-1,-1):
        T=sort_by_key(T,d,p,base)

    for i in range(n):
        A[i] = make_int(T[i])

    

#complexity : (log(10)(k)+1) * (n+10)  dla k = n (zakres danych) mamy O(nlogn)
# jesli zmienimy podstawe na n to wtedy mamy log(n)(n) * (2n) wtedy zlozonosc to O(n)

def sort_by_key(A,d,p,base):
    n = len(A)
    B = [0]*n
    for i in range(n):
        B[i] =[0]*d
    C = [0]*base
    for i in range(n):
        C[A[i][p]]+=1

    for i in range(1,base):
        C[i] +=C[i - 1]

    for i in range(n-1,-1,-1):
        B[C[A[i][p]] - 1 ]  = A[i]
        C[A[i][p]] -= 1
    return B    
def make_array(num,d):
    T = [0]*d
    for i in range(d-1,-1,-1):
        T[i] = num % 10 
        num//=10
    return T

def make_int(T):
    num = 0
    for i in range(len(T)) :
        num= num*10 + T[i]
    return num
A = [randint(0,999) for i in range(10)]
print(A)

radix_sort(A,3,10)
print(A)
