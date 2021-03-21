from random import randint
class Zakres:
    def __init__(self,A,k):
        self.A = A
        self.k = k

    def counting_sort(self):
        n = len(self.A)
       
        C = [0]*self.k

        for i in range(n):
            C[self.A[i]]+=1

        for i in range(1,self.k):
            C[i] +=C[i - 1]
       
        self.A = C

    

    def count_num_in_range(self,a,b):
        self.counting_sort()
        return self.A[b] -  self.A[a-1]


    

T = [randint(0,10)for i in range(10)]
print(T)
z = Zakres(T,11)
print(z.count_num_in_range(6,10))