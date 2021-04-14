class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h = {}
        
        for a in nums:
            if a in h:
                h[a] += 1
                
            else:
                h[a] = 1
                
        res = []
        
        for key in h:
            if h[key] == 2:
                res.append(key)
                
        return res
