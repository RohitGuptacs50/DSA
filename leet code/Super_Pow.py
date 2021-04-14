class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        str1 = ''
        for i in b:
            str1 += str(i)
            
        
        
        return pow(a, int(str1), 1337)
