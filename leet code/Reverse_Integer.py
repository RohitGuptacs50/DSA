class Solution(object):
    def reverse(self, x):
        
        self.x = x
        y = str(self.x)
        
        if y[0] == '-':
            y = y[-1:0:-1]
            y = int('-' + y)
        else:
            y = y[::-1]
            y = int(y)
            
        if y >= -2**31 and y <= (2**31-1):
            return y
        else:
            return 0
        
