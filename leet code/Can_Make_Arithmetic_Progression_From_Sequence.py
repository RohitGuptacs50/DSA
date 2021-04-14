class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        d=arr[0]-arr[1]
        for i in range(len(arr)-1):
            d1=arr[i]-arr[i+1]
            if d1==d:
                continue
            else:
                return False
        return True
        
