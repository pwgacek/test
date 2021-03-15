from random import randint
def counting_sort(A,k):
    n = len(A)
    B = [0]*n
    C = [0]*k
    for i in range(n):
        C[A[i]]+=1

    for i in range(1,k):
        C[i] +=C[i - 1]
    print(C)
    for i in range(n-1,-1,-1):
        B[C[A[i]] - 1 ]  = A[i]
        C[A[i]] -= 1
    return B




T = [randint(0,10) for i in range(7)]

print(T)
T = counting_sort(T,11)

print(T)
