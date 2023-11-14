"""
def reverseList():
    # list that contains songs
    lst = [1,2,3,4,5]
    lst_hdr = lst[-1]
    lst_hdr_copy = lst[-1]

    while lst_hdr.next is not None:
        lst_hdr.next(lst_hdr_copy.prev)
        lst_hdr = lst_hdr.prev
        lst_hdr.prev = lst_hdr
    
    return # head of lst_hdr

def findMedian():
    lst = [1,2,3,4,5]
    slow = lst[1]
    fast = lst[1]

    while fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

"""
import random

lst = [1,2,3,4,5]

random.shuffle(lst)
print(lst)
    

