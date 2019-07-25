def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    d = {}
    
    for s in strs:
        letters = [0 for i in range(26)]
        
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            
        si = ""    
        for i in range(len(letters)):
            si += str(letters[i])
            
        if si in d:
            d[si].append(s)
        else:
            d[si] = [s]
            
    return d.values()