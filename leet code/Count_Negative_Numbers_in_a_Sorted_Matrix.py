class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        count = 0
        for row in grid:
            for i, num in enumerate(row):
                if (num < 0):
                    count += len(row[i:])
                    break
        return count
        
