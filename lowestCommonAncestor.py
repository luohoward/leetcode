def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    
    self.lca = None
    self._lca(root, p, q)
    return self.lca

def _lca(self, root, p, q):
    if root == None:
        return [False, False]
    
    else:
        lookleft = self._lca(root.left, p, q)
        lookright = self._lca(root.right, p, q)
        
        seenPQ = [False, False]
        
        seenPQ[0] = lookleft[0] or lookright[0] or (root.val == p.val)
        seenPQ[1] = lookleft[1] or lookright[1] or (root.val == q.val)
        
        
        if seenPQ[0] and seenPQ[1] and self.lca == None:
            self.lca = root
            
        return seenPQ