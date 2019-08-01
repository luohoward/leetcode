class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        ans = []
        
        while len(queue) != 0:
            node = queue.pop()
            
            if not node:
                ans.append('#')
            else:
                ans.append(str(node.val))
                queue.insert(0, node.left)
                queue.insert(0, node.right)
                
                    
        return  ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        dataClean = data.split(",")
        
        if dataClean[0] == '#':
            return None
        
        n = len(dataClean)
    
        i = 0
        
        root = TreeNode(int(dataClean[i]))
        queueLevelNext = [root]

        i = 1
        
        while i < n:
            
            queueLevelThis = [x for x in queueLevelNext]
            queueLevelNext = []
        
            while queueLevelThis:

                node = queueLevelThis.pop(0)
                
                if dataClean[i] != '#':
                    node.left = TreeNode(int(dataClean[i]))
                    queueLevelNext.append(node.left)

                i = i+1

                if dataClean[i] != '#':
                    node.right = TreeNode(int(dataClean[i]))
                    queueLevelNext.append(node.right)

                i = i+1
        return root