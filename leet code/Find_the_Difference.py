class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res1 = {}
        res2 = {}
        
        for i in s:
            if i in res1:
                res1[i] += 1
            else:
                res1[i] = 1
                
        for i in t:
            if i in res2:
                res2[i] += 1
            else:
                res2[i] = 1
                
        
        for key, value in res2.items():
            if key not in res1:
                return(key)
                break
                
        for key_s,value_s in res1.items():
            for key_t,value_t in res2.items():
                if key_s == key_t and value_s < value_t:
                    return(key_s)
                    break
