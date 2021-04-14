class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {}
        for char in s:
            if char not in ht:
                ht[char] = 1
            else:
                ht[char] += 1
                
        
        for idx, char in enumerate(s):
            if ht[char] == 1:
                return idx
            
        return -1
