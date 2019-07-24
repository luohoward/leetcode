def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    letters = [0 for i in range(26)]
    
    for i in range(len(s)):
        letters[ord(s[i]) - ord('a')] += 1
        
    for i in range(len(t)):
        letters[ord(t[i]) - ord('a')] -= 1
        
    for value in letters:
        if value != 0:
            return False
        
    return True