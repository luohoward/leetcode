def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    nums.sort()
    zeroSums = set()
    
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                zeroSums.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
                
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
                
            else:
                j += 1
            
    l = []
    for i in zeroSums:
        l.append(list(i))
        
    return l