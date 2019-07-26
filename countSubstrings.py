def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    dp = [[False for j in range(len(s) + 1)] for i in range(len(s) + 1)]
    
    for i in range(len(s)):
        dp[i][i] = True
        
    total = 0
        
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if j - i == 0:
                pass
            elif j - i == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[j] == s[i] and dp[i + 1][j - 1]
                
            if dp[i][j]:
                total += 1
                
    return total