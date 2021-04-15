class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == 0 and len(B) == 0:
            return True
        
        for i in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
            
        return False
