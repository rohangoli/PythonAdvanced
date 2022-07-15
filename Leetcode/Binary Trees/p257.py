## 257. Binary Tree Paths

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.result = set()
        
        ## Bottom-Up Approach
#         def helper(node, path):
#             if not node:
#                 return 0
            
# #             if not node.left and not node.right:
# #                 self.result.append('->'.join(path))
            
# #             path.append(str(node.val))
#             left = helper(node.left, path)
#             right = helper(node.right, path)
#             print(node, path, left, right)
#             return 1+max(left,right)
                
#         helper(root, [])

        ## Top-Down Approach
        def helper2(node, path):
            if not node:
                return 
            
            path+=" "+str(node.val)
            if not node.right and not node.left:
                self.result.add(path)
                
            #print(node, path)
            return helper2(node.left, path) or helper2(node.right, path)
            
        helper2(root,"")
           
        self.result = list(self.result)
        for idx,arr in enumerate(self.result):
            self.result[idx] = "->".join(arr.split())
            
        return self.result