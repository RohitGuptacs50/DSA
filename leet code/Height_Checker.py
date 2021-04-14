class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        b = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != b[i]:
                count += 1
                
        return count
        
