def insert(self, intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    
    i = 0
    mergedIntervals = []
    addedNew = False
    
    
    while i < len(intervals):
        if (intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[0]) or (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][0]):
            addedNew = True
            
            minVal = min(intervals[i][0], newInterval[0])
            maxVal = max(intervals[i][1], newInterval[1])
            
            while i < len(intervals):
                if maxVal >= intervals[i][1]:
                    i += 1
                elif maxVal >= intervals[i][0] and maxVal <= intervals[i][1]:
                    maxVal = max(intervals[i][1], maxVal)
                    i += 1
                else:
                    break
            mergedIntervals.append([minVal, maxVal])
            
        else:
            if newInterval[1] < intervals[i][0] and not addedNew:
                addedNew = True
                mergedIntervals.append(newInterval)
                
            mergedIntervals.append(intervals[i])
            i += 1
            
    if not addedNew:
        mergedIntervals.append(newInterval)

    return mergedIntervals