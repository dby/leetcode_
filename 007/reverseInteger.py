#!/usr/bin/python

def reverse(x):
    res = 0
    ll = 1
    if x < 0:
        ll = -1
        x = x * -1
    while x:
        res = res * 10 + x%10
        x = x/10
    return res*ll

x = 300
print reverse(x)
