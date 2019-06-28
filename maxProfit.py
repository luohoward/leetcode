def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    
    maxProfit = 0
    maxSoFar = -float('inf')
    
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > maxSoFar:
            maxSoFar = prices[i]
        
        if maxSoFar - prices[i] > maxProfit:
            maxProfit = maxSoFar - prices[i]

    return maxProfit