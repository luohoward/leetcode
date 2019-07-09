def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    
    words = [[0 for i in range(len(s) + 2)] for j in range(len(s) + 1)]
    
    for i in range(len(s) -1, -1, -1):
        for j in range(len(s), i, -1):
            if s[i:j] not in wordDict:
                words[i][j] = words[i][j+1]
            else:
                words[i][j] = max(words[i][j+1], words[j][j+1] + (j - i))
    
    return words[0][1] == len(s)