def sort(T):
    max_length = find_max_length(T)
    if max_length == 0: return T
 
    B = [0]*max_length
    for i in range(max_length):
        B[i] = []
    for i in range(len(T)):
        B[len(T[i]) - 1].append(T[i])
    
    T_sorted = []
    for i in range(max_length-1,-1,-1):

        T_to_sort = B[i]

        for j in range(len(T_sorted)):
            T_to_sort.append(T_sorted[j])
     
        T_sorted = counting_sort(T_to_sort,i)

    return T_sorted
    




def counting_sort(A,index):
 
    n = len(A)
    B = [0]*n
    for i in range(len(B)):
        B[i] = []
    C = [0]*26
    for i in range(n):
     
        C[ord(A[i][index])-97]+=1

    for i in range(1,26):
        C[i] +=C[i - 1]
    
    for i in range(n-1,-1,-1):
        C[ord(A[i][index])-97] -= 1
        B[C[ord(A[i][index])-97]] = A[i]
        
    return B




def find_max_length(T):
    max_length = 0 
    for i in range(len(T)):
        if len(T[i]) > max_length:
            max_length = len(T[i])
    return max_length

T=["ala","ma","psiak","kota","i","psa","psak","a","masz"]
print(sort(T))