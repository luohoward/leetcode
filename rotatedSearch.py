def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    
    return self.searchHelper(nums, 0, len(nums) - 1, target)
    
    
def searchHelper(self, nums, lo, hi, target):
    if lo == hi:
        if nums[lo] == target:
            return lo
        else:
            return -1
        
    
    if hi - lo == 1:
        if nums[lo] == target:
            return lo
        elif nums[hi] == target:
            return hi
        else:
            return -1
    
    mid = (lo + hi)/2
        
    # one side of the array has to be sorted
    if nums[lo] < nums[hi]:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.searchHelper(nums, mid, hi, target)
        else:
            return self.searchHelper(nums, lo, mid, target)
        
    else:
        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[lo]:
            if target < nums[mid] and target >= nums[lo]:
                return self.searchHelper(nums, lo, mid, target)
            return self.searchHelper(nums, mid, hi, target)
            
        else:
            if nums[hi] >= target and target > nums[mid]:
                return self.searchHelper(nums, mid, hi, target)
            else:
                return self.searchHelper(nums, lo, mid, target)
            