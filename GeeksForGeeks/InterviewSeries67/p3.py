## Target Grid Sum

def gridSum(grid, k):
    #code here
    m,n = len(grid), len(grid[0])
    
    def bfs(x,y,reward):
        
        if x>=m or y>=n:
            return False
        
        reward += grid[x][y]
        if x==m-1 and y==n-1:
            if reward==k:
                return True
            else:
                return False
            
        return bfs(x+1,y,reward) or bfs(x,y+1,reward)
        
    if bfs(0,0,0):
        return 1
    else:
        return 0

print('Case1:')
print(gridSum([[1,-1,1],[-1,-1,1]],0)) #1
print(gridSum([[1,-1,1],[-1,-1,1]],3)) #0
print(gridSum([[1,-1,1],[-1,-1,1]],1)) #0
print(gridSum([[1,-1,1],[-1,-1,1]],2)) #0

print('Case2:')
print(gridSum([[1,-1,-1],[1,1,-1],[-1,-1,1]],3))
print(gridSum([[1,-1,-1],[1,1,-1],[-1,-1,1]],0))
print(gridSum([[1,-1,-1],[1,1,-1],[-1,-1,1]],7))

print('Case3:')
print(gridSum([[1,-1],[1,-1]],0))
print(gridSum([[1,-1],[1,-1]],-1))
print(gridSum([[1,-1],[1,-1]],1))