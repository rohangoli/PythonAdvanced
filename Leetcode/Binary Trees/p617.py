## Merge Two Binary Trees

# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         if not root1 and not root2:
#             return None
        
#         if not root1:
#             return root2
        
#         if not root2:
#             return root1
        
        def helper(node1, node2):
            if not node1 and not node2:
                return None
            
            if not node1 and node2:
                return node2 #TreeNode(node2.val)
            
            if not node2 and node1:
                return node1 #TreeNode(node1.val)
            
            
            node = TreeNode(node1.val + node2.val)
            node.left = helper(node1.left, node2.left)
            node.right = helper( node1.right, node2.right)

            return node
        
        return helper(root1, root2)
        
        