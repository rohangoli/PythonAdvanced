## 589. N-ary Tree Preorder Traversal

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.result = []
        def helper(node):
            if not node:
                return 
            self.result.append(node.val)
            
            for child in node.children:
                helper(child)
                
        helper(root)
        
        return self.result