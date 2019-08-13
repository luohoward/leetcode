class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        kFrequent = {}
        for i in range(len(nums)):
            if nums[i] not in kFrequent:
                kFrequent[nums[i]] = 1
            else:
                kFrequent[nums[i]] += 1
                
        frequency = {}
        
        for key, value in kFrequent.items():
            if value not in frequency:
                frequency[value] = [key]
            else:
                frequency[value].append(key)
        
        kFrequent = []
        i = 0
        numPushed = 0
        
        keys = sorted(frequency.keys())
        
        while numPushed < k:
            key = keys[-1 - i]
            
            for value in frequency[key]:
                kFrequent.append(value)
                numPushed += 1
                
            i += 1
            
        return kFrequent