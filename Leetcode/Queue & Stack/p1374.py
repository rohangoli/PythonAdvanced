## Number of Islands

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

## Rohan's Solution with Queue's(for greedy search of land) and HashSet(for visited nodes)
## O(N . M . log MN) - TC
## O(N . M) - SC
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        #island_groups = []
        visited = set()
        island_count = 0
        
        i=0
        while i<M:
            j=0
            while j<N:
                tempQ = []
                # print("({},{}) - {} - {}".format(i,j,grid[i][j],(i,j) in visited))
                if grid[i][j]=='1' and (i,j) not in visited:
                    # island_groups.append([grid[i][j]])
                    tempQ.append((i,j))
                    island_count+=1
                
                while tempQ:
                    # print(tempQ)
                    x,y = tempQ.pop(0)
                    # print(x,y)
                    
                    if (x,y) in visited:
                        continue
                    
                    visited.add((x,y))
                    
                    if x-1>=0 and grid[x-1][y]=='1' and (x-1,y) not in visited:
                        tempQ.append((x-1,y))
                        
                    if x+1<M and grid[x+1][y]=='1' and (x+1,y) not in visited:
                        tempQ.append((x+1,y))
                        
                    if y-1>=0 and grid[x][y-1]=='1' and (x,y-1) not in visited:
                        tempQ.append((x,y-1))
                        
                    if y+1<N and grid[x][y+1]=='1' and (x,y+1) not in visited:
                        tempQ.append((x,y+1))
                #print('-'*20)
                j+=1
            i+=1
        
        #print('='*50)
        return island_count

## Optimal Solution withn only Queue
from collections import deque

class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
                
        nrows = len(grid)
        ncols = len(grid[0])
        islands = 0
        for row in range(nrows):
            for col in range(ncols):                
                if grid[row][col] == "1":
                    islands += 1
                    queue.append((row, col))                    
                    grid[row][col] = "0"                    
                    while queue:                                                
                        r, c = queue.popleft()                        
                        if r < nrows - 1 and grid[r+1][c] == "1":
                            queue.append((r+1, c)) 
                            grid[r+1][c] = "0"                    
                        if c < ncols - 1 and grid[r][c+1] == "1":
                            queue.append((r, c+1)) 
                            grid[r][c+1] = "0"                    
                        if r > 0 and grid[r-1][c] == "1":
                            queue.append((r-1, c)) 
                            grid[r-1][c] = "0"                    
                        if c > 0 and grid[r][c-1] == "1":
                            queue.append((r, c-1)) 
                            grid[r][c-1] = "0"                    
                        
        return islands