## 695. Max Area of Island

class Solution:
    def bfs(self, start, visited, M, N, grid):
        tempQ = [start]
        area = 0
        while tempQ:
            size = len(tempQ)
            for _ in range(size):
                currX, currY = tempQ.pop(0)
                
                if (currX, currY) in visited:
                    continue
                
                visited.add((currX, currY))
                area +=1
                
                if 0<=(currX+1)<M and grid[currX+1][currY]==1 and (currX+1, currY) not in visited:
                    tempQ.append((currX+1, currY))
                    
                if 0<=(currX-1)<M and grid[currX-1][currY]==1 and (currX-1, currY) not in visited:
                    tempQ.append((currX-1, currY))
                    
                if 0<=(currY+1)<N and grid[currX][currY+1]==1 and (currX, currY+1) not in visited:
                    tempQ.append((currX, currY+1))
                    
                if 0<=(currY-1)<N and grid[currX][currY-1]==1 and (currX, currY-1) not in visited:
                    tempQ.append((currX, currY-1)) 
                
        return area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        #visited = [[False for _ in range(N)] for _x in range(M)]
        # print(visited)
        
        maxArea = 0
        visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    maxArea = max(maxArea, self.bfs((i,j), visited, M, N, grid))
        
        return maxArea