#!/usr/bin/python

class listNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    head = tail = listNode(0)
    flag = 0
    while l1 or l2 or flag:
        node = listNode(flag)
        if l1:
            node.val = node.val + l1.val
            l1 = l1.next
        if l2:
            node.val = node.val + l2.val
            l2 = l2.next
        flag = node.val / 10
        node.val = node.val % 10
        tail.next = node
        tail = tail.next
    tail.next = None

    return head.next

l1 = listNode(2)
l2 = listNode(4)
l3 = listNode(3)
l4 = listNode(5)
l5 = listNode(6)
l6 = listNode(4)

l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6

ll = addTwoNumbers(l1, l4)
while ll:
    print ll.val
    ll = ll.next
