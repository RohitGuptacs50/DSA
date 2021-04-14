class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        
        count = 1
        
        while n > 0:
            n = n - count
            if n < 0:
                return count - 1
            if n == 0:
                return count
            count += 1
        
