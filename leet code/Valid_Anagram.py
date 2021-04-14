class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sdict = collections.Counter(s)
        tdict = collections.Counter(t)
        
        return(len(sdict - tdict) == 0)
        
