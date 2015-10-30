#!/usr/bin/python

import math

def singleNumber(A):
    res = 0
    for i in A:
        res = res ^ i
    print res

b = [1, 2, 2, 3, 3, 4, 4]
singleNumber(b)
