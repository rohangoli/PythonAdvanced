## 576. Out of Boundary Paths

# Example 1:
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6

# Example 2:
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        
        @lru_cache(None)
        def helper(posX, posY,moves):
            if moves<0:
                return 0
            
            if posX<0 or posX>=m or posY<0 or posY>=n:
                return 1
            
            return helper(posX+1,posY, moves-1)+helper(posX-1,posY, moves-1)+helper(posX,posY+1, moves-1)+helper(posX,posY-1, moves-1)
        
        return helper(startRow, startColumn, maxMove)%mod
        
    def findPaths_v2(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        #print('-'*20)
        tempQ = [(startRow, startColumn)]
        level = 0
        result = 0
        visited = {}
        reachable = {}
        while tempQ and level<maxMove:
            #print(tempQ)
            size = len(tempQ)
            for _ in range(size):
                currX, currY = tempQ.pop(0)
                if (currX,currY) in visited:
                    #print("Visisted: ",(currX,currY)," value: +",visited[(currX,currY)])
                    tempQ.extend(reachable[(currX,currY)])
                    result+=visited[(currX,currY)]
                    continue
                    
                temp = 0
                tempReach = []
                if 0 <= (currX+1) < m:
                    tempReach.append((currX+1, currY))
                else:
                    temp+=1
                if 0 <= (currX-1) < m:
                    tempReach.append((currX-1, currY))
                else:
                    temp+=1
                if 0 <= (currY+1) < n:
                    tempReach.append((currX, currY+1))
                else:
                    temp+=1 
                if 0 <= (currY-1) < n:
                    tempReach.append((currX, currY-1))
                else:
                    temp+=1
                    
                visited[(currX,currY)]=temp
                reachable[(currX,currY)]=tempReach
                
                result+=temp
                tempQ.extend(tempReach)
                #print("Visisted: ",(currX,currY)," value: +",visited[(currX,currY)])
                
            level+=1
            
        #print(visited)
        return result