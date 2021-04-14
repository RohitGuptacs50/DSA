class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem not in hash_table:
                hash_table[nums[i]] = i
            else:
                return (hash_table[rem], i)
        
