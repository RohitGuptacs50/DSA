class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res1 = []
        res2 = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                res1.append(A[i])
            else:
                res2.append(A[i])
                
        res = res1 + res2
        return res
                
        
