def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    dp = [float('inf') for i in range(amount + 1)]
    
    dp[-1] = 0
    
    for i in range(len(dp) - 1, -1, -1):
        for coin in coins:
            if i + coin > amount:
                continue
            else:
                dp[i] = min(dp[i], dp[i + coin] + 1)
                
    if dp[0] == float('inf'):
        return -1
    return dp[0]