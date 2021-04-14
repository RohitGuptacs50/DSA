class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        res = {}
        for s in J:
            if s in res:
                res[s] += 1
            else:
                res[s] = 1
                
        for a in S:
            if a in res:
                count += 1
                
        return count
            
