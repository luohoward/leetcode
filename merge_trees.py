# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 == None and t2 == None:
            return None
        
        elif t1 != None and t2 == None:
            root = TreeNode(t1.val)
            root.left = self.mergeTrees(t1.left, t2)
            root.right = self.mergeTrees(t1.right, t2)
            return root
        
        elif t1 == None and t2 != None:
            root = TreeNode(t2.val)
            root.left = self.mergeTrees(t1, t2.left)
            root.right = self.mergeTrees(t1, t2.right)
            return root
        
        else:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root