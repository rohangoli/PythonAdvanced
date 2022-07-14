## 997. Find the Town Judge

# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ## Using Adjacency Matrix
        adjMat = [[False for _ in range(0,n)] for _x in range(0,n)]
        
        for x,y in trust:
            adjMat[x-1][y-1]=True
        
        #print(adjMat)
        findRow = -1
        tempL = [False]*n
        for idx in range(0,n):
            # print(all(adjMat[idx]), any(adjMat[idx]))
            if adjMat[idx]==tempL:
                findRow = idx
                
        if findRow==-1:
            return -1
        
        for idx in range(0,n):
            #print(adjMat[idx][findRow])
            if idx!=findRow and adjMat[idx][findRow]==False:
                return -1
        return findRow+1

