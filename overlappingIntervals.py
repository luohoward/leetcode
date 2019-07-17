# this doesnt work fully. what i came up with in 45 min

def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) <= 1:
        return 0
    
    intervals.sort(key = lambda x:(x[0],x[1]))
    
    i = 0
    j = 1
    
    count = 0
    
    while i < len(intervals):
        while j < len(intervals) and intervals[j][0] >= intervals[i][0] and intervals[j][0] < intervals[i][1]:
            count += 1
            j += 1
            
        i = j
        j += 1
        
    return count