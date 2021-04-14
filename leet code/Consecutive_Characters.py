class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        out=[]
        count=0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count+=1
                out.append(count)
            else:
                count=0
        if out ==[]:
            return 1
        return max(out)+1
