#!/usr/bin/python
#coding: utf-8
import math

def longestPalindrome(s):
    # 二维数组
    dp = [[-1 for col in range(len(s))] for row in range(len(s))]

    #dp = [[-1]*len(s)] +[[-1]*len(s)]
    print dp
    

    maxLen = 0 #回文字符串的长度
    le = 0     #回文字符串的左边界
    ri = 0     #回文字符串的右边界

    if len(s) == 0:
        return "";
    elif len(s) == 1:
        return s;

    for i in range(len(s)):
        for j in range(len(s)):
            if i >= j:
                dp[i][j] = 1 #当i == j时，认为是只有一个字符 i<j时，为空串，空串默认为回文字符串
            else:
                dp[i][j] = 0


    for k in range(1,len(s)):
        for i in range(0,len(s)):
            j = k + i
            if j >= len(s):
                break
            if s[i] != s[j]:
                dp[i][j] = 0
            else: #如果当s[i] == s[j]，回文字符串由dp[i+1[j-1]决定
                dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    if (j-i+1) > maxLen:
                        maxLen = j - i + 1;
                        ri = j
                        le = i
    return s[le:ri+1]


s = "abcba"
print longestPalindrome(s)
