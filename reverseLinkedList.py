def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    return self.reverseListHelper(head, None)
    
def reverseListHelper(self, head, prev):
    if head == None:
        return prev
    
    next = head.next
    head.next = prev
    
    return self.reverseListHelper(next, head)