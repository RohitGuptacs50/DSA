class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        prod = 1
        sum1 = 0
        for s1 in s:
            prod = prod * int(s1)
            sum1 += int(s1)
            
        return (prod - sum1)
