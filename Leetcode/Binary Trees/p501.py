## 501. Find Mode in Binary Search Tree

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxFreq = 0
        self.result = []
        self.current = 0
        self.freq = 0
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.result
        
        self.findMode(root.left)
        
        if(self.current != root.val):
            self.current = root.val
            self.freq = 1
        else:
            self.freq+=1
        
        if self.freq > self.maxFreq:
            self.maxFreq= self.freq
            self.result = [self.current]
            
        elif self.freq == self.maxFreq:
            self.result.append(self.current)
        
        self.findMode(root.right)
        
        return self.result