#!/usr/bin/python

def isPalindrome(x):
    res = 0
    xx = x
    while xx:
        res = res*10 + xx % 10
        xx = xx / 10
    
    if x == res:
        return True
    else:
        return False

    
print isPalindrome(-2147483648)
