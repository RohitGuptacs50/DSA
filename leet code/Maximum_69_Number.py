class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = ''
        nums = str(num)
        for i in range(len(nums)):
            if nums[i] != '9':
                ans+='9'                
                ans+=nums[i+1:]
                break
            else:
                ans+=nums[i]
        return int(ans)
        
