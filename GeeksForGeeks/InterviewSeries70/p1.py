## BST Downward Traversal
## Find target and return sum of nodes - vertically below the target node

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def verticallyDownBST(root, target):
    #code here
    result = 0
    
    def findTarget(node, target):
        if not node:
            return -1
        elif node.data == target:
            return node
            # result=0
            # if node.left and node.left.right:
            #     result += node.left.right.data
            # if node.right and node.right.left:
            #     result += node.right.left.data
            # return result
        else:
            return findTarget(node.left, target) and findTarget(node.right, target)
            
    def verticalSum(node, hd):
        if not node:
            return None
        else:
            verticalSum(node.left, hd-1)
            if hd==0:
                #print(node.data)
                result+=node.data
            verticalSum(node.right, hd+1)
        
            
    nodeAddr =  findTarget(root, target)
    if nodeAddr == -1:
        return -1
    else:
        verticalSum(nodeAddr, 0)
        
    return result-target


# 35
# 25 20 35 15 22 30 45 N N N N N 32 10 N
# >>> 42

# 35
# 25 20 35 15 22 30 45 N N N N N 32 N N
# >>> 32

# 25
# 25 20 35 15 22 30 45 N N N N N 32 10 N
# >>> 52

## Target not found = -1
# 14
# 22 21 22 12 N N 27 2 N N N N N
# >>> -1

### Failed Test Case
# 18
# 23 2 26 N 18 N N N 18 N 22 N 22 N N
# >>> 0