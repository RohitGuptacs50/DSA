class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr[0] == 0 and arr[1] == 0:
            return True
        d1 = {}
        for number in arr:
            d1[2*number] = True
        for number in arr:
            
            if number in d1 and number != 0:
                return True
        return False
