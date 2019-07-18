def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head:
        return None
    
    tortoise = head
    hare = head.next
    
    while hare != None and hare.next != None:
        tortoise = tortoise.next
        hare = hare.next.next
        
    reversePointer = tortoise.next
    tortoise.next = None
    
    reversedList = self.reverse(reversePointer)
    
    
    iter1 = head
    iter2 = reversedList
    
    
    while iter1:
        next1 = iter1.next
        
        next2 = None
        if iter2:
            next2 = iter2.next
        
        iter1.next = iter2
        
        if iter2:
            iter2.next = next1
        
        iter1 = next1
        iter2 = next2
        
    
        
def reverse(self, node):
    prev = None
    
    while node:
        nodeNext = node.next
        node.next = prev
        
        prev = node
        node = nodeNext
        
    return prev