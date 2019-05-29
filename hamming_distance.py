class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        xBits = [int(i) for i in bin(x)[2:]]
        yBits = [int(i) for i in bin(y)[2:]]
        
        i = len(xBits) - 1
        j = len(yBits) - 1
        
        hammingDistance = 0
        
        while i >= 0 and j >= 0:
            if xBits[i] != yBits[j]:
                hammingDistance += 1
            
            i -= 1
            j -= 1
            
        if i >= 0:
            while i >= 0:
                if xBits[i] == 1:
                    hammingDistance += 1
            
                i -= 1
            
        if j >= 0:
            while j >= 0:
                if yBits[j] == 1:
                    hammingDistance += 1
            
                j -= 1
                
        return hammingDistance