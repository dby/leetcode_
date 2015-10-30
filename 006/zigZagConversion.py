#!/usr/bin/python
#coding: utf-8

def convert(s,nRows):
    if len(s) == 1 or len(s) == 0 or nRows == 1:
        return s
    res = ""
    minNum = min(nRows , len(s)) + 1
    for i in range(1,minNum):
        flag = 0
        p1 = 2*(nRows - i)
        p2 = 2*(i-1)
        p = i - 1
        res = res + s[p]
        while p < len(s):
            if flag == 0:
                if p1 != 0:
                    p = p + p1 
                    if p >= len(s):
                        break
                    res = res + s[p]
                flag = 1
            else:
                if p2 != 0:
                    p = p + p2 
                    if p >= len(s):
                        break
                    res = res + s[p]
                flag = 0
    return res
s = "AB"
print convert(s,3)
