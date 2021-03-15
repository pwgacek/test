from random import randint

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_sort(head):
    if head == None or head.next == None : return head

    left_list,right_list = devide_list(head)

    
    return merge(merge_sort(left_list), merge_sort(right_list))

    

def merge(left_list,right_list):
    curr = Node(None)
    new_list = curr
    
  

    while left_list and right_list :
        if left_list.value < right_list.value:
            curr.next = left_list
            left_list=left_list.next
        else:
            curr.next = right_list
            right_list=right_list.next
        
        curr = curr.next

    if not left_list:
        curr.next = right_list
    else:
        curr.next = left_list

    return new_list.next


def scal_reku(z1,z2):
    if z1 == None:
        return z2
    if z2 == None:
        return z1

    if z1.value < z2.value:
        result = z1
        result.next = scal_reku(z1.next,z2)
    else:
        result = z2
        result.next = scal_reku(z1,z2.next)

    return result




def devide_list(head):
    n = list_length(head)
    middle = n // 2

    left_list = head
    prev = None
    for i in range(middle):
        prev = head
        head = head.next
    prev.next = None
    right_list = head
    return left_list,right_list

    


def list_length(head):
    counter = 0
    while head:
        head = head.next
        counter+=1
    return counter

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

z1=insert(None,randint(1,20))
for i in range(20):
    z1=insert(z1,randint(1,20))



printall(z1)

z1 = merge_sort(z1)

printall(z1)
