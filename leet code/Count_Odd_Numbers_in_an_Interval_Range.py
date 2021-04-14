class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        res = 0
        if low %2 == 1 or high%2 ==1:
            res+=1
        return int((high-low)/2)+res
