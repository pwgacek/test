from math import floor
from random import randint
class Node:
    def __init__(self):
        self.next = None
        self.value = None



def sort(first,a,b):
    n = length(first)
   
    curr = first
    B = [None]*n
    for i in range(n):
            index = floor(((curr.value-a)/(b-a))*n)
            if index == n: index-=1
            tmp = curr.next
            curr.next = B[index]
            B[index] = curr
            curr = tmp

    for i in range(n):
        B[i] = insertion_sort(B[i])
        printall(B[i])

    first = merge(B)
    return first


def merge(B):
    head = Node()
    head.next = B[0]
    curr = head.next
    prev = head
    for i in range(len(B)-1):
        while curr!=None:
            prev = curr
            curr = curr.next
        prev.next = B[i+1]
        curr = B[i+1]
    
    return head.next
            

def length(first):
    curr = first
    i = 0
    while curr != None:
        curr = curr.next 
        i+=1
    return i


def insert(curr, n):
    q = Node()
    q.value = n

    p = curr
    prev =None

    while p != None:
        prev = p
        p = p.next

    if prev == None:
        return q

    prev.next = q
    return curr


def printall(curr):
    while curr != None:
        print(curr.value,end=" ")
        curr = curr.next
    print("")


def insertion_sort(head):

    curr = head
    prev = None
    sorted_list = Node()
    while curr != None:
        prev = curr
        curr = curr.next
        
        sorted_list = add_to_sorted(sorted_list,prev)

    return sorted_list.next


def add_to_sorted(sorted_head,new_node):
    curr = sorted_head.next
    prev = sorted_head
    while  curr!=None   and new_node.value > curr.value :
        prev = curr 
        curr = curr.next

    prev.next = new_node
    new_node.next = curr

    return sorted_head





a = 0

b = 10

    
z1 = insert(None,randint(a,b))

for i in range(randint(10,20)):
    z1 = insert(z1,randint(a,b))


printall(z1)
z1 = sort(z1,a,b)
printall(z1)

