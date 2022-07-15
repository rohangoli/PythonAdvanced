## 590. N-ary Tree Postorder Traversal

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.result = []
        
        def helper(node):
            if not node:
                return
            
            for child in node.children:
                helper(child)
                
            self.result.append(node.val)
            
        helper(root)
        
        return self.result