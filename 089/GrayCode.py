#!/usr/bin/python

def grayCode(n):
    res = []
    s = 1 << n
    for i in range(s):
        print ("i is %s, i>>1 is %s, (i>>1)^i is %s") % (i, i>>1, (i>>1)^i)
        res.append((i>>1)^i)
    return res

print grayCode(0)
print ""
print grayCode(1)
print ""
#print grayCode(2)
#print ""
#print grayCode(3)
#print ""
#print grayCode(4)
