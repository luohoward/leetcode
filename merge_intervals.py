def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    
    if len(intervals) == 0:
        return []
    
    intervals.sort(key=lambda x:[x[0],x[1]])
    nonoverlappingIntervals = []
    
    lo = intervals[0][0]
    hi = intervals[0][1]
    
    for i in range(1, len(intervals)):            
        if intervals[i][0] <= hi:
            lo = min(intervals[i][0], lo)
            hi = max(intervals[i][1], hi)
        else:
            nonoverlappingIntervals.append([lo, hi])
            lo = intervals[i][0]
            hi = intervals[i][1]
            
    nonoverlappingIntervals.append([lo, hi])
    
    return nonoverlappingIntervals