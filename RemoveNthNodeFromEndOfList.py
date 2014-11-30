#!/usr/bin/python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    nn = 0
    le = head
    while le:
        nn = nn + 1
        le=le.next
    n = nn - n 
    print "n is %d, nn is %d" % (n, nn)
    i = 0
    tail = head
    tmp = head
    if n != 0:
        while i < n:
            tmp = tail
            tail = tail.next
            i = i + 1
        tmp.next = tail.next
    else:
        head = head.next
    return head

l1 = ListNode(1)
#l2 = ListNode(2)
#l3 = ListNode(3)
#l4 = ListNode(4)
#l5 = ListNode(5)

#l1.next = l2
#l2.next = l3
#l3.next = l4
#l4.next = l5

h = removeNthFromEnd(l1, 1)

while h:
    print h.val
    h = h.next
