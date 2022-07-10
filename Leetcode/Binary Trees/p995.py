## Serialize and Deserialize Binary Tree

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return ''
        
        result = []
        tempQ = [root]
        while tempQ:
            size = len(tempQ)
            for _ in range(size):
                curr = tempQ.pop(0)
                
                if curr:
                    result.append(str(curr.val))
                    tempQ.append(curr.left)
                    tempQ.append(curr.right)
                else:
                    result.append('null')
        
        print(result)
        return ' '.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return 
        
        data = data.split()
        root = TreeNode(int(data[0]))
        tempQ = [root]
        i=1
        while i<len(data):
            curr = tempQ.pop(0)
            
            if data[i]!='null':
                curr.left = TreeNode(int(data[i]))
                tempQ.append(curr.left)
            
            if data[i+1]!='null':
                curr.right = TreeNode(int(data[i+1]))
                tempQ.append(curr.right)
                
            i+=2
            
        return root
            
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))