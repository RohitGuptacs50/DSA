class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        has = {n,}
        while True:
            n = sum( int(x)**2 for x in str(n) )
            if n == 1:
                return True
            if n in has:
                return False
            has.add(n)
      
