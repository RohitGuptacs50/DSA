class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for y in range(1, amount + 1):
            for coin in coins:
                
                if y < coin :
                    continue
                
                dp[y] = min(dp[y], dp[y - coin] + 1)
                
        if dp[-1] == float("inf"):
            return -1
        
        return dp[-1]
            
