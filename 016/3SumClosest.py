#!/usr/bin/python

def threeSum(num, target):
    num.sort()
    r = -1000
    res = -1000
    for i in range(0, len(num)):
        print "i is %d" % i
        if i > 0 and num[i] == num[i-1]: continue
        j = i + 1
        k  = len(num) - 1
        while k > j:
            d = target - (num[j] + num[k] + num[i])
            print "i %d, j %d, k %d, num[i] %d, num[j] %d, num[k] %d, res  %d" % (i,j,k,num[i],num[j],num[k], res)
            r = target - res
            if d < 0:
                if abs(r) > abs(d):
                    res = num[i] + num[j] + num[k]
                k = k - 1
            elif d > 0:
                if abs(r) > abs(d):
                    res = num[i] + num[j] + num[k]
                j = j + 1
            else:
                return target
    return res

s = [1, 1, 1, 0]
print threeSum(s, 100)
