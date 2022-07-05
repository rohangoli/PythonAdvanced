## Symmetric Tree

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return
        
        temp = []
        tempQ = [root]
        while tempQ:
            size = len(tempQ)
            for i in range(size):
                if i==0:
                    temp.append([])
                curr = tempQ.pop(0)
                if curr:
                    temp[-1].append(curr.val)
                    tempQ.append(curr.left)
                    tempQ.append(curr.right)
                else:
                    temp[-1].append(None)
        #print(temp)
        for x in temp[:-1]:
            if x!=x[::-1]:
                return False
        return True