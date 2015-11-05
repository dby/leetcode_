class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i, n in enumerate(nums):
            if d.has_key(n):
                return (d[n]+1, i+1)
            else:
                d[target-n] = i
        return (0,0)

if __name__ == '__main__':
    num = [1, 4, 5, 2, 3]
    tup = ()
    tup = Solution().twoSum(num, 9)
    print tup