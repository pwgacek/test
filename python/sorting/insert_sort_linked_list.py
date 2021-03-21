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




    
z1 = insert(None,3)
for i in range(randint(3,10)):
    z1 = insert(z1,randint(1,10))

printall(z1)
z1 = insertion_sort(z1)
printall(z1)
