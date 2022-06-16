## Clone Graph - DFS

# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        nodeMap = {node.val: Node(node.val)}
        stack = [node]

        while stack:
            #print([x.val for x in stack])
            curr = stack.pop()
            
            cloneC = nodeMap[curr.val]
            
            for neighbor in curr.neighbors:
                if neighbor.val not in nodeMap:
                    cloneN = Node(neighbor.val)
                    nodeMap[neighbor.val] = cloneN
                    stack.append(neighbor)
                    
                cloneC.neighbors.append(nodeMap[neighbor.val])
                
        return nodeMap[node.val]
        