## Find Center of Star Graph

# Example 1:
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

# Example 2:
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Count Edges
        tempS = set()
        for x,y in edges:
            tempS.add(x)
            tempS.add(y)   
        numEdges = len(tempS)
        
        ## Using Adjancency List Representation - Accepted
        
        adjList = [[] for _ in range(numEdges)]
        
        for x,y in edges:
            adjList[x-1].append(y-1)
            adjList[y-1].append(x-1)
        
        for idx, row in enumerate(adjList):
            if len(row)==numEdges-1:
                return idx+1
        return -1
        
        
#         ## Using Adjancency Matrix - Memory Limit Exceeded
        
#         # Create AdjMat representation for Graph
#         adjMat = [[False for _ in range(numEdges)] for _x in range(numEdges)]
#         for x,y in edges:
#             adjMat[x-1][y-1] = True
#             adjMat[y-1][x-1] = True
        
#         # Check for vertice which has connections to others and but not self
#         for idx, row in enumerate(adjMat):
#             if row.count(True)==numEdges-1 and adjMat[idx][idx]==False:
#                 return idx+1
            
#         return -1