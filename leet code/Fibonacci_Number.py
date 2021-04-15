class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        F0 = 0
        F1 = 1
        if N == 0:
            return F0
        elif N == 1:
            return F1
        else:
            for i in range(2,N + 1):
                f = F1 + F0
                
                F0 = F1
                F1 = f
            return f
    
