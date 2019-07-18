def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and not l2:
        return None
    
    elif l1 and not l2:
        return l1
    
    elif not l1 and l2:
        return l2
    
    else:
        if l1.val < l2.val:
            nextNode = l1.next
            l1.next = self.mergeTwoLists(nextNode, l2)
            
            return l1
        else:
            nextNode = l2.next
            l2.next = self.mergeTwoLists(l1, nextNode)
            
            return l2