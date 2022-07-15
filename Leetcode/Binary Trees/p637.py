## 637. Average of levels in Binary Tree

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        
        tempQ = [root]
        while tempQ:
            size=len(tempQ)
            tempAvg = 0
            tempNo = 0
            for _ in range(size):
                curr = tempQ.pop(0)
                tempAvg+=curr.val
                tempNo+=1
                
                if curr.left:
                    tempQ.append(curr.left)
                if curr.right:
                    tempQ.append(curr.right)
                    
            result.append(tempAvg/tempNo)
        
        return result