def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 0:
        return ""
    
    
    dp = [[False for i in range(len(s) + 1)] for j in range(len(s) + 1)]
    
    for i in range(len(s)):
        dp[i][i] = True
        
    maxLen = 1
    maxString = s[0]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if j == i:
                continue
            elif j - i == 1:
                if maxLen <= j - i + 1 and s[i] == s[j]:
                    maxLen = j - i + 1
                    maxString = s[i: j + 1]
                
                dp[i][j] = s[i] == s[j]
            else:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    if maxLen <= j - i + 1:
                        maxLen = j - i + 1
                        maxString = s[i: j + 1]
                        
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

    return maxString