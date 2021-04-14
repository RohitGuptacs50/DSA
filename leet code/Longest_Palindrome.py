class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = collections.Counter(s)
        is_one_count = False
        count = 0
        
        for k, v in dic.items():
            while v >= 2:
                v = v - 2
                count += 2
                
            if v == 1 and not is_one_count:
                count += 1
                is_one_count = True
                
                
        return count
