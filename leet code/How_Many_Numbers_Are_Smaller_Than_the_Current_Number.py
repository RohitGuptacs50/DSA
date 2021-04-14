class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = sorted(nums)
        m = {}
        for i in range(len(t)):
            if t[i] not in m:
                m[t[i]] = i
        return [m[i] for i in nums]
