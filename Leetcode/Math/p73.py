## 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        
        def findZeros(matrix, M, N):
            zR, zC = set(),set()
            for i in range(M):
                for j in range(N):
                    if matrix[i][j]==0:
                        zR.add(i)
                        zC.add(j)
                        
            return zR, zC
        
        def printM(matrix, M, N):          
            for i in range(M):
                for j in range(N):
                    print(matrix[i][j],end=' ')
                print('\n')
        
        zeroX, zeroY = findZeros(matrix, M, N)
        #print(zeroX, zeroY)
        for i in range(M):
            if i in zeroX:
                for j in range(N):
                    matrix[i][j]=0
        for j in range(N):
            if j in zeroY:
                for i in range(M):
                    matrix[i][j]=0     
                    
        #print(matrix, M, N)
            
        