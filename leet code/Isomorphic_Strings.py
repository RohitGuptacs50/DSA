class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        has = {}
        for i in range(len(s)):
            if s[i] in has and has[s[i]] == t[i]:
                continue
            if s[i] not in has and t[i] not in has.values():
                
                has[s[i]] = t[i]
            else:
                return False
            
        return True
