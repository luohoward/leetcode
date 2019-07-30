def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    node = self.generateTrees(root)
    stack = [node]
    maxVal = -float('inf')
    
    while len(stack) != 0:
        popped = stack.pop()
        if not popped:
            continue
        else:
            if popped.val[0] > maxVal:
                maxVal = popped.val[0]
                
            if popped.val[1] > maxVal:
                maxVal = popped.val[1]
            stack.append(popped.right)
            stack.append(popped.left)
            
    return maxVal

    
def generateTrees(self, root):
    if not root:
        return None
    
    else:
        left = self.generateTrees(root.left)
        right = self.generateTrees(root.right)
        
        leftVal = 0
        if left:
            leftVal = left.val[0]
            
        rightVal = 0
        if right:
            rightVal = right.val[0]
            
        node = TreeNode([root.val + max(leftVal, rightVal, 0), root.val + leftVal + rightVal])
        node.left = left
        node.right = right
        
        return node