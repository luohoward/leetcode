def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    temp = ListNode(0)
    temp.next = head
    
    self.helper(temp, n)
    
    return temp.next
    
    


def helper(self, head, n):
    if not head:
        return 0
    
    else:
        nextNode = self.helper(head.next, n) + 1
        if nextNode == n + 1:
            head.next = head.next.next
            
        
        return nextNode