def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if s == None:
        return False
    
    if s.val == t.val and self.isSubtreeHelper(s, t):
        return True
    
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    
def isSubtreeHelper(self, s, t):
    if not s and not t:
        return True
    
    elif not s and t:
        return False
    
    elif s and not t:
        return False
    
    else:
        if s.val != t.val:
            return False
        
        else:
            return self.isSubtreeHelper(s.left, t.left) and self.isSubtreeHelper(s.right, t.right)