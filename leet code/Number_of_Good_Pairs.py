class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        num = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                num += d[i]
                d[i] += 1
                
        return num
        
