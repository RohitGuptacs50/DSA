class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''.join([str(x) for x in nums])
        return len(max(s.split('0')))
        
