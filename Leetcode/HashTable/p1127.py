## Find Duplicate Subtrees

# Your input

# [1,2,3,4,null,2,4,null,null,4]
# [2,1,1]
# [2,2,2,3,null,3,null]

# Your stdout

# Counter({(4, None, None): 1})
# Counter({(4, None, None): 1, (2, (4, None, None), None): 1})
# Counter({(4, None, None): 2, (2, (4, None, None), None): 1})
# Counter({(4, None, None): 2, (2, (4, None, None), None): 2})
# Counter({(4, None, None): 3, (2, (4, None, None), None): 2})
# Counter({(4, None, None): 3, (2, (4, None, None), None): 2, (3, (2, (4, None, None), None), (4, None, None)): 1})
# Counter({(4, None, None): 3, (2, (4, None, None), None): 2, (3, (2, (4, None, None), None), (4, None, None)): 1, (1, (2, (4, None, None), None), (3, (2, (4, None, None), None), (4, None, None))): 1})
# ------------------------------
# Counter({(1, None, None): 1})
# Counter({(1, None, None): 2})
# Counter({(1, None, None): 2, (2, (1, None, None), (1, None, None)): 1})
# ------------------------------
# Counter({(3, None, None): 1})
# Counter({(3, None, None): 1, (2, (3, None, None), None): 1})
# Counter({(3, None, None): 2, (2, (3, None, None), None): 1})
# Counter({(3, None, None): 2, (2, (3, None, None), None): 2})
# Counter({(3, None, None): 2, (2, (3, None, None), None): 2, (2, (2, (3, None, None), None), (2, (3, None, None), None)): 1})
# ------------------------------

# Your answer
# [[4],[2,4]]
# [[1]]
# [[3],[2,3]]

# Expected answer
# [[2,4],[4]]
# [[1]]
# [[2,3],[3]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        temp=Counter()
        
        def post_order(node):
            if not node:
                return None
            
            node_key = (node.val,post_order(node.left), post_order(node.right))
            temp[node_key]+=1
            #print(temp)
            
            if temp[node_key]==2:
                result.append(node)
                
            return node_key
        
        post_order(root)
        #print('-'*30)
        return result
        