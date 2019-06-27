def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if len(nums) == 0:
        return 0
    
    i = 0
    maxValue = -float('inf')
    runningMax = 0
    
    while i < len(nums):
        if nums[i] > runningMax + nums[i]:
            runningMax = nums[i]
        else:
            runningMax += nums[i]
            
        maxValue = max(runningMax, maxValue)
        i += 1
        
    return maxValue