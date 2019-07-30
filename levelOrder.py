def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    queue = [[root, 1]]
    
    ans = []
    
    while len(queue) != 0:
        node, level = queue.pop()
        
        if not node:
            continue
        else:
            if level > len(ans):
                ans.append([node.val])
                
            else:
                ans[level - 1].append(node.val)
                
            queue.insert(0, [node.left, level + 1])
            queue.insert(0, [node.right, level + 1])
            
    return ans