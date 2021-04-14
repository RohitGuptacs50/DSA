class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        i = 0
        total = 0
        while total < n:
            total = 3 ** i
            i += 1
            
        if total == n:
            return True
        else:
            return False
