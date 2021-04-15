class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        y = str(self.x)
        if y[0] == '-':
            return False
        y = y[::-1]
        y = int(y)
        if y == self.x:
            return True
        else: 
            return False
        
