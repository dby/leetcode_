#!/usr/bin/python

def threeSum(num):
    num.sort()
    r = list()
    for i in xrange(len(num)):
        if i > 0 and num[i] == num[i-1]: continue
        j = i + 1
        k  = len(num) - 1
        while k > j:
            diff = 0 - (num[j] + num[k] + num[i])
            if diff < 0:
                k = k - 1
            elif diff > 0:
                j = j + 1
            else:
                r.append([num[i], num[j], num[k]])
                while j < k and num[j] == num[j+1]: 
                    j = j + 1
                    print "j = %d" % j
                while j < k and num[k] == num[k-1]: k = k - 1
                j, k = j + 1, k - 1
    return r


print threeSum([-1, 0, 1, 2, -1, -4])
