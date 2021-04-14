class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        h = {}
        
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
                
        res = []
        
        for i in range(1, len(nums) + 1):
            if i not in h:
                res.append(i)
                
        return res
        
