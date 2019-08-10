def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    self.node = None
    self._kthSmallest(root, k, -float('inf'))
    return self.node    
        
def _kthSmallest(self, root, k, count):
    if root == None:
        return 0
    
    count = max(self._kthSmallest(root.left, k, count), count)
    
    count += 1
    
    if count == k:
        self.node = root.val
        
    count = max(self._kthSmallest(root.right, k, count), count)
    
    return count