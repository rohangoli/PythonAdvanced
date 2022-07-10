## Lowest Common Ancestor of a Binary Tree

## https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/ 

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, root: 'TreeNode', target: 'TreeNode', travelPath : 'List') -> 'List':
        if not root:
            return False
        
        travelPath.append(root)
        if root==target:
            return True
        
        if self.search(root.left, target, travelPath) or self.search(root.right, target, travelPath):
            return True
        
        travelPath.pop(-1)
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        searchP, searchQ = [], []
        self.search(root, p, searchP)
        self.search(root, q, searchQ)
        #print(searchP, searchQ)
        N = min(len(searchP), len(searchQ))
        i=0
        while i<N and searchP[i]==searchQ[i]:
            i+=1
        
        return searchP[i-1]
        