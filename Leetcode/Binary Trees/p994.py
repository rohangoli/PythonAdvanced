## Populating Next Right Pointers in Each Node

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
# Input: root = []
# Output: []

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return
        
        tempQ = [root]

        while tempQ:
            size = len(tempQ)
            i=1
            while i<size:
                tempQ[i-1].next = tempQ[i]
                i+=1
            tempQ[i-1].next = None
            
            for _ in range(size):
                curr = tempQ.pop(0)
                
                if curr.left:
                    tempQ.append(curr.left)
                if curr.right:
                    tempQ.append(curr.right)
                    
        return root