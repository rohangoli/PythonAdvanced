## 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 
        
        self.maxS = root.val
        
        ## Neetcode Implementation
        def dfs(Node):
            if not Node:
                return 0
            
            leftMax = dfs(Node.left)
            leftMax = max(leftMax,0)
            rightMax = dfs(Node.right)
            rightMax = max(rightMax, 0)
            
            self.maxS = max(self.maxS, Node.val+leftMax+rightMax)
            
            return Node.val + max(leftMax, rightMax)
        
        dfs(root)
        
        ## Self Implementation, Test Case - FAIL
#         def helper(Node):
#             #print(Node)
#             if not Node:
#                 return 0
            
#             if not Node.left and not Node.right:
#                 self.maxS = max(self.maxS, Node.val)
#                 #print(self.maxS)
#                 return Node.val
            
#             leftSum = helper(Node.left)
#             rightSum = helper(Node.right)
#             currSum = max(Node.val, Node.val + leftSum + rightSum, Node.val+leftSum, Node.val+rightSum)
#             # maxCSum = max(currSum, leftSum, rightSum)
#             self.maxS = max(self.maxS, currSum)
#             #print(self.maxS)
            
#             return currSum
        
#         helper(root)
        
        return self.maxS