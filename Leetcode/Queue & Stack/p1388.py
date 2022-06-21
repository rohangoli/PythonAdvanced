## 01 Matrix

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# import math
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        M = len(mat)
        N = len(mat[0])
        
        visited = set()
        tempQ = []
        for i in range(M):
            for j in range(N):
                if mat[i][j]==0:
                    tempQ.append((i,j))
                    visited.add((i, j))
                    
                   
        dist = 0
        while tempQ:
            #print("Level: {}\nQueue: {}\nVisited: {}\n".format(dist, tempQ, visited))
            size = len(tempQ)
            for _ in range(size):
                
                (currX, currY) = tempQ.pop(0)
                #print(currX, currY)
                
                mat[currX][currY] = dist
                   
                ## Add Neighbors
                if currX+1 < M and (currX+1, currY) not in visited:
                    tempQ.append((currX+1, currY))
                    visited.add((currX+1, currY))
                if 0 <= currX-1 and (currX-1, currY) not in visited:
                    tempQ.append((currX-1, currY))
                    visited.add((currX-1, currY))
                if currY+1 < N and (currX, currY+1) not in visited:
                    tempQ.append((currX, currY+1))
                    visited.add((currX, currY+1))
                if 0 <= currY-1 and (currX, currY-1) not in visited:
                    tempQ.append((currX, currY-1))
                    visited.add((currX, currY-1))
                    
            dist+=1
        #print('-'*25)    
        return mat
                
        
#         def helper(row, col, level):
#             #print("R:{} C:{} L:{}".format(row,col,level))
#             if row<0 or row>M-1 or col<0 or col>N-1 or level>M+N:
#                 return math.inf
#             elif mat[row][col]==0:
#                 return level
                        
#             return min(helper(row,col-1,level+1),
#                        helper(row-1,col,level+1),
#                        helper(row+1,col,level+1),
#                        helper(row,col+1,level+1))
#         i=0
#         visitedHM = {}
#         while i<M:
#             j=0
#             while j<N:
#                 mat[i][j] = helper(i,j,0)                    
#                 #print("row:{} col:{} val: {}".format(i,j,mat[i][j]))
#                 #print('-'*10)
#                 j+=1
#             #print("="*20)
#             i+=1
         
#         #print(mat)
#         #print('*'*50)
#         return mat