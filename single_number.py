class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singleValue = 0
        
        for i in range(len(nums)):
            singleValue ^= nums[i]
            
        return singleValue