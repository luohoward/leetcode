def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    staircase = [0 for i in range(n + 1)]
    
    staircase[0] = 1
    for i in range(1, len(staircase)):
        if i == 1:
            staircase[i] = staircase[i - 1]
        else:
            staircase[i] = staircase[i - 1] + staircase[i - 2]
    
    return staircase[-1]