def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    
    rob1 = [0 for i in range(len(nums))]
    rob2 = [0 for i in range(len(nums))]
    
    for i in range(len(rob1) - 2, -1, -1):
        iPlus1 = 0
        iPlus2 = 0
        
        if i + 1 < len(rob1):
            iPlus1 = rob1[i+1]
            
        if i + 2 < len(rob1):
            iPlus2 = rob1[i+2]
            
        print(nums[i])
            
        rob1[i] = max(iPlus1, iPlus2 + nums[i])
        
    for i in range(len(rob2) - 1, 0, -1):
        iPlus1 = 0
        iPlus2 = 0
        
        if i + 1 < len(rob2):
            iPlus1 = rob2[i+1]
            
        if i + 2 < len(rob2):
            iPlus2 = rob2[i+2]
            
        print(nums[i])
            
        rob2[i] = max(iPlus1, iPlus2 + nums[i])
    
    return max(rob1[0], rob2[1])