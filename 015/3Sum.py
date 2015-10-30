#!/usr/bin/python
#coding:utf-8

def threeSum(num):
    num.sort()
    res = list()
    for i in range(0, len(num) - 1):
        for j in range(0, len(num) - 1):
            num2 = sorted(num)
            print "num is %s" % num
            print "i , j is %d %d" % (i, j)
            if i >= j:
                continue
            s = num[i] + num[j]
            s = s * (-1)
            print "num[i], num[j], s is %d %d %d" % (num[i], num[j], s)
            num2.remove(num[i])
            num2.remove(num[j])
            if s in num2:
                r = list()
                r.append(num[i])
                r.append(num[j])
                r.append(s)
                r.sort()
                if r not in res:
                    res.append(r)

    return res


print threeSum([-1, 0 , 1, 2, -1, -4])
