class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = set()
        for index, num in enumerate(numbers):
            if target - num in seen:
                break
            else:
                seen.add(num)
                
        for index2, num2 in enumerate(numbers):
            if num2 == target - num and index != index2:
                return [index2 + 1, index + 1]
        
        
