def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    return self._isValidBST(root, -float('inf'), float('inf'))

def _isValidBST(self, root, min, max):
    if not root:
        return True
    
    else:
        if root.val <= min or root.val >= max:
            return False
        
        return self._isValidBST(root.left, min, root.val) and self._isValidBST(root.right, root.val, max)