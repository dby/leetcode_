#!/usr/bin/python

class Solution:
    def combine(self, n, k):
        self.res = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.res

    def dfs(self, n, k, m, p, tmp):
        print "n=%d, k=%d, m=%d, p=%d" % (n, k, m, p)
        print "tmp=%s"%tmp
        if k == p:
            self.res.append(tmp[:])
            return 
        for i in range(m, n+1):
            tmp.append(i)
            self.dfs(n, k, i+1, p+1, tmp)
            print "tmp2 = %s" % tmp
            tmp.pop()
            print "tmp3 = %s" % tmp


s = Solution()
k = s.combine(4, 1)
print k
