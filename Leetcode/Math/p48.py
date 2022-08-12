## 48. Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def matT(matrix):
            M = len(matrix)
            N = len(matrix[0])
            
            for i in range(M):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
            return matrix
        
        def printMatrix(matrix):
            M = len(matrix)
            N = len(matrix[0])
            
            print('-'*10)
            for i in range(M):
                for j in range(N):
                    print(matrix[i][j],' ', end='')
                print('\n')
            print('-'*10)
            
        def rowRev(matrix):
            M = len(matrix)
            
            for i in range(M):
                N = 0
                O = len(matrix[i])-1
                while N<O:
                    matrix[i][N],matrix[i][O] = matrix[i][O], matrix[i][N]
                    N+=1
                    O-=1
            return matrix    
            
        matrix = matT(matrix)
        #printMatrix(matrix)
        
        matrix = rowRev(matrix)
        #printMatrix(matrix)