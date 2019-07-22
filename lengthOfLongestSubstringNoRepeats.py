def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    letterIndex = {}
    
    minLetter = -1
    maxVal = 0
    
    for i in range(len(s)):
        if s[i] in letterIndex:
            minLetter = max(minLetter, letterIndex[s[i]])
            letterIndex[s[i]] = i
        else:
            letterIndex[s[i]] = i
            
        if i - minLetter > maxVal:
            print(minLetter, i)
            print(letterIndex)
            
            maxVal = i - minLetter
            
    return maxVal