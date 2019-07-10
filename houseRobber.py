def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    
    robCount = [0 for i in range(len(nums))]
    
    for i in range(len(nums) - 1, -1, -1):
        
        iPlus1 = 0
        iPlus2 = 0
        
        if i + 1 < len(nums):
            iPlus1 = robCount[i+1]
            
        if i + 2 < len(nums):
            iPlus2 = robCount[i+2]

        robCount[i] = max(iPlus1, nums[i] + iPlus2)

    
    return robCount[0]