## 145. Binary Tree Postorder Traversal

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         result = []
#         def helper(node):
#             if node:
#                 helper(node.left)
#                 helper(node.right)
#                 result.append(node.val)
                
#         helper(root)
#         return result

        tempS1 = [root]
        result = []
        
        while tempS1:
            temp = tempS1.pop()
            if temp:
                result.append(temp.val)

                tempS1.append(temp.left)
                tempS1.append(temp.right)
                #print(temp, tempS1, result)
                
        return result[::-1]