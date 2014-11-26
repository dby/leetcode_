#!/usr/bin/python

def longestCommonPrefix(strs):
    slen = 0
    if len(strs) == 0:
        return ""
    
    prefix = strs[0]
    for s in strs:
        if len(s) == 0 or len(prefix) == 0:
            return "" 
        slen = len(s) if len(s) < len(prefix) else len(prefix)
        print "s is %s, prefix is %s" % (s, prefix)
        print "slen is %d" % slen
        j = 0
        for i in range(0, slen):
            print "j %d" % j
            if s[i] == prefix[i]:
                j = j + 1
            else:
                break

        prefix = s[0:j]
        print "prefix 22 is %s" % prefix

    return prefix

strs = ["aaa","aa","aaa"]
print longestCommonPrefix(strs)
