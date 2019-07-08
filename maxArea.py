def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    
    low = 0
    hi = len(height) - 1
    maxArea = 0
    
    while low < hi:
        maxArea = max(min(height[low], height[hi]) * (hi - low), maxArea)
        
        if height[low] < height[hi]:
            low += 1
            
        else:
            hi -= 1
            
    return maxArea