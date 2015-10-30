#!/usr/bin/python

def threeSum(num):
    num.sort()
    r = [] 
    for i in range(0,len(num)):
        if i > 0 and num[i] == num[i-1]:
            continue
        for l in range(i+1, len(num)):
            if l > i+1 and num[l] == num[l-1]:
                continue
            j, k = l + 1, len(num) - 1
            while k > j:
                diff = 0 - (num[j] + num[k] + num[i] + num[l])
                if diff < 0:
                    k = k - 1
                elif diff > 0:
                    j = j + 1
                else:
                    r.append([num[i],num[l], num[j], num[k]])
                    while j < k and num[j] == num[j+1]: 
                        j = j + 1
                    while j < k and num[k] == num[k-1]: k = k - 1
                    j, k = j + 1, k - 1
    return r


print threeSum([1, 0, -1, 0, -2, 2])
