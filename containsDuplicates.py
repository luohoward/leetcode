def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dictionary = {}
    
    for i in nums:
        if i in dictionary:
            dictionary[i] += 1
            
        else:
            dictionary[i] = 1
            
    for key, value in dictionary.items():
        if value > 1:
            return True
        
    return False