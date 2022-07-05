## Maximum Depth of Binary Tree

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ## Top-Down Approach
        def helper(Node, depth):
            if not Node:
                return depth
            else:
                return max(helper(Node.left,depth+1), helper(Node.right, depth+1))
            
        ## Bottom-Up Approach
        def helper2(Node):
            if not Node:
                return 0
            else:
                return max(helper2(Node.right), helper2(Node.left))+1
            
        #return helper(root,0)
        return helper2(root)
