class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hs = {}
        
        for c in s:
            if c in hs:
                hs[c] += 1
            else:
                hs[c] = 1
                
        hs = sorted(hs.items(), key=lambda x: x[1], reverse=True)
        
        
        
        res = []
        for key, value in hs:
                res.append(key*value)
            
        return "".join(res)
        
