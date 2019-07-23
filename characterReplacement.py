def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    
    characters = [0 for i in range(26)]
    maxVal = 0
    beginning = 0
    
    for i in range(len(s)):
        characters[ord(s[i]) - ord('A')] += 1
        maxCharacter = max(characters)
        
        if maxCharacter + k < i - beginning + 1:
            characters[ord(s[beginning]) - ord('A')] -= 1
            beginning += 1
        
        maxVal = max(maxVal, len(s) if maxCharacter + k > len(s) else maxCharacter + k)
        
    return maxVal