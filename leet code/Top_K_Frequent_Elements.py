class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        res = {}
        
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
                
        
        res = sorted(res.items(), key=lambda x: x[1], reverse=True)
        
        return [res[i][0] for i in range(k)]
