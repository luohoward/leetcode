def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.insert(0, -100000000000000)
    numsDP = [[0 for j in range(len(nums) + 1)] for i in range(len(nums) + 1)]
    
    for i in range(len(nums)):
        numsDP[i][i] = 1
    
    for i in range(len(nums) -1, -1, -1):
        for j in range(len(nums) - 1, i - 1, -1):
            if nums[i] >= nums[j]:
                numsDP[i][j] = numsDP[i][j+1]
            else:
                numsDP[i][j] = max(numsDP[i][j+1], 1 + numsDP[j][j+1])
                
    return numsDP[0][1]