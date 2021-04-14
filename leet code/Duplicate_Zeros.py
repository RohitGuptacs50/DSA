class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] != 0:
                i += 1
            else:
                arr[i+2:], arr[i+1] = arr[i+1:len(arr)-1], 0
                i += 2
            
        
