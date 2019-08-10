def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if len(preorder) != 0:
        if preorder[0] in inorder:
            nodeVal = preorder.pop(0)
            index = inorder.index(nodeVal)
            
            node = TreeNode(nodeVal)
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node
        else:
            return None
        
    return None