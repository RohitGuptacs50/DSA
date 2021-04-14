class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        s = ''
        for i in A:
            s += str(i)
            
        num = int(s)
        
        res1 = str(num + K)
        
        res = []
        
        for j in res1:
            res.append(int(j))
            
        return res
