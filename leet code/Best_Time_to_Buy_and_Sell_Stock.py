class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cost = float("inf")
        
        for i in prices:
            if i < cost:
                cost = i
                
            profit = max(profit, i - cost)
                
        return profit
        
