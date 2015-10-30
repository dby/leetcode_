#!/usr/bin/python

import math
def twoSum(num, target):
    index = []
    numToSort = num[:]
    numToSort.sort()
    i = 0
    j = len(numToSort) - 1
    while i < j:
        if numToSort[i] + numToSort[j] == target:
            for k in range(0, len(num)):
                if num[k] == numToSort[i]:
                    index.append(k)
                    break
            for k in range(len(num)-1, -1, -1):
                if num[k] == numToSort[j]:
                    index.append(k)
                    break
            index.sort()
            break
        elif numToSort[i] + numToSort[j] < target:
            i = i + 1
        elif numToSort[i] + numToSort[j] > target:
            j = j - 1
    print index[0]
    print index[1]
    return (index[0]+1, index[1]+1)

num = [1,4,5,2,3]
tup = ()
tup = twoSum(num, 9)
print tup[:]
