class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        l = []
        A = A.split(' ')
        B = B.split(' ')
        A_dict = {}
        B_dict = {}
        for i in A:
            if i not in A_dict:
                A_dict[i] = 1
            else:
                A_dict[i] += 1
                
        for i in B:
            if i not in B_dict:
                B_dict[i] = 1
            else:
                B_dict[i] += 1
                
        for i in A_dict:
            if i not in B_dict and A_dict[i] == 1:
                l.append(i)
        
        for i in B_dict:
            if i not in A_dict and B_dict[i] == 1:
                l.append(i)
                
        return l
