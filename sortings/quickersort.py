from random import randrange
class Node:
    def __init__(self):
        self.value=None
        self.next=None

def quicker_sort(number):
    smaller=Node()
    bigger=Node()
    equal=Node()
    smaller_cpy=smaller
    bigger_cpy=bigger
    equal_cpy=equal
    pivot=number.value
    while(number.next!=None):
        if number.value <pivot:
            smaller.next=number
            smaller=smaller.next
            number=number.next
        elif number.value>pivot:
            bigger.next=number
            bigger=bigger.next
            number=number.next
        else:
            equal.next=number
            equal=equal.next
            number=number.next
    quicker_sort(smaller_cpy)
    quicker_sort(bigger_cpy)

def create_list(size):
    element = Node()
    element.next=None
    element.val=randrange(100)
    for i in range(size-1):
        temp = Node()
        temp.val = randrange(100)
        temp.next = element
        element = temp
    return element
