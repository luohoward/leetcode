class Solution(object):
    def helper(self, tDict, sDict):
        for key in tDict.keys():
            if key not in sDict or sDict[key] < tDict[key]:
                return False
            
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        minLen = float('inf')
        minString = ""
        
        tDict = {}
        
        for i in range(len(t)):
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
        
        sDict = {}
        coreString = ""
        
        
        for i in range(len(s)):
            coreString += s[i]
            
            if s[i] in tDict:
                if s[i] in sDict:
                    sDict[s[i]] += 1
                else:
                    sDict[s[i]] = 1

                    
            while self.helper(tDict, sDict):
                if minLen > len(coreString):
                    minLen = len(coreString)
                    minString = coreString
                    
                if coreString[0] in sDict:
                    sDict[coreString[0]] -= 1
                    
                    if sDict[coreString[0]] == 0:
                        del sDict[coreString[0]]
                        
                coreString = coreString[1:]
                
        return minString