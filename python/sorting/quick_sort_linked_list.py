from random import randint

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def insert(start, n):
    q = Node(n)

    p = start
    prev = None

    while p != None:
        prev = p
        p = p.next

    if prev == None:
        return q

    prev.next = q
    return start


def printall(start):
    while start != None:
        print(start.value,end=" ")
        start = start.next
    print("")


def set_elem(head,n):
    if n == -1: return None
    curr = head
    for i in range(n):
        curr = curr.next
    return curr
def get_index(head,pivot):
    i = 0
    curr = head
    while(curr != pivot):
        curr = curr.next
        i+=1
    return i
def get_tail(head):
    i = -1
    curr = head
    while(curr):
        curr=curr.next
        i+=1
    return i
def partition(head,p,r):

    
    pivot = set_elem(head,r) 
    last = pivot
    end = last.next
    curr = set_elem(head,p)
    prev = set_elem(head,p-1)

    while curr != pivot :
        if curr.value > pivot.value:
            if curr == head:
                head = head.next
                last.next = curr
                last = last.next
            else:
                prev.next = curr.next
                last.next = curr
                last = last.next
            
            help = curr
            curr = curr.next
            help.next = None
        else:
            prev = curr
            curr = curr.next

    last.next = end

    return head , get_index(head,pivot)

def quick_sort(head,p,r):
    if p < r:
      
        head , q = partition(head,p,r)
        head = quick_sort(head,p,q-1)
        head = quick_sort(head,q+1,r)
    return head


z1=insert(None,randint(1,20))
for i in range(20):
    z1=insert(z1,randint(1,20))

z1 = quick_sort(z1,0,get_tail(z1))


printall(z1)

        