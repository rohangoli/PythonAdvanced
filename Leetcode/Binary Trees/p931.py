## Binary Tree Level Order Traversal

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if not root:
            return 
        
        tempQ = [root]
        while tempQ:
            size = len(tempQ)
            for i in range(size):
                curr = tempQ.pop(0)
                
                if i==0:
                    result.append([])
                
                if curr:
                    result[-1].append(curr.val)
                    if curr.left:
                        tempQ.append(curr.left)
                    if curr.right:
                        tempQ.append(curr.right)
        
        return result