class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        Dynamic = [0, 1, 1]
        for i in range(n + 1):
            if n <= len(Dynamic) - 1:
                return Dynamic[n]
            Dynamic.append(Dynamic[i]+Dynamic[i + 1]+Dynamic[i+2])
