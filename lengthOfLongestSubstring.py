#!/usr/bin/python
import math

def lengthOfLongestSubstring(s):
    max = 0
    temp = 0
    sign = [0]*300
    
    for i in range(0, len(s)):
        if sign[(ord)(s[i]) - (ord)('a')] == 0:
            temp = temp + 1
            sign[(ord)(s[i]) - (ord)('a')] = 1
        else:
            sign = [0]*300
            max = max if max > temp else temp
            sign[(ord)(s[i]) - (ord)('a')] = 1
            temp = 1
    max = max if max > temp else temp
    return max

s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
print lengthOfLongestSubstring(s)
