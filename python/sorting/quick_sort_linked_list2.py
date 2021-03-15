from random import randint

class Node:
    def __init__(self):
        self.next = None
        self.value = None

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



def get_tail(head):
    
    curr = head
    while(curr  and curr.next):
        curr=curr.next
    
    return curr
def partition(head):

    pivot = get_tail(head) 
    last = pivot
    curr = head
    prev = None

    while curr != pivot :
       
        if curr.value > pivot.value:
            if curr == head:
                head = head.next
             
            if prev :
                prev.next = curr.next
                
            
            last.next = curr
            last = last.next
            tmp = curr
            curr = curr.next
            tmp.next = None
        

        else:
            prev = curr
            curr = curr.next

    return head , pivot


def divide(head,pivot):

  
    curr = head
    prev = None
    if head == pivot:
        new_head1 = None
    else:
        while curr and curr!= pivot:
            prev = curr
            curr = curr.next
        if prev:
            prev.next = None
        new_head1 = head
    pp = curr
    prev = None
   
    prev = curr
    curr = curr.next
    prev.next = None
    new_head2 = curr
    
 

    return new_head1,pp,new_head2

def merge(new_head1,pp,new_head2):
    if new_head1:
        head = new_head1
        while new_head1.next:
            new_head1 = new_head1.next
        new_head1.next  = pp 
        pp.next = new_head2

    else:
        head = pp
        pp.next = new_head2
    
    return head
        

def quick_sort(head):
    if head and head.next :
        head,pivot = partition(head)
        new_head1, pp, new_head2 = divide(head,pivot)
        new_head1 = quick_sort(new_head1)
        new_head2 = quick_sort(new_head2)
        head = merge(new_head1,pp,new_head2)

    return head


z1=insert(None,randint(1,20))
for i in range(20):
    z1=insert(z1,randint(1,20))

printall(z1)

z1 = quick_sort(z1)

printall(z1)


        