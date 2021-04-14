class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d1 = {}
        
        for i in arr:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
                
        res = []
        
        for key in d1:
            if key == d1[key]:
                res.append(key)
                
        if len(res) == 0:
            return -1
        else:
            return max(res)
