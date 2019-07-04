def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    
    return self.findMinHelper(0, len(nums) - 1, nums)
    
    
def findMinHelper(self, lo, hi, nums):
    if lo == hi:
        return nums[lo]
    
    if hi - lo == 1:
        return min(nums[lo], nums[hi])
    
    mid = (lo + hi)/2
    
    if nums[lo] > nums[hi]:
        if nums[hi] > nums[mid]:
            return self.findMinHelper(lo, mid, nums)
        else:
            return self.findMinHelper(mid, hi, nums)
    else:
        return self.findMinHelper(lo, mid, nums)