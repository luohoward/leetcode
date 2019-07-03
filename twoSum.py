def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashSet = {}
    
    for i in range(len(nums)):
        hashSet[nums[i]] = i
        
    print(hashSet)
        
    for i in range(len(nums)):
        if target - nums[i] in hashSet and hashSet[target - nums[i]] != i:
            return [i, hashSet[target - nums[i]]]
        
    return []