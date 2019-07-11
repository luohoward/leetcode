def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 1:
        return True
    
    dp = [0 for i in range(len(nums))]
    dp[-1] = 1
    
    for i in range(len(nums) - 2, -1, -1):
        for j in range(nums[i] + 1):
            if i + j >= len(nums):
                continue
            else:
                dp[i] = max(dp[i], dp[i + j])
                
    return not (dp[0] == 0)

def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        
        lastPos = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
                    
        return lastPos == 0