class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = [str(i) for i in digits]
        
        res = int(''.join(s))
        
        res = res + 1
        
        
        res1 = [int(d) for d in str(res)]
        return res1
