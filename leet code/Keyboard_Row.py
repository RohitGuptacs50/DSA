class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        
        l1 = []
        l2 = []
        l3 = []
        
        res = []
        
        for word in words:
            for letter in word.lower():
                if letter in r1:
                    l1.append(letter)
                elif letter in r2:
                    l2.append(letter)
                    
                elif letter in r3:
                    l3.append(letter)
                    
            if (len(l1) == 0 and len(l2) == 0) or (len(l2) == 0 and len(l3) == 0) or (len(l3) == 0 and len(l1) == 0):
                res.append(word)
            
            l1 = []
            l2 = []
            l3 = []
            
        return res
