import re

class Solution(object):
    """docstring for Solution"""
    def isPalindrome(self, s):
        s1 = "".join(re.findall(r"\w*", s)).lower()
        s2 = s1[::-1]
        return True if s2 == s1 else False
        

if __name__ == '__main__':
    print Solution().isPalindrome("A man, a plan, a canal: Panama")