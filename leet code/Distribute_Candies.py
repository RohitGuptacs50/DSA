class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        has = {}
        
        for ct in candyType:
            if ct in has:
                has[ct] += 1
            else:
                has[ct] = 1
        
        n = len(candyType) / 2
        
        if n == len(has):
            return n
        elif len(has) < n:
            return len(has)
        else:
            return n
