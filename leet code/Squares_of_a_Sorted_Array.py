class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = [x*x for x in A]
        a.sort()
        return a
