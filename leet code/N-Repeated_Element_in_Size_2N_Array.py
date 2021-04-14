class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = {}
        for i in A:
            if i not in l:
                l[i] = 1
            else:
                l[i] += 1
                
        
        for i in l:
            if l[i] == len(A)/2:
                return i
