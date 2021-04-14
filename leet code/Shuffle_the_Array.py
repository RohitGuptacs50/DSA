class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:n]
        y = nums[n:]
        arr = []
        for i in range(n):
            arr.append(x[i])
            arr.append(y[i])
        return(arr)     
