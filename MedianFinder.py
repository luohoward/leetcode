import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        self.median = 0.0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if num > self.median:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
            
        if len(self.minHeap) - len(self.maxHeap) == 2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            
        if len(self.maxHeap) - len(self.minHeap) == 2:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 1:
            if len(self.maxHeap) > len(self.minHeap):
                self.median = float(-self.maxHeap[0])
            else:
                self.median = float(self.minHeap[0])
                
        else:
            self.median = (self.minHeap[0] + (-self.maxHeap[0])) / 2.0
            
        

    def findMedian(self):
        """
        :rtype: float
        """
        
        return self.median