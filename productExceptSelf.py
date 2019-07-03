def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    left = []
    right = []
        
    leftProduct = 1
    rightProduct = 1
    
    for i in range(len(nums)):
        leftProduct *= nums[i]
        left.append(leftProduct)
        
    for i in range(len(nums) - 1, -1, -1):
        rightProduct *= nums[i]
        right.insert(0, rightProduct)
        
    output = [1 for i in range(len(nums))]
    
    output[0] = right[1]
    output[-1] = left[-2]
    
    for i in range(1, len(nums) - 1):
        output[i] = left[i - 1] * right[i + 1]
        
    return output