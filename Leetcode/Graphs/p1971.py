## 1971. Find if Path Exists in Graph

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source==destination:
            return True
        
        # Create Adjacency List for Graph
        adjList = [[] for _ in range(n)]
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        # BFS for search from source to destination
        tempS = [source]
        visited = set()
        while tempS:
            size = len(tempS)
            for _ in range(size):
                curr = tempS.pop(0)
                visited.add(curr)
                
                for vrtx in adjList[curr]:
                    if vrtx==destination:
                        return True
                    elif vrtx not in visited:
                        tempS.append(vrtx)
                        
        return False
                
                
        # if destination in adjList[source]:
        #     return True
        # else:
        #     return False