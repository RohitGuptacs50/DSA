import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = math.sqrt(x)
        
        return math.trunc(res)
        
