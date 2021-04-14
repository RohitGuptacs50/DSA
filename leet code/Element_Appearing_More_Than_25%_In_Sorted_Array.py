class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        h1 = {}
        n = len(arr)
        
        for i in arr:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1
        
        for i in h1:
            if h1[i] > n/4:
                return i
