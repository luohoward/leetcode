# only passes 46/48 tests. needs refinement

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [[root, 0]]
        ans = []
        maxHeight = 0
        
        while len(queue) != 0:
            node, height = queue.pop()
            
            if height > maxHeight:
                break
            
            if not node:
                ans.append(node)
                queue.insert(0, [None, height + 1])
                queue.insert(0, [None, height + 1])
            else:
                ans.append(node.val)
                queue.insert(0, [node.left, height + 1])
                queue.insert(0, [node.right, height + 1])
                
                if height + 1 > maxHeight:
                    maxHeight = height + 1
                    
        return str(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        elements = data.split(",")
        print(elements)
        
        return self.deserializationHelper(elements, 0)
        
    def deserializationHelper(self, data, index):
        if index > len(data) or data[index] is "None":
            return None
        else:
            try:
                node = TreeNode(int(data[index], 10))
                node.left = self.deserializationHelper(data, 2 * index + 1)
                node.right = self.deserializationHelper(data, 2 * index + 2)
                return node
            except ValueError:
                return None