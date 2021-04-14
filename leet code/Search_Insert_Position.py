class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_index = 0
        last_index = len(nums) - 1
        while start_index <= last_index:
            mid = (start_index + last_index)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                last_index = mid - 1
            elif target > nums[mid]:
                start_index = mid + 1
            
        return start_index
