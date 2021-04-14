class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        has = {}
        
        for a in nums:
            if a in has:
                has[a] += 1
            else:
                has[a] = 1
                
        for key, value in has.items():
            if value > 1:
                return key
