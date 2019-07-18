def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if lists == []:
        return None
    
    head = None
    i = self.findMinVal(lists)
    iter = lists[i]
    
    while i != -1:
        if not head:
            head = lists[i]
            
        temp = lists[i]
        lists[i] = temp.next
        iter.next = temp
        iter = iter.next            
        i = self.findMinVal(lists)

    if iter:
        iter.next = None
    
    return head
    
    
def findMinVal(self, lists):
    index = -1
    minVal = float('inf')
    
    for i in range(len(lists)):
        if lists[i]:
            if lists[i].val < minVal:
                minVal = lists[i].val
                index = i
            
    return index