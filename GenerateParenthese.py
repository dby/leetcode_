#!/usr/bin/python

def generateParentThesis(n):
   res = []
   generate(n,n,"",res)
   return res

def generate(left, right, str, res):
    if left == 0 and right == 0:
        res.append(str)
        print "both left and right is zero"
        return res
    if left > 0:
        generate(left-1, right, str+'(', res)
    if left < right:
        if right > 0:
            generate(left, right-1, str+')', res)


print generateParentThesis(3)
