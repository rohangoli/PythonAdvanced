## Number of islands - Stack Implementation 

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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        #island_groups = []
        visited = set()
        island_count = 0
        
        ## Stack Implementation
        i=0
        while i<M:
            j=0
            while j<N:
                tempS = []
                if grid[i][j]=='1' and (i,j) not in visited:
                    tempS.append((i,j))
                    island_count+=1
                    # visited.add((i,j))
                
                while tempS:
                    # print(tempS)
                    x,y = tempS[-1]
                    # print(x,y)
                        
                    visited.add((x,y))
                    if y+1<N and grid[x][y+1]=='1' and (x,y+1) not in visited:
                        tempS.append((x,y+1))
                        
                    elif x+1<M and grid[x+1][y]=='1' and (x+1,y) not in visited:
                        tempS.append((x+1,y))
                        
                    elif y-1>=0 and grid[x][y-1]=='1' and (x,y-1) not in visited:
                        tempS.append((x,y-1))
                    
                    elif x-1>=0 and grid[x-1][y]=='1' and (x-1,y) not in visited:
                        tempS.append((x-1,y))

                    else:
                        tempS.pop()
                    
                # print('-'*20)    
                j+=1
            i+=1
        # print('='*50)
        return island_count
        
        ## Queue Implementation
        
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
                # print('-'*20)
                j+=1
            i+=1
        
        # print('='*50)
        return island_count