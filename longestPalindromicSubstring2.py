#!/usr/bin/python
import math
# the algorithm called Manacher's Algorithm

def preProcess(s):
    res = '^#'
    for i in s:
        res = res + i
        res = res + '#'
    res = res + '$'
    return res

def longestPalindrome(s):
   sPreProcess = preProcess(s)
   p =[0]*len(sPreProcess)
   c = 0 #center
   r = 0
   for i in range(0, len(sPreProcess)-1):
       i_mirror = 2*c-i
       if r > i:
           p[i] = min(r-i, p[i_mirror]) 
       else:
           p[i] = 0
       while sPreProcess[i+p[i]] == sPreProcess[i-p[i]]:
           p[i] = p[i] + 1
       if i + p[i] > r:
           r = i + p[i]
           c = i
   maxLen = 0
   index = 0
   for i in range(len(sPreProcess)):
       if p[i] > maxLen:
           maxLen = p[i]
           index = i
   print "index, maxLen = %d,%d"%(index,maxLen)
   return s[(index-maxLen)/2:(index-maxLen)/2+maxLen-1]


s = "1234321345"
print longestPalindrome(s)
