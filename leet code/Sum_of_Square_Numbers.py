class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        seen = set()
        pos = 0
        while True:
            x = pos**2
            seen.add(x)
            if c - x in seen:
                return True
            if x > c:
                return False
            pos += 1
