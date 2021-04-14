class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        ht = {}
        for idx, num in enumerate(nums):
            if num in ht:
                if (idx - ht[num]) <= k:
                    return True
                
            
            ht[num] = idx
                
        return False
        
