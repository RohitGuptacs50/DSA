class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        has = {}
        s1 = s.split(" ")
        if len(pattern) != len(s1):
            return False
        for i in range(len(pattern)):
            if pattern[i] in has and has[pattern[i]] == s1[i]:
                continue
            if pattern[i] not in has and s1[i] not in has.values():
                has[pattern[i]] = s1[i]
            else:
                return False
            
        return True
